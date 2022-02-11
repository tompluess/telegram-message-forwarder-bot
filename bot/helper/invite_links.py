import logging
from os import environ
from datetime import datetime, timedelta
from cachetools import TTLCache

LOG = logging.getLogger(__name__)
LOG.setLevel(environ.get("LOG_LEVEL", "INFO").upper())

invite_links_cache_hours=int(environ.get("INVITE_LINKS_CACHE_HOURS", "24"))
invite_links_cache = TTLCache(maxsize=99, ttl=invite_links_cache_hours*3600)


def get_invite_link(chat_id, app):
    try:
        invite_link_from_cache = invite_links_cache[chat_id]
        LOG.debug(f"using invite link from cache: {invite_link_from_cache}")
        return invite_link_from_cache
    except KeyError:
        new_invite_link = create_invite_link(chat_id, app)
        if new_invite_link:
            invite_links_cache[chat_id] = new_invite_link
        return new_invite_link


def create_invite_link(chat_id, app):
    try:
        expire_days = int(environ.get("INVITE_LINKS_EXPIRE_DAYS", "7"))
        now = datetime.now()
        expire_date = now + timedelta(days=expire_days)
        link_name = f"Used for {invite_links_cache_hours}h from {now}"
        LOG.debug(f"Link Name: {link_name}")

        invite_link = app.create_chat_invite_link(
            chat_id, name=link_name, creates_join_request=True, expire_date=int(expire_date.timestamp()))
        LOG.debug(f"got invite link for chat {chat_id}: {invite_link}")
        return invite_link.invite_link
    except Exception as e:
        LOG.info(e)
        return None


def reset_invite_links():
    LOG.warning("reset invite links")
    invite_links_cache.clear()
