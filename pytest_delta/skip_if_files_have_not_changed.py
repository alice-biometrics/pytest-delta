import os
from typing import List

import pytest

from pytest_delta.latest_git_commit_files_have_changed import (
    latest_git_commit_files_have_changed,
)

PYTEST_DELTA_TESTING_ENABLED = bool(os.getenv("PYTEST_DELTA_TESTING_ENABLED", "True"))


def skip_if_files_have_not_changed(files: List[str]):
    return pytest.mark.skipif(
        not latest_git_commit_files_have_changed(files)
        and PYTEST_DELTA_TESTING_ENABLED,
        reason=f"Skip as {files} do not change",
    )
