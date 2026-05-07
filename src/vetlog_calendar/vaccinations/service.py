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

from vetlog_calendar.vaccinations.model import Vaccination
from vetlog_calendar.vaccinations.repository import VaccinationRepository


class VaccinationService:
    def __init__(self, repository: VaccinationRepository):
        self.repository = repository

    def get_pending_vaccinations(self):
        """Return pending vaccinations"""
        return self.repository.find_pending_vaccinations()

    def get_pending_dewormings(self, months: int):
        """Return pending dewormings"""
        return self.repository.find_pending_dewormings(months)

    def get_possible_dewormings(self):
        """Return possible dewormings for outdoor pets"""
        return self.repository.find_pending_dewormings(6)

    def update_vaccination_status(self, vaccination: Vaccination) -> None:
        """Update vaccination status to PENDING"""
        self.repository.update_vaccination_status(vaccination)
