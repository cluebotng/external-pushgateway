#!/usr/bin/env python3
import os
import subprocess
from pathlib import PosixPath


TARGET_RELEASE = "1.11.1"
WORKSPACE_DIR = PosixPath("/workspace")


def install_package():
    subprocess.run(
        [
            "curl",
            "--silent",
            "--show-error",
            "--fail",
            "-L",
            "-o",
            f"/tmp/pushgateway-{TARGET_RELEASE}.linux-amd64.tar.gz",
            f"https://github.com/prometheus/pushgateway/releases/download/v{TARGET_RELEASE}/"
            f"pushgateway-{TARGET_RELEASE}.linux-amd64.tar.gz",
        ],
        check=True,
    )
    subprocess.run(
        [
            "tar",
            "-C",
            WORKSPACE_DIR.as_posix(),
            "-xf",
            f"/tmp/pushgateway-{TARGET_RELEASE}.linux-amd64.tar.gz",
            "--strip-components=1",
            f"pushgateway-{TARGET_RELEASE}.linux-amd64/pushgateway",
        ],
        check=True,
    )
    os.remove(f"/tmp/pushgateway-{TARGET_RELEASE}.linux-amd64.tar.gz")


def appease_poetry():
    # Poetry expects a Python package from `setup.py install`, create a minimal one
    package_dir = PosixPath("/workspace/external_pushgateway")
    package_dir.mkdir(parents=True)
    (package_dir / "__init__.py").open("w").close()


def main():
    install_package()
    appease_poetry()


if __name__ == "__main__":
    main()
