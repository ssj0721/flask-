from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError


class Argon2Util:
    _ph = PasswordHasher(
        memory_cost=65536,
        time_cost=4,
        parallelism=2
    )

    # 用于加密，返回加密后的密码
    @staticmethod
    def encrypt_password(raw_password: str) -> str:
        if not raw_password:
            raise ValueError("密码不能为空")
        return Argon2Util._ph.hash(raw_password)

    # 用于验证,参数：加密后密码，原始密码
    @staticmethod
    def verify_password(stored_hash: str, raw_password: str) -> bool:
        try:
            Argon2Util._ph.verify(stored_hash, raw_password)
            return True
        except VerifyMismatchError:
            return False
