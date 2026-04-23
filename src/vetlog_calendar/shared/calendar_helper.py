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

from vetlog_calendar.pets.model import Pet
from vetlog_calendar.users.model import User


class Helper:
    def __init__(self, pet: Pet, owner: User | None):
        self.pet = pet
        self.owner = owner

    def get_event_title(self) -> str:
        if self.owner is None:
            return f"Vaccination appointment for {self.pet.name}"
        owner_name = self.owner.first_name or self.owner.username
        return f"{owner_name} - Vaccination appointment for {self.pet.name}"

    def get_event_description(self) -> str:
        owner_info = (
            f"{self.owner.first_name} {self.owner.last_name}\n{self.owner.mobile}\n"
        )
        pet_info = f"Vaccination appointment for {self.pet.name}\n"
        thank_you_info = "Thank you for trusting Vetlog!"
        website_info = "https://vetlog.org/"
        return f"{owner_info}\n{pet_info}\n{thank_you_info}\n{website_info}"
