import os
import pytest
from unittest.mock import patch
from vetlog_calendar.shared.config import Settings


@pytest.fixture
def mock_env_vars():
    with patch.dict(
        os.environ,
        {
            "TOKEN_PATH": "token_path_value/token.json",
            "CREDENTIALS_PATH": "token_path_value/credentials.json",
        },
    ):
        yield


def test_settings_loads_from_env(mock_env_vars):
    settings = Settings()
    assert settings.TOKEN_PATH == "token_path_value/token.json"
    assert settings.CREDENTIALS_PATH == "token_path_value/credentials.json"
