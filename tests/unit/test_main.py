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

from unittest.mock import MagicMock, patch
from datetime import datetime

from vetlog_calendar import main
from vetlog_calendar.pets.model import Pet
from vetlog_calendar.users.model import User
from vetlog_calendar.vaccinations.model import Vaccination


def test_list_users_prints_user_details(capsys):
    """List all users prints expected user details"""
    user = User(
        username="josdem",
        email="contact@josdem.io",
        mobile="1234567890",
        role="USER",
    )

    mock_session_cm = MagicMock()
    mock_session_cm.__enter__ = MagicMock(return_value=MagicMock())
    mock_session_cm.__exit__ = MagicMock(return_value=False)

    with (
        patch("vetlog_calendar.main.get_session", return_value=mock_session_cm),
        patch("vetlog_calendar.main.UserService.get_all", return_value=[user]),
    ):
        main.list_users()

    captured = capsys.readouterr()
    assert "user: josdem" in captured.out
    assert "email: contact@josdem.io" in captured.out
    assert "mobile: 1234567890" in captured.out
    assert "role: USER" in captured.out


def test_list_vaccinations_handles_missing_pet(capsys):
    """List pending vaccinations keeps running when pet is missing"""
    vaccination = Vaccination(
        pet_id=999,
        name="Rabies",
        date=datetime(2026, 1, 1, 0, 0, 0),
    )

    mock_session_cm = MagicMock()
    mock_session_cm.__enter__ = MagicMock(return_value=MagicMock())
    mock_session_cm.__exit__ = MagicMock(return_value=False)

    with (
        patch("vetlog_calendar.main.get_session", return_value=mock_session_cm),
        patch(
            "vetlog_calendar.main.VaccinationService.get_pending_vaccinations",
            return_value=[vaccination],
        ),
        patch("vetlog_calendar.main.PetRepository.find_by_id", return_value=None),
    ):
        main.list_vaccinations()

    captured = capsys.readouterr()
    assert "vaccination: Rabies" in captured.out
    assert "pet: unknown" in captured.out
    assert "notify to: unknown" in captured.out


def test_list_vaccinations_handles_missing_user(capsys):
    """List pending vaccinations keeps running when user is missing"""
    vaccination = Vaccination(
        pet_id=1,
        name="Rabies",
        date=datetime(2026, 1, 1, 0, 0, 0),
    )
    pet = Pet(
        id=1,
        user_id=999,
        name="Sora",
        birth_date=datetime(2020, 1, 1, 0, 0, 0),
        breed_id=1,
        status="ACTIVE",
        uuid="pet-uuid",
    )

    mock_session_cm = MagicMock()
    mock_session_cm.__enter__ = MagicMock(return_value=MagicMock())
    mock_session_cm.__exit__ = MagicMock(return_value=False)

    with (
        patch("vetlog_calendar.main.get_session", return_value=mock_session_cm),
        patch(
            "vetlog_calendar.main.VaccinationService.get_pending_vaccinations",
            return_value=[vaccination],
        ),
        patch("vetlog_calendar.main.PetRepository.find_by_id", return_value=pet),
        patch("vetlog_calendar.main.UserRepository.find_by_id", return_value=None),
    ):
        main.list_vaccinations()

    captured = capsys.readouterr()
    assert "vaccination: Rabies" in captured.out
    assert "pet: Sora" in captured.out
    assert "notify to: unknown" in captured.out
