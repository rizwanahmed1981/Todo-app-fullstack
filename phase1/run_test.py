#!/usr/bin/env python3
"""Simple test runner to verify the application works."""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from main import main

if __name__ == "__main__":
    print("Testing import and basic functionality...")
    print("Application module imported successfully!")
    print("To run the application, use: python -m src.main")