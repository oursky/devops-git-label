from typing import List
from github import (
    Github,
    Repository,
    UnknownObjectException,
)
from label import Label


class GithubIssueCreator():
    _verbose: bool
    _github: Github
    _slug: str

    def __init__(self, github_token: str, slug: str, verbose: bool = False):
        self._verbose = verbose
        self._github = Github(github_token)
        self._slug = slug

    def create_labels(self, labels: List[Label]) -> bool:
        repo = self._github.get_repo(self._slug)
        for label in labels:
            self._create_label(repo, label)

    def _create_label(self, repo: Repository, label: Label) -> bool:
        try:
            github_label = repo.get_label(label.name)
            if self._verbose:
                print("[I] Edit existing label: {}".format(label.name))
            github_label.edit(name=label.name, color=label.color, description=label.description)
        except UnknownObjectException:
            try:
                if self._verbose:
                    print("[I] Creating label {}".format(label.name))
                label = repo.create_label(label.name, label.color, label.description)
            except Exception as e:
                print("[E] Error creating label {}".format(label.name), str(e))
                return False
        return True
