from pyrogram.types import (
    InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup)
from user import username_long


def compose_buttons(message):

    from_chat = str(message.chat.id).replace("-100", "")
    message_link = f"https://t.me/c/{from_chat}/{message.message_id}"
    sender_name = username_long(message.from_user)

    if message.from_user.username:
        buttons = [InlineKeyboardButton(f"{message.chat.title}", url=message_link),
                   InlineKeyboardButton(f"PN {sender_name}", url=f"https://t.me/{message.from_user.username}")]
    else:
        buttons = [InlineKeyboardButton(
            f"{sender_name} in {message.chat.title}", url=message_link)]

    return [buttons]