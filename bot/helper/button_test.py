from pyrogram.types import (
    InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup)
from button import compose_buttons
from pyrogram.types import (User, Message, Chat)


def test_compose_buttons_with_username():
    chattitle="Chat Title"
    user = User(id=0)
    user.first_name = "First"
    user.username = "maxmuster"
    chat = Chat(id=100, type="Text", title=chattitle)
    message = Message(message_id=1, chat=chat, from_user=user)
    # act
    buttons = compose_buttons(message)
    assert buttons == [[InlineKeyboardButton(chattitle, url="https://t.me/c/100/1"),
                        InlineKeyboardButton(f"PN First @maxmuster", url=f"https://t.me/maxmuster")]]

def test_compose_buttons_without_username():
    chattitle="Chat Title"
    user = User(id=0)
    user.first_name = "First"
    chat = Chat(id=100, type="Text", title=chattitle)
    message = Message(message_id=1, chat=chat, from_user=user)
    # act
    buttons = compose_buttons(message)
    assert buttons == [[InlineKeyboardButton(f"First in {chattitle}", url="https://t.me/c/100/1")]]
