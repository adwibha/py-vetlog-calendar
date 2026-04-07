from urllib.parse import quote_plus
from functools import lru_cache

from sqlmodel import Session, create_engine

from vetlog_calendar.shared.config import get_settings


@lru_cache
def get_database_url() -> str:
    settings = get_settings()
    return f"mysql+mysqlconnector://{quote_plus(settings.db_user)}:{quote_plus(settings.db_password)}@{settings.db_host}/{settings.db_name}"


@lru_cache
def get_engine():
    return create_engine(get_database_url(), echo=False, pool_pre_ping=True)


def get_session() -> Session:
    return Session(get_engine())
