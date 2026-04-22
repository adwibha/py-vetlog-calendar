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

from .shared.calendar_helper import Helper
from .shared.database import get_session
from .users.repository import UserRepository
from .users.service import UserService
from .pets.repository import PetRepository
from .pets.service import PetService
from .vaccinations.repository import VaccinationRepository
from .vaccinations.service import VaccinationService
from .calendar_reader import Reader
from .shared.config import Settings
from . import __project__, __version__


def list_events():
    """List events"""
    reader = Reader()
    reader.listing_events()


def print_paths():
    """Print paths"""
    settings = Settings()
    print(f"Token path: {settings.TOKEN_PATH}")
    print(f"Credentials path: {settings.CREDENTIALS_PATH}")


def list_users():
    """List all users"""
    with get_session() as session:
        repo = UserRepository(session)
        service = UserService(repo)
        users = service.get_all()
        for user in users:
            print(
                f"user: {user.username}, email: {user.email}, mobile: {user.mobile}, role: {user.role}"
            )


def list_pets():
    """List all pets"""
    with get_session() as session:
        repo = PetRepository(session)
        service = PetService(repo)
        pets = service.get_all()
        for pet in pets:
            print(
                f"pet: {pet.name}, birth date: {pet.birth_date}, going_out_often: {pet.going_out_often}"
            )


def list_vaccinations():
    """List pending vaccinations"""
    with get_session() as session:
        repo = VaccinationRepository(session)
        service = VaccinationService(repo)
        pet_repository = PetRepository(session)
        user_repository = UserRepository(session)
        vaccinations = service.get_pending_vaccinations()
        for vaccination in vaccinations:
            pet = pet_repository.find_by_id(vaccination.pet_id)

            user = (
                user_repository.find_by_id(pet.adopter_id)
                if pet.adopter_id is not None
                else user_repository.find_by_id(pet.user_id)
            )

            helper = Helper(pet=pet, owner=user)
            event_title = helper.get_event_title()
            print(f"Google calendar event title: {event_title}")


def version_check():
    """Print version info"""
    print(f"{__project__} version {__version__}")
