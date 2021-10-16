#!/usr/bin/env pytest

"""
The test validates entrypoint of the project.
"""

import os
import sys
import pytest

from helpers import get_expected_data_from_file, get_actual_message
from src.main import main as entrypoint

def test_entrypoint_1(caplog):
    """Test project entrypoint default behavior"""
    sys.argv = ("")
    entrypoint()
    actual_output = get_actual_message(caplog)
    expected_output = get_expected_data_from_file("default.txt")
    assert actual_output == expected_output

@pytest.mark.usefixtures("change_directory")
def test_entrypoint_2(caplog):
    """Test project entrypoint with default behavior when 'assets' directory is not found."""
    sys.argv = ("")
    with pytest.raises(SystemExit) as exception:
        entrypoint()
    assert exception.value.code == 1
    actual_output = get_actual_message(caplog)
    expected_output = get_expected_data_from_file("no_assets_directory.txt")
    assert actual_output == expected_output

def test_entrypoint_3(caplog):
    """Test project entrypoint with non-existing asset"""
    sys.argv = ("", "non-existing-asset.json")
    with pytest.raises(SystemExit) as exception:
        entrypoint()
    assert exception.value.code == 2
    actual_output = get_actual_message(caplog)
    expected_output = get_expected_data_from_file("non-existing_asset.txt")
    assert actual_output == expected_output

def test_entrypoint_4(caplog):
    """Test project entrypoint with invalid asset"""
    sys.argv = ("", os.path.join("tests", "input", "invalid_asset.json"))
    with pytest.raises(SystemExit) as exception:
        entrypoint()
    assert exception.value.code == 3
    actual_output = get_actual_message(caplog)
    expected_output = get_expected_data_from_file("invalid_asset.txt")
    assert actual_output == expected_output

@pytest.mark.parametrize("index", (1, 2))
def test_entrypoint_5(caplog, index):
    """Test project entrypoint when incorrect pyramid is provided"""
    sys.argv = ("", os.path.join("tests", "input", f"invalid_pyramid_{index}.json"))
    with pytest.raises(SystemExit) as exception:
        entrypoint()
    assert exception.value.code == 4
    actual_output = get_actual_message(caplog)
    expected_output = get_expected_data_from_file(f"invalid_pyramid_{index}.txt")
    assert actual_output == expected_output

def test_entrypoint_6(caplog):
    """Test project entrypoint with valid asset"""
    sys.argv = ("", os.path.join("assets", "minor_pyramid.json"))
    entrypoint()
    actual_output = get_actual_message(caplog)
    expected_output = get_expected_data_from_file("valid_asset.txt")
    assert actual_output == expected_output
