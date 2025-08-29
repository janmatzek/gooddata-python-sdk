# (C) 2025 GoodData Corporation

"""Module for utilities used in GoodData Pipelines provisioning."""

from typing import Any, Generic, Mapping, Type, TypeVar

import attrs
from requests import Response

ConstructorType = TypeVar("ConstructorType", bound="ConstructorMixin")
InputTypedDict = TypeVar("InputTypedDict", bound=Mapping[str, Any])


class AttributesMixin:
    """
    Mixin class to provide a method for getting attributes of an object which may or may not exist.
    """

    @staticmethod
    def get_attrs(
        *objects: object, overrides: dict[str, str] | None = None
    ) -> dict[str, str]:
        """
        Returns a dictionary of attributes from the given objects.

        Args:
            objects: The objects to get the attributes from. Special handling is implemented for
                    requests.Response, __dict__ attribute is used for general objects.
            overrides: A dictionary of attributes to override the object's attributes.
        Returns:
            dict: Returns a dictionary of the objects' attributes.
        """
        # TODO: This might not work great with nested objects, values  which are lists of objects etc.
        # If we care about parsing the logs back from the string, we should consider some other approach
        attrs: dict[str, str] = {}
        for context_object in objects:
            if isinstance(context_object, Response):
                # for request.Response objects, keys need to be renamed to match the log schema
                attrs.update(
                    {
                        "http_status": str(context_object.status_code),
                        "http_method": getattr(
                            context_object.request, "method", "NA"
                        ),
                        "api_endpoint": getattr(
                            context_object.request, "url", "NA"
                        ),
                    }
                )
            else:
                # Generic handling for other objects
                for key, value in context_object.__dict__.items():
                    if value is None:
                        continue

                    if isinstance(value, list):
                        attrs[key] = ", ".join(
                            str(list_item) for list_item in value
                        )
                    else:
                        attrs[key] = str(value)

        if overrides:
            attrs.update(overrides)

        return attrs


class ConstructorMixin(Generic[InputTypedDict]):
    @classmethod
    def from_list_of_dicts(
        cls: Type[ConstructorType], data: list[InputTypedDict] | Any
    ) -> list[ConstructorType]:
        """Creates a list of instances from list of dicts.

        Allowed input structures are outlined in `gooddata_pipelines.models.provisioning_input_schema`.
        """
        # NOTE: We can use typing.Self for the return type in Python 3.11
        if not data:
            raise TypeError("Data is empty")

        if not isinstance(data, list):
            raise TypeError("Data is not a list")

        if not all(isinstance(item, dict) for item in data):
            raise TypeError("Data is not a list of dictionaries")

        model_instances: list[ConstructorType] = []
        for dictionary in data:
            model_instances.append(cls.from_dict(dictionary))
        return model_instances

    @classmethod
    def from_dict(
        cls: Type[ConstructorType], data: InputTypedDict
    ) -> ConstructorType:
        """Returns an instance of WorkspaceIncrementalLoad from a dictionary.

        Allowed input structures are outlined in `gooddata_pipelines.models.provisioning_input_schema`.
        """
        return cls(**data)


@attrs.define
class EntityGroupIds:
    ids_in_both_systems: set[str]
    ids_to_delete: set[str]
    ids_to_create: set[str]
