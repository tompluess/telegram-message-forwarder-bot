import logging
from os import environ
from datetime import datetime, timedelta

LOG = logging.getLogger(__name__)
LOG.setLevel(environ.get("LOG_LEVEL", "INFO").upper())


def get_invite_link(chat_id, app):
    try:
        expire_days = int(environ.get("INVITE_LINKS_EXPIRE_DAYS", "7"))
        now = datetime.now()
        expire_date = now + timedelta(days=expire_days)
        link_name = f"Message Forwarder Bot {now}"
        LOG.debug(f"Link Name: {link_name}")

        invite_link = app.create_chat_invite_link(
            chat_id, name=link_name, creates_join_request=True, expire_date=int(expire_date.timestamp()))
        LOG.debug(f"got invite link for chat {chat_id}: {invite_link}")
        return invite_link.invite_link
    except Exception as e:
        LOG.info(e)
        return None
