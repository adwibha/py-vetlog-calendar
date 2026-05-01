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

import os

import pytest
from unittest.mock import MagicMock, patch

from vetlog_calendar.pets.model import Pet
from vetlog_calendar.shared.calendar_helper import Helper
from vetlog_calendar.users.model import User
from vetlog_calendar.vaccinations.model import Vaccination

from pydantic import ValidationError
from vetlog_calendar.shared.config import Settings


@pytest.fixture
def clean_env():
    with patch.dict(os.environ, {}, clear=True):
        yield


@pytest.fixture
def pet():
    return Pet(id=1, name="Sora", user_id=7)


@pytest.fixture
def owner():
    return User(
        id=7,
        username="josdem",
        first_name="Jose",
        last_name="Morales",
        mobile="1234567890",
        email="contact@josdem.io",
    )


@pytest.fixture
def vaccination():
    return Vaccination(id=1, pet_id=1, name="C6CV", date="2026-05-21", status="NEW")


def test_get_event_description(pet, vaccination, owner):
    mock_settings = MagicMock()
    mock_settings.DEFAULT_EMAILS = [
        "email1@example.com",
        "email2@example.com",
        "email3@example.com",
    ]
    with patch(
        "vetlog_calendar.shared.calendar_helper.get_settings",
        return_value=mock_settings,
    ):
        helper = Helper(pet=pet, vaccination=vaccination, owner=owner, language="en")
        expected_description = {
            "summary": "Jose - Vaccination appointment for Sora",
            "location": "Whatever works for you",
            "description": """Jose Morales\n1234567890\n\nVaccination appointment for Sora\n\nThank you for trusting Vetlog!\nhttps://vetlog.org/""",
            "start": {
                "dateTime": "2026-05-21T11:00:00-06:00",
                "timeZone": "UTC",
            },
            "end": {
                "dateTime": "2026-05-21T11:15:00-06:00",
                "timeZone": "UTC",
            },
            "attendees": [
                {"email": "contact@josdem.io"},
                {"email": "email1@example.com"},
                {"email": "email2@example.com"},
                {"email": "email3@example.com"},
            ],
        }
        assert helper.get_event() == expected_description


def test_settings_missing_required_vars(clean_env):
    with pytest.raises(ValidationError):
        Settings(_env_file=None)
