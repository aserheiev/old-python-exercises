def check_email(string):
    check = []
    at = "@" not in string
    dot = ".@" in string or "@." in string
    space = " " in string
    check = [at, dot, space]
    at_index = string.find("@")
    has_dot = string.find(".", at_index)
    if has_dot == -1:
        check.append(True)
    return not any(check)

def check_email(string):
    email = string
    if "@." in email or " " in email or email.count('@') > 1 or email.rfind("@") > email.rfind("."):
        return False
    elif "@" not in email or "." not in email:
        return False

    return True


check_email(input())