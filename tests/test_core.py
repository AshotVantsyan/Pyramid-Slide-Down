#!/usr/bin/env pytest

"""
The test validates core functionality.
"""

import os
import pytest

from helpers import get_pyramid_from_file
from src.pyramid_slide_down import longest_slide_down


@pytest.mark.parametrize("size,expected", [("minor", 23), ("middle", 1074), ("major", 7273)])
def test_core(size, expected):
    """Test core function with small/medium and huge pyramids"""
    pyramid = get_pyramid_from_file(os.path.join("assets", f"{size}_pyramid.json"))
    assert longest_slide_down(pyramid) == expected, "Invalid longest path."
