from typing import List

from git import Repo


def latest_git_commit_files_have_changed(files: List[str]) -> bool:

    try:
        repo = Repo(".")

        # Check differences between current files and last commit
        # diff = repo.git.diff(repo.head.commit.tree)

        commits_list = list(repo.iter_commits())

        # --- To compare the current HEAD against the bare init commit
        a_commit = commits_list[0]
        b_commit = commits_list[-1]

        diff = a_commit.diff(b_commit)

        for file in files:
            if file in diff:
                return True
    except Exception as exc:
        print(f"Warning (pytest-delta): {str(exc)}")

    return False
