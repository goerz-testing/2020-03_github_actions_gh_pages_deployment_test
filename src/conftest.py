"""Set up the environment for doctests

This file is automatically evaluated by py.test. It ensures that we can write
doctests without distracting import statements in the doctest.
"""
import pytest

import github_actions_gh_pages_deployment_test


@pytest.fixture(autouse=True)
def set_doctest_env(doctest_namespace):
    doctest_namespace[
        'github_actions_gh_pages_deployment_test'
    ] = github_actions_gh_pages_deployment_test
