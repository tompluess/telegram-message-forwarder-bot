import logging
from pyrogram.types import (
    InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, ChatInviteLink)
from pyrogram.types import (User, Message, Chat)
from invite_links import get_invite_link, reset_invite_links

LOG = logging.getLogger(__name__)


def test_get_invite_link():
    reset_invite_links()
    app = TestApp()
    # act
    invite_link = get_invite_link(100, app)
    # assert
    assert invite_link == ChatInviteLinkFixture.invite_link_base+"1"


def test_get_invite_link_no_permission():
    reset_invite_links()
    app = AppNoPermissionFixture()
    # act
    invite_link = get_invite_link(100, app)
    # assert
    assert invite_link == None


def test_get_invite_link_twice():
    reset_invite_links()
    app = TestApp()
    # act
    invite_link = get_invite_link(100, app)
    invite_link = get_invite_link(100, app)
    # assert
    assert invite_link == ChatInviteLinkFixture.invite_link_base+"1"

def test_get_invite_link_twice_different_chats():
    reset_invite_links()
    app = TestApp()
    # act
    invite_link = get_invite_link(100, app)
    invite_link = get_invite_link(200, app)
    # assert
    assert invite_link == ChatInviteLinkFixture.invite_link_base+"2"



class TestApp:
    count = 0

    def create_chat_invite_link(self, chat_id, creates_join_request=False, name="Test", expire_date=None):
        assert chat_id, "chat id mandatory"
        assert creates_join_request, "join request mandatory"
        #LOG.debug(f"link name: {name}")
        if expire_date:
            assert isinstance(expire_date, int)
        self.count = self.count+1
        return ChatInviteLinkFixture(self.count)


class ChatInviteLinkFixture:
    invite_link_base = "https://test_invite_link"

    def __init__(self, id):
        self.invite_link = self.invite_link_base+str(id)


class AppNoPermissionFixture:
    def create_chat_invite_link(self, chat_id, name="Test", expire_date=None):
        raise RuntimeError('simulated no permission exception')
