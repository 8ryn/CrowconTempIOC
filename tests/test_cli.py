import subprocess
import sys

from CrowconTempIOC import __version__


def test_cli_version():
    cmd = [sys.executable, "-m", "CrowconTempIOC", "--version"]
    assert subprocess.check_output(cmd).decode().strip() == __version__
