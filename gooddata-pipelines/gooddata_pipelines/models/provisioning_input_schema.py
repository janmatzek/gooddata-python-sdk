# (C) 2025 GoodData Corporation

"""This module contains input schemas for provisioning scripts."""

from typing import TypedDict


# Workspace provisioning input schemas
class WorkspaceFullLoadSchema(TypedDict):
    parent_id: str
    workspace_id: str
    workspace_name: str
    workspace_data_filter_id: str | None
    workspace_data_filter_values: list[str] | None


class WorkspaceIncrementalLoadSchema(TypedDict):
    parent_id: str
    workspace_id: str
    workspace_name: str
    workspace_data_filter_id: str | None
    workspace_data_filter_values: list[str] | None
    is_active: bool


# User provisioning input schemas
class UserFullLoadSchema(TypedDict):
    user_id: str
    firstname: str | None
    lastname: str | None
    email: str | None
    auth_id: str | None
    user_groups: list[str]


class UserIncrementalLoadSchema(TypedDict):
    user_id: str
    firstname: str | None
    lastname: str | None
    email: str | None
    auth_id: str | None
    user_groups: list[str]
    is_active: bool


# User group provisioning input schemas
class UserGroupFullLoadSchema(TypedDict):
    user_group_id: str
    user_group_name: str | None
    parent_user_groups: list[str] | None  # NOTE: Use NotRequired in Python 3.11


class UserGroupIncrementalLoadSchema(TypedDict):
    user_group_id: str
    user_group_name: str | None
    parent_user_groups: list[str] | None  # NOTE: Use NotRequired in Python 3.11
    is_active: bool


# Worksapce permission provisioning input schemas
class PermissionFullLoadSchema(TypedDict):
    user_id: str | None
    user_group_id: str | None
    workspace_id: str
    permission: str


class PermissionIncrementalLoadSchema(TypedDict):
    user_id: str | None
    user_group_id: str | None
    workspace_id: str
    permission: str
    is_active: bool
