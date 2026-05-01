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


from vetlog_calendar.shared.date_helper import validate_date


def test_move_two_days_if_monday():
    date_str = "2026-06-01"  # Monday
    expected = "2026-06-03"  # Wednesday
    assert validate_date(date_str) == expected


def test_move_two_days_if_tuesday():
    date_str = "2026-06-02"  # Tuesday
    expected = "2026-06-04"  # Thursday
    assert validate_date(date_str) == expected


def test_no_move_if_wednesday():
    date_str = "2026-06-03"  # Wednesday
    expected = "2026-06-03"  # Wednesday
    assert validate_date(date_str) == expected


def test_no_move_if_thursday():
    date_str = "2026-06-04"  # Thursday
    expected = "2026-06-04"  # Thursday
    assert validate_date(date_str) == expected


def test_no_move_if_friday():
    date_str = "2026-06-05"  # Friday
    expected = "2026-06-05"  # Friday
    assert validate_date(date_str) == expected


def test_no_move_if_saturday():
    date_str = "2026-06-06"  # Saturday
    expected = "2026-06-06"  # Saturday
    assert validate_date(date_str) == expected


def test_no_move_if_sunday():
    date_str = "2026-06-07"  # Sunday
    expected = "2026-06-07"  # Sunday
    assert validate_date(date_str) == expected
