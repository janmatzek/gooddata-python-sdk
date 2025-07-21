[![Build Python Package and Create Release](https://github.com/gooddata/gooddata-python-sdk/actions/workflows/build-release.yaml/badge.svg)](https://github.com/gooddata/gooddata-python-sdk/actions/workflows/build-release.yaml)
[![docs](https://github.com/gooddata/gooddata-python-sdk/actions/workflows/docs.yaml/badge.svg)](https://github.com/gooddata/gooddata-python-sdk/actions/workflows/docs.yaml)
[![tests](https://github.com/gooddata/gooddata-python-sdk/actions/workflows/tests.yaml/badge.svg)](https://github.com/gooddata/gooddata-python-sdk/actions/workflows/tests.yaml)
[![codecov](https://codecov.io/gh/gooddata/gooddata-python-sdk/branch/master/graph/badge.svg?token=9C602ASR4Q)](https://codecov.io/gh/gooddata/gooddata-python-sdk)
[![FOSSA Status](https://app.fossa.com/api/projects/git%2Bgithub.com%2Fjanmatzek%2Fgooddata-python-sdk.svg?type=shield)](https://app.fossa.com/projects/git%2Bgithub.com%2Fjanmatzek%2Fgooddata-python-sdk?ref=badge_shield)

# GoodData Cloud Python Foundations

This repository contains Python packages useful for integration with [GoodData Cloud](https://www.gooddata.com/docs/cloud/).

## Available packages

### GoodData API Client

API client is generated directly from the Good Data Cloud OpenAPI specifications and allow you to call any API from
Python. Learn more about the clients in their [dedicated readme](./clients_README.md).

### GoodData Python SDK

The [gooddata-sdk](./gooddata-sdk) package provides a clean and convenient Python API to interact with GoodData.CN.

Check out the GoodData Python SDK [documentation](https://www.gooddata.com/docs/python-sdk) to learn more and get started.

### GoodData Pandas

The [gooddata-pandas](./gooddata-pandas) package is a thin layer that utilizes Python SDK and allows you to conveniently
create pandas series and data frames.

Check out the GoodData Pandas [documentation](https://gooddata-pandas.readthedocs.io/en/latest/) to learn more and get started.

### GoodData FlexConnect

The [gooddata-flexconnect](./gooddata-flexconnect) package is the foundation for writing custom FlexConnect data sources.

Check out the GoodData FlexConnect [documentation](https://www.gooddata.com/docs/cloud/connect-data/create-data-sources/flexconnect/) to learn more and get started.

### GoodData Foreign Data Wrapper

> [!WARNING]
> GoodData Foreign Data Wrapper is currently deprecated.

The [gooddata-fdw](./gooddata-fdw) package provides a way
to map GoodData Cloud semantic layer and/or visualizations stored in your GoodData Cloud
into PostgreSQL as foreign tables that you can then query using SQL.

Check out the GoodData Foreign Data Wrapper [documentation](https://gooddata-fdw.readthedocs.io/en/latest/) to learn more and get started.

## Contributing
If you would like to improve, extend or fix a feature in the repository, read and follow the
[Contributing guide](./CONTRIBUTING.md).


## License
[![FOSSA Status](https://app.fossa.com/api/projects/git%2Bgithub.com%2Fjanmatzek%2Fgooddata-python-sdk.svg?type=large)](https://app.fossa.com/projects/git%2Bgithub.com%2Fjanmatzek%2Fgooddata-python-sdk?ref=badge_large)