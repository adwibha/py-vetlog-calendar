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

from vetlog_calendar.pets.model import Pet
from vetlog_calendar.pets.service import PetService


@pytest.fixture
def mock_repo():
    return MagicMock()


def test_get_pets(mock_repo):
    """Get all pets"""
    service = PetService(repository=mock_repo, vaccination_service=MagicMock())
    pets = []
    # Add logic to get all pets with pending vaccinations
    mock_repo.get_pets_with_pending_vaccinations.return_value = pets
    assert service.process_vaccinations() == pets
