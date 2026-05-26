from datetime import datetime
from src.extensions import db

class RoleDB(db.Model):
    __tablename__ = 'role'

    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True, comment='角色ID')
    role = db.Column(db.String(50), nullable=False, unique=True, comment='角色名称')
    is_delete = db.Column(db.SmallInteger, nullable=False, default=0, comment='是否删除 0-否 1-是')

    def to_dict(self):
        return {
            "id": self.id,
            "role": self.role
        }


class UserRoleDB(db.Model):
    __tablename__ = 'user_role'

    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True, comment='关联ID，主键')
    user_id = db.Column(db.BigInteger, nullable=False, comment='用户ID')
    role_id = db.Column(db.BigInteger, nullable=False, comment='角色ID')
    is_delete = db.Column(db.SmallInteger, nullable=False, default=0, comment='是否删除 0-否 1-是')

    __table_args__ = (
        db.UniqueConstraint('user_id', 'role_id', name='uk_user_role'),
    )

    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "role_id": self.role_id,
        }

