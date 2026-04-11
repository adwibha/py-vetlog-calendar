from vetlog_calendar.users.repository import UserRepository


class UserService:
    def __init__(self, repo: UserRepository) -> None:
        self.repo = repo

    def get_all(self, user) -> bool:
        """Return all users"""
        return False
