import pytest

from app.utils.validator import validate_email, validate_password_policy


def test_alidate_email_is_valid():
    valid_email = "testMail@example.com"

    assert validate_email(valid_email) == True


def test_validate_email_is_invalid():
    invalid_email = "testmail.youcandoit"

    assert validate_email(invalid_email) == False


def test_validate_password_policy_is_valid():
    valid_password = "Admin_123!"

    assert validate_password_policy(valid_password) == True


def test_validate_password_policy_is_less_than_8_return_false():
    password = "abcdef"

    assert validate_password_policy(password) == False


def test_validate_password_policy_is_greater_than_8_but_only_uppercase_return_false():
    password = "ABCDEF"

    assert validate_password_policy(password) == False


def test_validate_password_policy_is_greater_than_8_but_only_lowercase_return_false():
    password = "abcdefdsa"

    assert validate_password_policy(password) == False


def test_validate_password_policy_is_greater_than_8_but_only_lowercase_with_numeric_return_false():
    password = "abcdef1234"

    assert validate_password_policy(password) == False


def test_validate_password_policy_is_greater_than_8_but_only_uppercase_with_numeric_return_false():
    password = "ABCDEF1234"

    assert validate_password_policy(password) == False


def test_validate_password_policy_is_greater_than_8_have_upper_and_lowercase_but_no_special_characters_return_false():
    password = "AbcDEF1234"

    assert validate_password_policy(password) == False


def test_validate_password_policy_is_greater_than_8_have_upper_and_lowercase_and_special_characters_is_valid():
    password = "AbcDEF1234@!"

    assert validate_password_policy(password) == True
