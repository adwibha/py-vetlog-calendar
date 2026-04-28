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

from vetlog_calendar.shared.locale import Locale


def test_return_spanish_title():
    """Test that the title is returned in Spanish"""
    locale = Locale(language="es")
    title = locale.get_event_title(owner="Jose", pet="Sora")
    assert title == "Jose - Cita de vacunación para Sora"


def test_return_english_title():
    """Test that the title is returned in English"""
    locale = Locale()
    title = locale.get_event_title(owner="Jose", pet="Sora")
    assert title == "Jose - Vaccination appointment for Sora"


def test_return_spanish_location():
    """Test that the location is returned in Spanish"""
    locale = Locale(language="es")
    location = locale.get_event_location()
    assert location == "La que mejor funcione para ambos"


def test_return_english_location():
    """Test that the location is returned in English"""
    locale = Locale()
    location = locale.get_event_location()
    assert location == "Whatever works for you"
