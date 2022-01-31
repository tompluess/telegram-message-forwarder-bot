from pyrogram.types import (
    InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup)
from message import compose_buttons
from pyrogram.types import (User, Message, Chat)


def test_compose_buttons_with_username_and_invitelink():
    chattitle = "Chat Title"
    invite_link = "https://test.example/url"
    user = User(id=0)
    user.first_name = "First"
    user.username = "maxmuster"
    chat = Chat(id=100, type="Text", title=chattitle)
    message = Message(message_id=1, chat=chat, from_user=user)
    # act
    buttons = compose_buttons(message, invite_link=invite_link)
    # assert
    expected_username = "First @maxmuster"
    assert buttons == [[InlineKeyboardButton(f"{expected_username} in {chattitle}", url="https://t.me/c/100/1"),
                        InlineKeyboardButton(
                            f"Join {chattitle}", url=invite_link)]]


def test_compose_buttons_with_username_without_invitelink():
    chattitle = "Chat Title"
    user = User(id=0)
    user.first_name = "First"
    user.username = "maxmuster"
    chat = Chat(id=100, type="Text", title=chattitle)
    message = Message(message_id=1, chat=chat, from_user=user)
    # act
    buttons = compose_buttons(message)
    # assert
    expected_username = "First @maxmuster"
    assert buttons == [[InlineKeyboardButton(f"{expected_username} in {chattitle}", url="https://t.me/c/100/1"),
                        InlineKeyboardButton(f"PN {expected_username}", url=f"https://t.me/maxmuster")]]


def test_compose_buttons_without_username():
    chattitle = "Chat Title"
    invite_link = "https://test.example/url"
    user = User(id=0)
    user.first_name = "First"
    user.last_name = "Last"
    chat = Chat(id=100, type="Text", title=chattitle)
    message = Message(message_id=1, chat=chat, from_user=user)
    # act
    buttons = compose_buttons(message, invite_link=invite_link)
    assert buttons == [[
        InlineKeyboardButton(
            f"First Last in {chattitle}", url="https://t.me/c/100/1"),
        InlineKeyboardButton(f"Join {chattitle}", url=invite_link)]]


def test_compose_buttons_without_invitelink():
    chattitle = "Chat Title"
    user = User(id=0)
    user.first_name = "First"
    chat = Chat(id=100, type="Text", title=chattitle)
    message = Message(message_id=1, chat=chat, from_user=user)
    # act
    buttons = compose_buttons(message)
    assert buttons == [[InlineKeyboardButton(
        f"First in {chattitle}", url="https://t.me/c/100/1")]]
