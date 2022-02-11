import logging
from os import environ
from pyrogram.types import (Message, Photo,
    InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup)
from cachetools import TTLCache

LOG = logging.getLogger(__name__)
LOG.setLevel(environ.get("LOG_LEVEL", "INFO").upper())

deduplicate_messages_cache_hours = int(
    environ.get("MESSAGES_CACHE_HOURS", "72"))
deduplicate_messages_cache = TTLCache(
    maxsize=99, ttl=deduplicate_messages_cache_hours*3600)


def send_message(message, chat_id, app, invite_link=None):

    message_info = ForwardedMessageInfo(message, chat_id)
    LOG.debug(f"try to send message with forward_id {message_info.forward_id()}")
    try:
        message_info_from_cache = deduplicate_messages_cache[message_info.forward_id()]
        LOG.info(f"message info from cache: {message_info_from_cache.forward_id()}, skip forwarding.")
        return None
    except KeyError:
        sent_message = do_send_message(message,chat_id, app, invite_link)
        message_info.target_message_id = sent_message.message_id
        message_info.text=sent_message.text or sent_message.caption
        LOG.warning(f"add to cache message with forward_id {message_info.forward_id()}")
        deduplicate_messages_cache[message_info.forward_id()] = message_info
        return sent_message


def do_send_message(message, chat_id, app, invite_link=None):

    sender_name = username_long(message.from_user)

    LOG.info(
        f"Send message from: {sender_name} / {message.chat.title} (invite link: {invite_link}) to chat: {chat_id} ")
    LOG.debug(f"Send message: {message}")

    buttons = compose_buttons(message, invite_link)

    return app.copy_message(
        chat_id, message.chat.id, message.message_id,
        reply_markup=InlineKeyboardMarkup(buttons))


def compose_buttons(message, invite_link=None):

    from_chat = str(message.chat.id).replace("-100", "")
    message_link = f"https://t.me/c/{from_chat}/{message.message_id}"
    sender_name = username_long(message.from_user)

    buttons = []
    buttons.append(InlineKeyboardButton(
        f"{sender_name} in {message.chat.title}", url=message_link))

    if invite_link:
        buttons.append(InlineKeyboardButton(
            f"Join {message.chat.title}", url=invite_link))
    elif message.from_user.username:
        buttons.append(InlineKeyboardButton(
            f"PN @{message.from_user.username}", url=f"https://t.me/{message.from_user.username}"))

    return [buttons]


def username_long(user):
    sender_name_parts = []
    if user.first_name:
        sender_name_parts.append(user.first_name)
    if user.last_name:
        sender_name_parts.append(user.last_name)
    sender_name = " ".join(sender_name_parts)
    return sender_name


def reset_messages_cache():
    LOG.warning("reset messages cache")
    deduplicate_messages_cache.clear()


class ForwardedMessageInfo:
    source_chat_id = None
    source_message_id = None
    target_chat_id = None
    target_message_id = None
    text = None

    def __init__(self, message: Message, target_chat_id):
        self.source_chat_id = message.chat.id
        self.source_message_id = message.message_id
        self.target_chat_id = target_chat_id

    def forward_id(self):
        return f"{self.source_chat_id}_{self.source_message_id}_{self.target_chat_id}"
