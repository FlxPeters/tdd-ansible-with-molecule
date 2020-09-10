"""Playbook testing files using testinfra."""


def test_user_demo(host):
    """Validate a user demo exists and has the correct values"""

    user = host.user("demo")
    assert user.exists


def test_secret_for_user_demo(host):
    """Validate file access for user demo"""

    secret = host.file("/opt/secrets/message.txt")
    assert secret.exists
    assert secret.is_file
    assert secret.user == "demo"
    assert secret.mode == 0o600
    assert secret.content_string == "Secure"
