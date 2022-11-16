# pytest delta

[![version](https://img.shields.io/github/release/alice-biometrics/pytestdelta/all.svg)](https://github.com/alice-biometrics/pytestdelta/releases) 
[![ci](https://github.com/alice-biometrics/pytestdelta/workflows/ci/badge.svg)](https://github.com/alice-biometrics/pytestdelta/actions) 
[![pypi](https://img.shields.io/pypi/dm/pytestdelta)](https://pypi.org/project/pytestdelta/) 
[![codecov](https://codecov.io/gh/alice-biometrics/meiga/branch/main/graph/badge.svg?token=BX1IZJZLJQ)](https://codecov.io/gh/alice-biometrics/pytestdelta)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)
[![license](https://img.shields.io/github/license/alice-biometrics/pytestdelta.svg)](https://github.com/alice-biometrics/pytestdelta/blob/main/LICENSE)
[![versions](https://img.shields.io/pypi/pyversions/pytestdelta.svg)](https://github.com/alice-biometrics/pytestdelta)

<img src="https://github.com/alice-biometrics/custom-emojis/blob/master/images/alice_header.png?raw=true" width=auto>


## What is pytest-delta?

`pytest-delta` is a plugin to run your tests only when selected files are changed.

## Installation 💻

```console
pip install pytest-delta
```

## Usage

```python
from pytest_delta import skip_if_files_have_not_changed


@skip_if_files_have_not_changed(files=["my_specific_file.py"])
def test_should_do_whatever():
    print("Runnint the test")
```

You can use the envvar `PYTEST_DELTA_TESTING_ENABLED` to enable or disable pytest decorators

```
export PYTEST_DELTA_TESTING_ENABLED=True
export PYTEST_DELTA_TESTING_ENABLED=False
```

## Contribute 

We'd love you to contribute to *pytest-delta* 🥳🥳🥳🥳🥳🥳️️!

For more information, check our [documentation](https://alice-biometrics.github.io/pytestdelta/contributing/)

## Contact 📬

support@alicebiometrics.com
