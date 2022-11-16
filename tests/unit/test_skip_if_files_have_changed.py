from pytest_delta import skip_if_files_have_not_changed


class TestSkipIfFilesHaveNotChanged:
    @skip_if_files_have_not_changed(
        files=["pytest_delta/latest_git_commit_files_have_changed.py"]
    )
    def should_do_whatever(self):
        assert True is True
