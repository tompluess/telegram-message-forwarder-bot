from datetime import datetime, timedelta


def get_invite_link(chat_id, app):
    expire_date = datetime.now() + timedelta(days=1)
    invite_link = app.create_chat_invite_link(
        chat_id, name="Test Phase", expire_date=expire_date)
    return invite_link
