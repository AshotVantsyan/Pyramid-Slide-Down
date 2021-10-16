#!/usr/bin/env python3.8

"""
The module for helper functions/classes implemention which will be used in tests.
"""

import os
import json
from typing import List
import pytest


def check_directory_availability(directory_path: str) -> None:
    """
    Make sure that provided directory exists.
    """
    if not os.path.isdir(directory_path):
        raise NotADirectoryError(f"No such directory: {directory_path}")


def check_file_availability(file_path: str) -> None:
    """
    Make sure that provided path is a regular file and is readable
    """
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"No such file: {file_path}")
    if not os.access(file_path, os.R_OK):
        raise PermissionError(f"Unable to read file: {file_path}")


def escape_separators(text: str) -> str:
    """
    Escape path and line separator characters and return unified result.
    """
    text = text.replace(os.sep, "/")
    text = text.replace(os.linesep, "\n")
    return text


def get_pyramid_from_file(file_path: str) -> List[List[int]]:
    """
    The function returns pyramid object.
    Valid file path must be specified.
    """
    check_file_availability(file_path)
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)


def get_expected_data_from_file(file_name: str) -> str:
    """
    The function reads the data from expected file and returns as string.
    Destination directory for the files is './expected' directory
    """
    expected_directory = os.path.join(os.path.dirname(__file__), "expected")
    check_directory_availability(expected_directory)
    expected_file = os.path.join(expected_directory, file_name)
    check_file_availability(expected_file)
    with open(expected_file, "r", encoding="utf-8") as file:
        return escape_separators(file.read())


def get_actual_message(caplog: pytest.LogCaptureFixture) -> str:
    """
    Get entrypoint output message by capturing logging module.
    """
    return escape_separators(os.linesep.join(caplog.messages))
