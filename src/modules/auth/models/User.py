from datetime import datetime
from src.extensions import db



class UserDB(db.Model):
    __tablename__ = 'user'
    __table_args__ = {
        'mysql_engine': 'InnoDB',
        'mysql_charset': 'utf8mb4',
        'comment': '用户表'
    }

    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True, comment='主键ID')
    name = db.Column(db.String(50), nullable=False, unique=True, comment='用户名')
    nick = db.Column(db.String(50), nullable=True, comment='昵称')
    avatar_url = db.Column(db.String(255), default='', nullable=False, comment='头像地址')
    email = db.Column(db.String(80), nullable=False, comment='邮箱')
    password = db.Column(db.String(512), nullable=False, comment='密码')
    description = db.Column(db.Text, nullable=True, comment='个人描述')
    refresh_token = db.Column(db.String(512), nullable=True, comment='刷新令牌')
    create_time = db.Column(db.DateTime, nullable=False, default=datetime.now(), comment='创建时间')
    update_time = db.Column(db.DateTime, nullable=False, default=datetime.now(), onupdate=datetime.now(), comment='更新时间')
    is_delete = db.Column(db.SmallInteger, nullable=False, default=0, comment='是否删除 0-否 1-是')

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "nick": self.nick,
            "avatar_url": self.avatar_url,
            "email": self.email,
            "description": self.description,
            "create_time": self.create_time.strftime("%Y-%m-%d %H:%M:%S"),
            "update_time": self.update_time.strftime("%Y-%m-%d %H:%M:%S")
        }