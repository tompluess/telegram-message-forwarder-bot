from email.mime import image
from pyrogram.types import (
    InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, ChatInviteLink)
from pyrogram.types import (User, Message, Chat, Photo)
from message import send_message, reset_messages_cache, accepted_message

def test_accepted_messages_image():
    chattitle = "Chat Title"
    user = User(id=0)
    user.first_name = "First"
    user.username = "maxmuster"
    chat = Chat(id=100, type="Text", title=chattitle)
    message = Message(message_id=1, chat=chat,
                      from_user=user,  media="test-image.jpg", caption="test")
    result = accepted_message(None, None, message)
    assert result == True

def test_accepted_messages_text():
    chattitle = "Chat Title"
    user = User(id=0)
    user.first_name = "First"
    user.username = "maxmuster"
    chat = Chat(id=100, type="Text", title=chattitle)
    message = Message(message_id=1, chat=chat,
                      from_user=user, text="Text with more than 10 characters")
    result = accepted_message(None, None, message)
    assert result == True

def test_accepted_messages_very_short_text():
    chattitle = "Chat Title"
    user = User(id=0)
    user.first_name = "First"
    user.username = "maxmuster"
    chat = Chat(id=100, type="Text", title=chattitle)
    message = Message(message_id=1, chat=chat,
                      from_user=user, text="Hello")
    result = accepted_message(None, None, message)
    assert result == False

def test_accepted_messages_command():
    chattitle = "Chat Title"
    user = User(id=0)
    user.first_name = "First"
    user.username = "maxmuster"
    chat = Chat(id=100, type="Text", title=chattitle)
    message = Message(message_id=1, chat=chat,
                      from_user=user, text="/command")
    result = accepted_message(None, None, message)
    assert result == False

def test_accepted_messages_command():
    chattitle = "Chat Title"
    user = User(id=0)
    user.first_name = "First"
    user.username = "maxmuster"
    chat = Chat(id=100, type="Text", title=chattitle)
    message = Message(message_id=1, chat=chat,
                      from_user=user, text="@user xyz hello")
    result = accepted_message(None, None, message)
    assert result == False

def test_send_message():
    reset_messages_cache()
    chattitle = "Chat Title"
    user = User(id=0)
    user.first_name = "First"
    user.username = "maxmuster"
    chat = Chat(id=100, type="Text", title=chattitle)
    message = Message(message_id=1, chat=chat,
                      from_user=user, text="Hello Text")
    app = TestApp()
    # act
    sent_message = send_message(message, 100, app)
    # assert
    assert sent_message.text == "sent message"
    assert isinstance(
        app.arg_reply_markup.inline_keyboard[0][0], InlineKeyboardButton)
    assert app.count_copy_message == 1


def test_send_text_message_twice():
    reset_messages_cache()
    chattitle = "Chat Title"
    user = User(id=0)
    user.first_name = "First"
    user.username = "maxmuster"
    chat = Chat(id=100, type="Text", title=chattitle)
    message = Message(message_id=1, chat=chat,
                      from_user=user, text="Hello Text")
    app = TestApp()
    # act
    sent_message = send_message(message, 100, app)
    sent_message = send_message(message, 100, app)
    # assert
    assert sent_message == None
    assert app.count_copy_message == 1


class TestApp:
    count_copy_message = 0
    arg_chat_id = None
    arg_source_chat_id = None
    arg_source_message_id = None
    arg_reply_markup = None
    example_invite_link = "https://test_invite_link"

    def copy_message(self, chat_id, source_chat_id, source_message_id,
                     reply_markup=None):
        self.count_copy_message = self.count_copy_message+1
        self.arg_chat_id = chat_id
        self.arg_source_chat_id = source_chat_id
        self.arg_source_message_id = source_message_id
        self.arg_reply_markup = reply_markup
        return Message(message_id=9,chat=chat_id,from_user=99,text="sent message")

    def create_chat_invite_link(self, chat_id, name="Test", expire_date=None):
        if expire_date:
            assert isinstance(expire_date, int)
        return TestChatInviteLink()


class TestChatInviteLink:
    invite_link = "https://test_invite_link"
