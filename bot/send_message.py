import os
import random
from time import sleep
from pyrogram import filters
from pyrogram.types import (
    InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup)
from bot import LOG
from bot.helper.utils import get_formatted_chat
from bot.helper.user import username_long
from bot.helper.button import compose_buttons
from bot.helper.invite_links import get_invite_link


def send_message(message, chat_id, app):

    sender_name = username_long(message.from_user)

    LOG.info(
        f"Send message from: {sender_name} / {message.chat.title} to chat: {chat_id} ")
    LOG.debug(f"Send message: {message}")

    invite_link = get_invite_link(message.chat.id, app)
    buttons = compose_buttons(message, invite_link)

    return app.copy_message(
        chat_id, message.chat.id, message.message_id,
        reply_markup=InlineKeyboardMarkup(buttons))
