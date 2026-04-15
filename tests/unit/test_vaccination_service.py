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

import pytest

from unittest.mock import MagicMock

from vetlog_calendar.vaccinations.model import Vaccination
from vetlog_calendar.vaccinations.service import VaccinationService


@pytest.fixture
def mock_repo():
    return MagicMock()


def test_get_vaccinations(mock_repo):
    """Get all vaccinations"""
    service = VaccinationService(repository=mock_repo)
    vaccinations = [Vaccination(id=1, name="Rabies")]
    mock_repo.get_all.return_value = vaccinations
    assert service.get_all() == vaccinations
