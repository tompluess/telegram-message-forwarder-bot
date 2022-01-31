import logging
from datetime import datetime, timedelta

LOG = logging.getLogger(__name__)


def get_invite_link(chat_id, app):
    expire_date = datetime.now() + timedelta(days=7)
    try:
        invite_link = app.create_chat_invite_link(
            chat_id, name="Message Forwarder Bot", creates_join_request=True, expire_date=int(expire_date.timestamp()))
    except Exception as e:
        LOG.info(e)
        return None
    return invite_link.invite_link
