"""Tests for `github_actions_gh_pages_deployment_test` package."""

import pytest
from pkg_resources import parse_version

import github_actions_gh_pages_deployment_test


def test_valid_version():
    """Check that the package defines a valid ``__version__``."""
    v_curr = parse_version(github_actions_gh_pages_deployment_test.__version__)
    v_orig = parse_version("0.1.0-dev")
    assert v_curr >= v_orig
