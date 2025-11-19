# Snapshot Tool

Simple system snapshot tool that writes system metrics to JSON and console.

## Installation

```bash
pip install -U ./snapshot-util

Usage

Run the tool with optional arguments:

snapshot -i 1 -f snapshot.json -n 5

Options

    -i Interval between snapshots in seconds (default: 30)

    -f Output file name (default: snapshot.json)

    -n Number of snapshots to output (default: 20)
