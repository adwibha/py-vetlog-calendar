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


def owner():
    return User(
        id=1,
        username="josdem",
        first_name="Jose",
        last_name="Morales",
        email="contact@josdem.io",
        mobile="1234567890",
        role="USER",
    )


def test_list_users_prints_user_details(capsys):
    """List all users prints expected user details"""

    mock_session_cm = MagicMock()

    with (
        patch("vetlog_calendar.main.get_session", return_value=mock_session_cm),
        patch("vetlog_calendar.main.UserService.get_all", return_value=[owner()]),
    ):
        main.list_users()

    captured = capsys.readouterr()
    assert "user: josdem" in captured.out
    assert "email: contact@josdem.io" in captured.out
    assert "mobile: 1234567890" in captured.out
    assert "role: USER" in captured.out


def test_list_vaccinations(capsys):
    """List pending vaccinations"""
    vaccination = Vaccination(
        pet_id=1,
        name="Rabies",
        date=datetime(2026, 1, 1, 0, 0, 0),
    )

    pet = Pet(
        id=1,
        user_id=1,
        name="Sora",
        birth_date=datetime(2020, 1, 1, 0, 0, 0),
        breed_id=1,
    )

    mock_session_cm = MagicMock()

    with (
        patch("vetlog_calendar.main.get_session", return_value=mock_session_cm),
        patch(
            "vetlog_calendar.main.VaccinationService.get_pending_vaccinations",
            return_value=[vaccination],
        ),
        patch("vetlog_calendar.main.PetRepository.find_by_id", return_value=pet),
        patch("vetlog_calendar.main.UserRepository.find_by_id", return_value=owner()),
    ):
        main.list_vaccinations()

    captured = capsys.readouterr()
    assert (
        "Google calendar event title: Jose - Vaccination appointment for Sora"
        in captured.out
    )


def test_list_vaccinations_handles_pet_has_adopter(capsys):
    """List pending vaccinations"""
    vaccination = Vaccination(
        pet_id=1,
        name="Rabies",
        date=datetime(2026, 1, 1, 0, 0, 0),
    )
    pet = Pet(
        id=1,
        user_id=999,
        adopter_id=1,
        name="Sora",
        birth_date=datetime(2020, 1, 1, 0, 0, 0),
        breed_id=1,
        status="ADOPTED",
        uuid="pet-uuid",
    )

    mock_session_cm = MagicMock()

    with (
        patch("vetlog_calendar.main.get_session", return_value=mock_session_cm),
        patch(
            "vetlog_calendar.main.VaccinationService.get_pending_vaccinations",
            return_value=[vaccination],
        ),
        patch("vetlog_calendar.main.PetRepository.find_by_id", return_value=pet),
        patch(
            "vetlog_calendar.main.UserRepository.find_by_id", return_value=owner()
        ) as mock_find_user_by_id,
    ):
        main.list_vaccinations()

    mock_find_user_by_id.assert_called_with(pet.adopter_id)
    captured = capsys.readouterr()
    assert (
        "Google calendar event title: Jose - Vaccination appointment for Sora"
        in captured.out
    )
