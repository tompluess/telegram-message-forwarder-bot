from pyrogram.types import (
    InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup)


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

    if message.from_user.username:
        buttons.append(InlineKeyboardButton(
            f"PN {sender_name}", url=f"https://t.me/{message.from_user.username}"))

    return [buttons]


def username_long(user):
    sender_name_parts = []
    if user.first_name:
        sender_name_parts.append(user.first_name)
    if user.last_name:
        sender_name_parts.append(user.last_name)
    if user.username:
        sender_name_parts.append("@"+user.username)
    sender_name = " ".join(sender_name_parts)
    return sender_name
