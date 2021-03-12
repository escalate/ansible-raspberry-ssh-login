"""Role testing files using testinfra"""


def test_login_user(host):
    """Check login user"""
    g = host.group("berry")
    assert g.exists

    u = host.user("rasp")
    assert u.exists

    public_key = "ssh-ed25519 RASPI"
    f = host.file("/home/rasp/.ssh/authorized_keys").content_string
    assert public_key in f


def test_root_user(host):
    """Check root user"""
    u = host.user("root")
    assert u.password == "*"

    f = host.file("/root/.ssh/authorized_keys")
    assert f.exists is False


def test_pi_user(host):
    """Check pi user"""
    u = host.user("pi")
    assert u.password == "*"

    f = host.file("/home/pi/.ssh/authorized_keys")
    assert f.exists is False
