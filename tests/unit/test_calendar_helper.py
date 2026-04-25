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

from vetlog_calendar.pets.model import Pet
from vetlog_calendar.shared.calendar_helper import Helper
from vetlog_calendar.users.model import User
from vetlog_calendar.vaccinations.model import Vaccination


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
    return Vaccination(id=1, pet_id=1, name="C6CV", date="2026-04-21", status="NEW")


def test_get_event_description(pet, vaccination, owner):
    helper = Helper(pet=pet, vaccination=vaccination, owner=owner)
    expected_description = {
        "summary": "Jose - Vaccination appointment for Sora",
        "location": "Online",
        "description": """Jose Morales\n1234567890\n\nVaccination appointment for Sora\n\nThank you for trusting Vetlog!\nhttps://vetlog.org/""",
        "start": {
            "dateTime": "2026-04-21T11:00:00Z",
            "timeZone": "CST",
        },
        "end": {
            "dateTime": "2026-04-21T11:15:00Z",
            "timeZone": "CST",
        },
        "attendees": [
            {"email": "contact@josdem.io"},
        ],
    }
    assert helper.get_event_description() == expected_description
