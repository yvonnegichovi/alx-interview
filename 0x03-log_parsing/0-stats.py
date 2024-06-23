#!/usr/bin/python3
"""
This script reads stdin line by line and computes metrics
"""

import signal
import sys


def handle_signal():
    """
    Handles signal
    """
    signal.sigint


with open('filename', 'r', encoding="utf-8") as f:
    read_data = f.read()
