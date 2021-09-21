"""Role testing files using testinfra."""


def test_user_foo(host):
    """Validate a user foo exists and has the correct values"""

    user = host.user("foo")
    assert user.uid == 1042


def test_user_bar(host):
    """Validate a user bar exists and has the correct values"""

    user = host.user("bar")
    assert user.uid == 1043
    assert user.home == "/opt/baz"
