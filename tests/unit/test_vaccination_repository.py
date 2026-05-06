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
#  limitations under the License

from datetime import datetime, timedelta
from unittest.mock import MagicMock

from sqlmodel import Session

from vetlog_calendar.vaccinations.model import Vaccination
from vetlog_calendar.vaccinations.repository import VaccinationRepository


def test_find_pending_dewormings():
    session = MagicMock(spec=Session)
    repository = VaccinationRepository(session)

    # Create a vaccination with status "APPLIED" and date 7 months ago
    vaccination = Vaccination(
        id=1,
        name="Deworming",
        date=datetime.now() - timedelta(days=30 * 7),
        status="APPLIED",
    )
    session.exec.return_value.all.return_value = [vaccination]
    pending_dewormings = repository.find_pending_dewormings()
    assert len(pending_dewormings) == 1
    assert pending_dewormings[0].id == vaccination.id
    assert pending_dewormings[0].status == "APPLIED"
