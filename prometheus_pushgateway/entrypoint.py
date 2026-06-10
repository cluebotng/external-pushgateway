#!/usr/bin/env python3
import os
import sys
from pathlib import PosixPath


def main():
    # Note: We replace the current process, rather than running as a subprocess,
    #      so `alloy` is essentially being run from the launcher.
    binary_path = PosixPath(__file__).parent / "pushgateway"
    if not binary_path.is_file():
        print("Missing binary!")
        sys.exit(2)

    arguments = ["--web.listen-address=0.0.0.0:9091"]
    if tool_data_dir := os.environ.get("TOOL_DATA_DIR"):
        home_dir = PosixPath(tool_data_dir)
        if home_dir.exists():
            path = home_dir / "persistent-data" / "pushgateway"
            if not path.parent.is_dir():
                path.parent.mkdir(parents=True, exist_ok=True)
            arguments.append(f"--persistence.file={path.as_posix()}")

    return os.execv(binary_path.as_posix(), [binary_path.as_posix()] + arguments)


if __name__ == "__main__":
    main()
