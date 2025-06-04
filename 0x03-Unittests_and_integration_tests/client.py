#!/usr/bin/env python3
from utils import get_json

class GithubOrgClient:
    """Github org client."""

    def __init__(self, org_name):
        self.org_name = org_name

    @property
    def org(self):
        """Return the org info by calling get_json."""
        return get_json(f"https://api.github.com/orgs/{self.org_name}")

