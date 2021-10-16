#!/usr/bin/env pytest

"""
The module contains necessary configurations and fixtures for the tests.
This module is run automatically by 'pytest' during any running session.
"""

import os
import sys
import logging
import pytest

sys.path.append('src')

@pytest.fixture(scope="function", autouse=True)
def rewrite_argv():
    """
    The fixture is used to mock 'sys.argv' list for testing purposes.
    """
    original_argv = sys.argv.copy()
    yield
    sys.argv = original_argv.copy()

@pytest.fixture(scope="function", autouse=True)
def capture_log(caplog: pytest.LogCaptureFixture):
    """
    The fixture is used to catch logging calls of entrypoint.
    """
    caplog.set_level(logging.INFO)


@pytest.fixture(scope="function")
def change_directory():
    """
    The fixture is used to run test case in a specific directory.
    """
    cwd = os.getcwd()
    os.chdir(os.path.dirname(__file__))
    yield
    os.chdir(cwd)
