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
