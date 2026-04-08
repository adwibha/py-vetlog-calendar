import os
from pydantic_core import ValidationError
import pytest
from unittest.mock import patch
from vetlog_calendar.shared.config import Settings


@pytest.fixture
def mock_env_vars():
    with patch.dict(
        os.environ,
        {
            "DB_HOST": "localhost",
            "DB_NAME": "vetlog",
            "DB_USER": "vetlogUser",
            "DB_PASSWORD": "vetlogDB",
            "TOKEN_PATH": "token_path_value/token.json",
            "CREDENTIALS_PATH": "token_path_value/credentials.json",
        },
    ):
        yield


@pytest.fixture
def clean_env():
    with patch.dict(os.environ, {}, clear=True):
        yield


def test_settings_loads_from_env(mock_env_vars):
    settings = Settings()
    assert settings.db_host == "localhost"
    assert settings.db_name == "vetlog"
    assert settings.db_user == "vetlogUser"
    assert settings.db_password == "vetlogDB"
    assert settings.TOKEN_PATH == "token_path_value/token.json"
    assert settings.CREDENTIALS_PATH == "token_path_value/credentials.json"


def test_settings_missing_required_vars(clean_env):
    with pytest.raises(ValidationError):
        Settings(_env_file=None)
