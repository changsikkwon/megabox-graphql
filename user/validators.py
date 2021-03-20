import re


def account_validation(value):
    regex_account = re.compile("^.*(?=^.{8,12}$)(?=.*\d)(?=.*[a-zA-Z]).*$")
    return regex_account.search(value)


def password_validation(value):
    regex_password = re.compile("^.*(?=^.{8,15}$)(?=.*\d)(?=.*[a-zA-Z])(?=.*[!@#$%^&+=]).*$")
    return regex_password.search(value)


def phone_number_validation(value):
    regex_phone_number = re.compile("^\+?1?\d{9,15}$")
    return regex_phone_number.search(value)
