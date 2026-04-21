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


@pytest.fixture
def pet():
    return Pet(id=1, name="Sora", owner_id=7)


@pytest.fixture
def owner():
    return User(id=7, first_name="josdem")


def test_get_event_title(pet, owner):
    helper = Helper(pet=pet, owner=owner)
    expected_title = "josdem - Vaccination appointment for Sora"
    assert helper.get_event_title() == expected_title
