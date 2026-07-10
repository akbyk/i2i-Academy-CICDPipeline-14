from app import is_valid_email


def test_is_valid_email():
    # Valid email formats should return True
    assert is_valid_email("user@example.com") is True
    assert is_valid_email("first.last@sub.domain.co") is True

    # Invalid email formats should return False
    assert is_valid_email("not-an-email") is False
    assert is_valid_email("missing@domain") is False
    assert is_valid_email("") is False