from typing import Dict, Optional, Tuple, Any


class JwtUtil:

    @staticmethod
    def create_tokens(user_id: int, role: str) -> Dict[str, str]:
        pass

    @staticmethod
    def parse_token(token: str) -> Optional[Dict[str, Any]]:
        pass

    @staticmethod
    def refresh_access_token(refresh_token: str) -> Tuple[bool, str]:
        pass

    @staticmethod
    def get_current_user_id() -> int:
        pass

    @staticmethod
    def get_current_user_role() -> str:
        pass