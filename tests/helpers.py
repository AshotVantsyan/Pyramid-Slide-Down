#!/usr/bin/env python3.8

import json
from typing import List

def get_pyramid_from_file(file_path: str) -> List[List[int]]:
    """
    The helper function returns pyramid object.
    Valid file path must be specified.
    """
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)