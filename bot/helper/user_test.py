from user import username_long

def test_username_long():
    user = type('', (object,), {
                'first_name': "First", 'last_name': None, 'username': None})()
    username = username_long(user)
    assert username == "First"

def test_username_long_first_last():
    user = type('', (object,), {
                'first_name': "First", 'last_name': "Last", 'username': None})()
    username = username_long(user)
    assert username == "First Last"

def test_username_long_with_username():
    user = type('', (object,), {
                'first_name': "First", 'last_name': None, 'username': "maxmuster"})()
    username = username_long(user)
    assert username == "First @maxmuster"

def test_username_long_firstname_null():
    user = type('', (object,), {
                'first_name': None, 'last_name': None, 'username': "maxmuster"})()
    username = username_long(user)
    assert username == "@maxmuster"
