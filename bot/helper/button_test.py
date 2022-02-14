from pyrogram.types import (
    InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup)
from message import compose_buttons
from pyrogram.types import (User, Message, Chat)


def test_compose_buttons_with_username_and_invitelink():
    chattitle = "Chat Title"
    invite_link = "https://test.example/url"
    user = User(id=0)
    user.first_name = "Max"
    user.username = "maxmuster"
    chat = Chat(id=100, type="Text", title=chattitle)
    message = Message(message_id=1, chat=chat, from_user=user)
    # act
    buttons = compose_buttons(message, invite_link=invite_link)
    # assert
    assert buttons == [[InlineKeyboardButton(f"💌 Max", url="https://t.me/c/100/1"),
                        InlineKeyboardButton(f"{chattitle}", url=invite_link)]]


def test_compose_buttons_with_username_without_invitelink():
    chattitle = "Chat Title"
    user = User(id=0)
    user.first_name = "Max"
    user.username = "maxmuster"
    chat = Chat(id=100, type="Text", title=chattitle)
    message = Message(message_id=1, chat=chat, from_user=user)
    # act
    buttons = compose_buttons(message)
    # assert
    expected_username = "Max"
    assert buttons == [[InlineKeyboardButton(f"💌 Max", url="https://t.me/c/100/1"),
                        InlineKeyboardButton(f"PN @maxmuster", url=f"https://t.me/maxmuster")]]


def test_compose_buttons_without_username():
    chattitle = "Chat Title"
    invite_link = "https://test.example/url"
    user = User(id=0)
    user.first_name = "Max"
    user.last_name = "Last"
    chat = Chat(id=100, type="Text", title=chattitle)
    message = Message(message_id=1, chat=chat, from_user=user)
    # act
    buttons = compose_buttons(message, invite_link=invite_link)
    assert buttons == [[
        InlineKeyboardButton(
            f"💌 Max Last", url="https://t.me/c/100/1"),
        InlineKeyboardButton(f"{chattitle}", url=invite_link)]]


def test_compose_buttons_without_invitelink():
    chattitle = "Chat Title"
    user = User(id=0)
    user.first_name = "Max"
    chat = Chat(id=100, type="Text", title=chattitle)
    message = Message(message_id=1, chat=chat, from_user=user)
    # act
    buttons = compose_buttons(message)
    assert buttons == [[InlineKeyboardButton(
        f"💌 Max", url="https://t.me/c/100/1")]]
