import tomllib
from pathlib import Path

from vetlog_calendar import __version__
from vetlog_calendar.main import version_check


def test_package_version_matches_pyproject():
    pyproject_path = Path(__file__).resolve().parents[2] / "pyproject.toml"
    with pyproject_path.open("rb") as pyproject_file:
        expected_version = tomllib.load(pyproject_file)["project"]["version"]

    assert __version__ == expected_version


def test_version_check_uses_pyproject_version(capsys):
    version_check()

    assert capsys.readouterr().out.strip() == f"vetlog-calendar version {__version__}"
