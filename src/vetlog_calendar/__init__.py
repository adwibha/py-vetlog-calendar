#  Copyright 2026 Jose Morales contact@josdem.io
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

from importlib.metadata import PackageNotFoundError, version
from pathlib import Path
import tomllib


# Get project info from pyproject.toml
__project__ = "vetlog-calendar"


def _read_version() -> str:
    try:
        return version("py-vetlog-calendar")
    except PackageNotFoundError:
        pyproject_path = Path(__file__).resolve().parents[2] / "pyproject.toml"
        with pyproject_path.open("rb") as pyproject_file:
            return tomllib.load(pyproject_file)["project"]["version"]


__version__ = _read_version()
