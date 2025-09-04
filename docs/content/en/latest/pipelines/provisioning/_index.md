---
title: "Provisioning"
linkTitle: "Provisioning"
weight: 1
no_list: true
---

Manage resources in GoodData.


## Supported Resources

Resources you can provision using GoodData Pipelines:

- [Workspaces](./workspaces.md)
- [Users](users.md)
- [User Groups](user_groups.md)
- [Workspace Permissions](workspace-permissions.md)


## Workflow Types

There are two types of provisioning supported by GoodData Pipelines:

- [Full load](#full-load)
- [Incremental load](#incremental-load)

The provisioning types employ different algorithms and expect different structure of input data. For details about the expected inputs, check out the documentation page of individual provisioned resource.

### Full Load

Full load provisioning aims to fully synchronize the state of your GoodData instance with the provided input. This workflow will create new resources and update existing ones based on the input. Any resources existing on GoodData Cloud not inluded in the input will be deleted.

### Incremental Load

During incremental provisioning, the algorithm will only interact with resources specified in the input. During the incremental load, the input data expects an extra parameter: `is_active`. Resources with `True` value will be updated. On the other hand, by setting it to `False`, you can mark resources for deletion. Any other resources already existing in GoodData will not be altered.
