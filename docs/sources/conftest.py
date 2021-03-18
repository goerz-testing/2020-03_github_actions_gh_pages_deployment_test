"""This file is automatically executed by pytest when testing anything in the
docs folder"""
import pytest

import github_actions_gh_pages_deployment_test


@pytest.fixture(autouse=True)
def set_doctest_env(doctest_namespace):
    """Inject package itself into doctest namespace.

    This is so we don't need

    .. doctest::

        >>> import github_actions_gh_pages_deployment_test

    in any doctests
    """
    doctest_namespace['github_actions_gh_pages_deployment_test'] = github_actions_gh_pages_deployment_test
