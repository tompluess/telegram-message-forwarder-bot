from user import username_long
from pyrogram.types import (User)


def test_username_long():
    user = User(id=0)
    user.first_name = "First"
    username = username_long(user)
    assert username == "First"


def test_username_long_first_last():
    user = User(id=0)
    user.first_name = "First"
    user.last_name = "Last"
    username = username_long(user)
    assert username == "First Last"


def test_username_long_with_username():
    user = User(id=0)
    user.first_name = "First"
    user.username = "maxmuster"
    username = username_long(user)
    assert username == "First @maxmuster"


def test_username_long_firstname_null():
    user = User(id=0)
    user.username = "maxmuster"
    username = username_long(user)
    assert username == "@maxmuster"
