#!/usr/bin/env python3.8

import os
import sys
import logging

def check_asset(asset: str) -> None:
    pass

def get_pyramid_from_asset(asset: str) -> tuple:
    return ()

def main() -> None:
    if len(sys.argv) > 1:
        assets = sys.argv[1:]
        for asset in assets:
            check_asset(asset)
    else:
        assets = [os.path.join("assets", asset) for asset in os.listdir("assets")]

if __name__ == "__main__":
    main()
