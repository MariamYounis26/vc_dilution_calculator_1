# vc_dilution_calculator/repository/session_repository.py
class SessionRepository:
    """Repository to manage session data."""

    def __init__(self):
        self._session_data = {}

    def save(self, key: str, value: dict) -> None:
        self._session_data[key] = value

    def load(self, key: str) -> dict:
        return self._session_data.get(key)

