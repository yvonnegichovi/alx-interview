#!/usr/bin/python3
"""
This script reads stdin line by line and computes metrics
"""

import signal
import sys


total_size = 0
status_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

def print_stats():
    global total_size, status_counts
    print(f"File size: {total_size}")
    for status_code in sorted(status_counts.keys()):
        if status_counts[status_code] > 0:
            print(f"{status_code}: {status_counts[status_code]}")


def signal_handler(sig, frame):
    """
    Handles signal
    """
    print_stats()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        line_count += 1
        parts = line.split()
        
        if len(parts) < 9:
            continue
        
        ip = parts[0]
        date = parts[3][1:] + " " + parts[4][:-1]
        request = " ".join(parts[5:8])
        status_code = parts[8]
        file_size = parts[9]

        if request != '"GET /projects/260 HTTP/1.1"':
            continue
        
        try:
            file_size = int(file_size)
            total_size += file_size
        except ValueError:
            continue

        try:
            status_code = int(status_code)
            if status_code in status_counts:
                status_counts[status_code] += 1
        except ValueError:
            continue
        
        if line_count % 10 == 0:
            print_stats()

except KeyboardInterrupt:
    print_stats()
    sys.exit(0)

print_stats()
