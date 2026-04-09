import tomllib
from importlib.metadata import PackageNotFoundError
from pathlib import Path

from vetlog_calendar import __version__, _read_version
from vetlog_calendar.main import version_check


def test_package_version_matches_pyproject():
    pyproject_path = Path(__file__).resolve().parents[2] / "pyproject.toml"
    with pyproject_path.open("rb") as pyproject_file:
        expected_version = tomllib.load(pyproject_file)["project"]["version"]

    assert __version__ == expected_version


def test_read_version_falls_back_to_pyproject_when_package_metadata_is_missing(monkeypatch):
    monkeypatch.setattr("vetlog_calendar.version", lambda _: (_ for _ in ()).throw(PackageNotFoundError()))

    pyproject_path = Path(__file__).resolve().parents[2] / "pyproject.toml"
    with pyproject_path.open("rb") as pyproject_file:
        expected_version = tomllib.load(pyproject_file)["project"]["version"]

    assert _read_version() == expected_version


def test_version_check_uses_pyproject_version(capsys):
    version_check()

    assert capsys.readouterr().out.strip() == f"vetlog-calendar version {__version__}"
