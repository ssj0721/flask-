from src import mail
from flask_mail import Message
from threading import Thread
from flask import copy_current_request_context

# 通用服务类
class CommentService:

    # 发送验证码邮件
    @staticmethod
    def sendVirCodeMail(to: str, code: str) -> bool:
        # 构造邮件
        msg = Message(
            subject="GCOJ 验证码",
            recipients=[to],  # 收件人
            html=f"""           
            <!DOCTYPE html>
                <html lang="zh-CN">
                <head>
                    <meta charset="UTF-8">
                    <title>验证码</title>
                    <style>
                        * {{
                            margin: 0;
                            padding: 0;
                            box-sizing: border-box;
                        }}
                        body {{
                            font-family: "Microsoft YaHei", Arial, sans-serif;
                            background-color: #f5f7fa;
                            padding: 20px;
                        }}
                        .card {{
                            max-width: 480px;
                            margin: 0 auto;
                            background: #ffffff;
                            padding: 40px 30px;
                            border-radius: 12px;
                            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.05);
                            text-align: center;
                        }}
                        .title {{
                            font-size: 22px;
                            color: #333;
                            margin-bottom: 20px;
                        }}
                        .desc {{
                            font-size: 15px;
                            color: #666;
                            margin-bottom: 30px;
                        }}
                        .code {{
                            display: inline-block;
                            font-size: 32px;
                            font-weight: bold;
                            color: #16d0ff;
                            letter-spacing: 6px;
                            background: #e8f6ff;
                            padding: 12px 24px;
                            border-radius: 8px;
                            margin-bottom: 30px;
                        }}
                        .tip {{
                            font-size: 13px;
                            color: #999;
                            line-height: 1.6;
                        }}
                        .footer {{
                            margin-top: 40px;
                            font-size: 12px;
                            color: #ccc;
                        }}
                    </style>
                </head>
                <body>
                    <div class="card">
                        <div class="title">欢迎注册【GCOJ】！！!</div>
                        <div class="desc">您的验证码是：</div>
                        <div class="code">{code}</div>
                        <div class="tip">请在5分钟内完成验证<br>
                            如非本人操作，请忽略此邮件<br>
                            请勿向他人泄露验证码
                        </div>
                        <div class="footer">系统自动发送 · 无需回复</div>
                    </div>
                </body>
                </html>
            """
        )  # 邮件内容

        @copy_current_request_context
        def send_async_mail(msg):  # 获取上下文
            mail.send(msg)

        Thread(target=send_async_mail, args=(msg,)).start()

        return True
