# (C) 2025 GoodData Corporation

from typing import Any

from gooddata_sdk.catalog.user.entity_model.user import CatalogUser
from pydantic import BaseModel

from gooddata_pipelines.models.provisioning_input_schema import (
    UserFullLoadSchema,
    UserIncrementalLoadSchema,
)
from gooddata_pipelines.provisioning.utils.utils import (
    ConstructorMixin,
)


class BaseUser(BaseModel):
    """Base class containing shared user fields and functionality."""

    user_id: str
    firstname: str | None
    lastname: str | None
    email: str | None
    auth_id: str | None
    user_groups: list[str]
    # TODO: docstring

    @classmethod
    def _create_from_sdk_data(cls, obj: CatalogUser) -> dict[str, Any]:
        """Helper method to extract common data from SDK object."""
        if obj.attributes:
            firstname = obj.attributes.firstname
            lastname = obj.attributes.lastname
            email = obj.attributes.email
            auth_id = obj.attributes.authentication_id
        else:
            firstname = None
            lastname = None
            email = None
            auth_id = None

        return {
            "user_id": obj.id,
            "firstname": firstname,
            "lastname": lastname,
            "email": email,
            "auth_id": auth_id,
            "user_groups": [ug.id for ug in obj.user_groups],
        }

    def to_sdk_obj(self) -> CatalogUser:
        """Converts to CatalogUser SDK object."""
        return CatalogUser.init(
            user_id=self.user_id,
            firstname=self.firstname,
            lastname=self.lastname,
            email=self.email,
            authentication_id=self.auth_id,
            user_group_ids=self.user_groups,
        )


class UserIncrementalLoad(
    BaseUser, ConstructorMixin[UserIncrementalLoadSchema]
):
    """Input validator for incremental load of user provisioning.

    To validate the input, use the `from_list_of_dicts` method. The input should
    be a list of dictionaries that match that match `gooddata_pipelines.models.provisioning_input_schema.UserIncrementalLoadSchema`.
    """

    is_active: bool

    @classmethod
    def from_sdk_obj(cls, obj: CatalogUser) -> "UserIncrementalLoad":
        """Creates GDUserTarget from CatalogUser SDK object."""
        base_data = cls._create_from_sdk_data(obj)
        base_data["is_active"] = True
        return cls(**base_data)


class UserFullLoad(BaseUser, ConstructorMixin[UserFullLoadSchema]):
    """Input validator for full load of user provisioning.

    To validate the input, use the `from_list_of_dicts` method. The input should
    be a list of dictionaries that match that match `gooddata_pipelines.models.provisioning_input_schema.UserFullLoadSchema`.
    """

    @classmethod
    def from_sdk_obj(cls, obj: CatalogUser) -> "UserFullLoad":
        """Creates GDUserTarget from CatalogUser SDK object."""
        base_data = cls._create_from_sdk_data(obj)
        return cls(**base_data)
