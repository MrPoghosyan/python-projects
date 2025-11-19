"""
Make snapshot

{"Tasks": {"total": 440, "running": 1, "sleeping": 354, "stopped": 1, "zombie": 0},
"%CPU": {"user": 14.4, "system": 2.2, "idle": 82.7},
"KiB Mem": {"total": 16280636, "free": 335140, "used": 11621308},
"KiB Swap": {"total": 16280636, "free": 335140, "used": 11621308},
"Timestamp": 1624400255}
"""

import argparse
import psutil
import time
import json
import os

class Snapshot:
    """Class to create system snapshots."""

    def __init__(self, output_file="snapshot.json"):
        # Initialize the snapshot object and clear the output file.
        self.output_file = output_file
        # Clear file at start
        open(self.output_file, "w").close()

    def take_snapshot(self):
        """Create a single snapshot dict."""
        cpu = psutil.cpu_times_percent()
        snapshot = {
            "Tasks": {
                "total": len(psutil.pids()),
                "running": len([p for p in psutil.process_iter(attrs=['status']) if p.info['status'] == psutil.STATUS_RUNNING]),
                "sleeping": len([p for p in psutil.process_iter(attrs=['status']) if p.info['status'] == psutil.STATUS_SLEEPING]),
                "stopped": len([p for p in psutil.process_iter(attrs=['status']) if p.info['status'] == psutil.STATUS_STOPPED]),
                "zombie": len([p for p in psutil.process_iter(attrs=['status']) if p.info['status'] == psutil.STATUS_ZOMBIE]),
            },
            "%CPU": {
                "user": cpu.user,
                "system": cpu.system,
                "idle": cpu.idle
            },
            "KiB Mem": {
                "total": psutil.virtual_memory().total // 1024,
                "free": psutil.virtual_memory().free // 1024,
                "used": psutil.virtual_memory().used // 1024,
            },
            "KiB Swap": {
                "total": psutil.swap_memory().total // 1024,
                "free": psutil.swap_memory().free // 1024,
                "used": psutil.swap_memory().used // 1024,
            },
            "Timestamp": int(time.time())
        }
        return snapshot

    def save_snapshot(self, snapshot):
        """Write snapshot to file and console."""
        with open(self.output_file, "a") as f:
            json.dump(snapshot, f)
            f.write("\n")
        os.system("clear")
        print(snapshot, end="\r")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", help="Interval between snapshots in seconds", type=int, default=30)
    parser.add_argument("-f", help="Output file name", default="snapshot.json")
    parser.add_argument("-n", help="Quantity of snapshot to output", type=int, default=20)
    args = parser.parse_args()

    snapshot_tool = Snapshot(output_file=args.f)
    for _ in range(args.n):
        snap = snapshot_tool.take_snapshot()
        snapshot_tool.save_snapshot(snap)
        time.sleep(args.i)


if __name__ == "__main__":
    main()
