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

from typing import Sequence
from datetime import datetime, timedelta
from sqlmodel import Session, select, update

from vetlog_calendar.vaccinations.model import Vaccination, VaccineType


class VaccinationRepository:
    def __init__(self, session: Session):
        self.session = session

    def find_pending_vaccinations(self, type: VaccineType) -> Sequence[Vaccination]:
        stmt = select(Vaccination).where(
            (Vaccination.status == "NEW") & (Vaccination.name == type)
        )
        return self.session.exec(stmt).all()

    def find_pending_dewormings(self, months: int) -> Sequence[Vaccination]:
        stmt = select(Vaccination).where(
            (Vaccination.status == "APPLIED")
            & (Vaccination.name == VaccineType.DEWORMING)
            & (Vaccination.date <= datetime.now() - timedelta(days=30 * months))
        )
        return self.session.exec(stmt).all()

    def update_vaccination_status(self, vaccination: Vaccination):
        stmt = (
            update(Vaccination)
            .where(Vaccination.id == vaccination.id)
            .values(status="PENDING")
        )
        self.session.exec(stmt)
        self.session.commit()
