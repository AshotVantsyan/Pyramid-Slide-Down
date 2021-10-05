#!/usr/bin/env python3.8

import os
import sys
import json
import logging
from typing import List

from pyramid_slide_down import longest_slide_down


def check_asset_validity(asset: str) -> None:
    """
    Check if asset is a valid file in JSON format.
    """
    if not os.path.isfile(asset):
        logging.error("'%s' doesn't exist", asset)
        sys.exit(2)
    try:
        with open(asset, 'r', encoding='utf-8') as file:
            json.load(file)
    except ValueError as error:
        logging.error("Invalid JSON is provided.")
        logging.error("Asset: %s", asset)
        logging.error(error)
        sys.exit(3)


def get_assets(arguments: List[str]) -> List[str]:
    """
    Retrurn list of files containing pyramids in JSON format.
    If no input argument is provided, JSON-s under 'assets' directory will be used.
    """
    assets = arguments
    if arguments:
        for asset in arguments:
            check_asset_validity(asset)
    elif os.path.isdir("assets"):
        assets = [os.path.join("assets", asset) for asset in os.listdir("assets")]
    else:
        logging.error("'assets' directory hasn't not found")
        sys.exit(1)
    logging.info("Selected asset(s): %s", ", ".join(assets))
    return assets


def get_pyramid_from_asset(asset: str) -> List[List[int]]:
    """
    The function gets file containing the pyramid in JSON format, validates and return as a list of lists.
    """
    with open(asset, 'r', encoding='utf-8') as file:
        pyramid: List[List[int]] = json.load(file)
    for count, row in enumerate(pyramid, start=1):
        if count != len(row):
            logging.error("Invalid pyramid. Expected %s elements "
                          "at %s row, got %s", count, count, len(row))
            sys.exit(4)
    return pyramid


def main() -> None:
    """
    Entrypoint function for the project.
    """
    logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.INFO)
    assets = get_assets(sys.argv[1:])
    pyramids = [get_pyramid_from_asset(asset) for asset in assets]
    for i, pyramid in enumerate(pyramids):
        max_path_sum = longest_slide_down(pyramid)
        logging.info("Asset: %s, Longest Slide Down: %s", assets[i], max_path_sum)

if __name__ == "__main__":
    main()
