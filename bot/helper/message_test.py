from pyrogram.types import (
    InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, ChatInviteLink)
from pyrogram.types import (User, Message, Chat)
from message import send_message


def test_send_message():
    chattitle = "Chat Title"
    user = User(id=0)
    user.first_name = "First"
    user.username = "maxmuster"
    chat = Chat(id=100, type="Text", title=chattitle)
    message = Message(message_id=1, chat=chat, from_user=user)
    app = TestApp()
    # act
    sent_message = send_message(message, 100, app)
    # assert
    assert sent_message == "sent message"
    print(app.arg_reply_markup)
    assert isinstance(app.arg_reply_markup.inline_keyboard[0][0], InlineKeyboardButton)


class TestApp:
    arg_copy_message = None
    arg_reply_markup = None
    example_invite_link = "https://test_invite_link"

    def copy_message(self, chat_id, source_chat_id, source_message_id,
                     reply_markup=None):
        self.arg_reply_markup = reply_markup
        return "sent message"

    def create_chat_invite_link(self, chat_id, name="Test", expire_date=None):
        if expire_date:
            assert isinstance(expire_date, int)
        return TestChatInviteLink()

class TestChatInviteLink:
    invite_link = "https://test_invite_link"