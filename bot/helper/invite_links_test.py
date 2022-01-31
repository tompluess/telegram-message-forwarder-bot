from pyrogram.types import (
    InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, ChatInviteLink)
from pyrogram.types import (User, Message, Chat)
from invite_links import get_invite_link


def test_get_invite_link():
    app = TestApp()
    # act
    invite_link = get_invite_link(100, app)
    # assert
    assert invite_link == TestChatInviteLink.invite_link

def test_get_invite_link_no_permission():
    app = TestAppNoPermission()
    # act
    invite_link = get_invite_link(100, app)
    # assert
    assert invite_link == None


class TestApp:
    def create_chat_invite_link(self, chat_id, name="Test", expire_date=None):
        if expire_date:
            assert isinstance(expire_date, int)
        return TestChatInviteLink()

class TestChatInviteLink:
    invite_link = "https://test_invite_link"


class TestAppNoPermission:
    def create_chat_invite_link(self, chat_id, name="Test", expire_date=None):
        raise RuntimeError('simulated no permission exception')
