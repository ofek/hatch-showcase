# hatch-showcase

| | |
| --- | --- |
| CI/CD | [![CI - Test](https://github.com/ofek/hatch-showcase/actions/workflows/test.yml/badge.svg)](https://github.com/ofek/hatch-showcase/actions/workflows/test.yml) [![CD - Build](https://github.com/ofek/hatch-showcase/actions/workflows/build.yml/badge.svg)](https://github.com/ofek/hatch-showcase/actions/workflows/build.yml) |
| Package | [![PyPI - Version](https://img.shields.io/pypi/v/hatch-showcase.svg?logo=pypi&label=PyPI&logoColor=gold)](https://pypi.org/project/hatch-showcase/) [![PyPI - Python Version](https://img.shields.io/pypi/pyversions/hatch-showcase.svg?logo=python&label=Python&logoColor=gold)](https://pypi.org/project/hatch-showcase/) |
| Meta | [![code style - black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black) [![types - Mypy](https://img.shields.io/badge/types-Mypy-blue.svg)](https://github.com/ambv/black) [![imports - isort](https://img.shields.io/badge/imports-isort-ef8336.svg)](https://github.com/pycqa/isort) [![License - MIT](https://img.shields.io/badge/license-MIT-9400d3.svg)](https://spdx.org/licenses/) [![GitHub Sponsors](https://img.shields.io/github/sponsors/ofek?logo=GitHub%20Sponsors&style=social)](https://github.com/sponsors/ofek) |

-----

This project is meant to showcase various features and plugins for [Hatch](https://github.com/ofek/hatch) as well as providing a place to test experimental functionality.

**Table of Contents**

- [Installation](#installation)
- [Environments](#environments)
- [Build](#build)
- [License](#license)

## Installation

```console
pip install hatch-showcase
```

## Environments

- Defined neatly in a standalone [`hatch.toml`](https://ofek.dev/hatch/latest/intro/#configuration)
- The `test` matrix uses the [hatch-containers](https://github.com/ofek/hatch-containers) plugin to run each environment inside Docker containers; usage can be seen in the [test](.github/workflows/test.yml) GitHub workflow

## Build

- Wheels use the [hatch-mypyc](https://github.com/ofek/hatch-mypyc) build hook plugin to first compile all code with [Mypyc](https://github.com/mypyc/mypyc)
- The [build](.github/workflows/build.yml) GitHub workflow shows:
  - how to use [cibuildwheel](https://github.com/pypa/cibuildwheel) to distribute binary wheels for every platform
  - how to disable build hooks in order to build pure Python wheels

## License

`hatch-showcase` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.
