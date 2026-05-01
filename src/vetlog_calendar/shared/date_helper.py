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

from datetime import datetime, timedelta


def validate_date(date_str: str) -> str:
    """Validate if day of the week is valid"""
    date = datetime.strptime(date_str, "%Y-%m-%d")
    week_day = date.weekday()
    match week_day:
        case 0 | 1:
            new_date = date + timedelta(days=2)
            return new_date.strftime("%Y-%m-%d")
        case 2 | 3 | 4 | 5 | 6:
            return date_str
