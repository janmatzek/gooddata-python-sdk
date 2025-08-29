# (C) 2025 GoodData Corporation

from pydantic import BaseModel, Field, field_validator

from gooddata_pipelines.models.provisioning_input_schema import (
    UserGroupFullLoadSchema,
    UserGroupIncrementalLoadSchema,
)
from gooddata_pipelines.provisioning.utils.utils import (
    ConstructorMixin,
)


class UserGroupBase(BaseModel):
    user_group_id: str
    user_group_name: str
    parent_user_groups: list[str] = Field(default_factory=list)

    @field_validator("user_group_name", mode="before")
    @classmethod
    def validate_user_group_name(cls, v: str | None, info) -> str:
        """If user_group_name is None or empty, default to user_group_id."""
        if not v:  # handles None and empty string
            return info.data.get("user_group_id", "")
        return v

    @field_validator("parent_user_groups", mode="before")
    @classmethod
    def validate_parent_user_groups(
        cls, v: list[str] | None, info
    ) -> list[str]:
        """If parent_user_groups is None or empty, default to empty list."""
        if not v:
            return []
        return v


class UserGroupIncrementalLoad(
    UserGroupBase, ConstructorMixin[UserGroupIncrementalLoadSchema]
):
    """Input validator for incremental load of user group provisioning.

    To validate the input, use the `from_list_of_dicts` method. The input should
    be a list of dictionaries that match that match `gooddata_pipelines.models.provisioning_input_schema.UserGroupIncrementalLoadSchema`.
    """

    is_active: bool


class UserGroupFullLoad(
    UserGroupBase, ConstructorMixin[UserGroupFullLoadSchema]
):
    """Input validator for full load of user group provisioning.

    To validate the input, use the `from_list_of_dicts` method. The input should
    be a list of dictionaries that match that match `gooddata_pipelines.models.provisioning_input_schema.UserGroupFullLoadSchema`.
    """
