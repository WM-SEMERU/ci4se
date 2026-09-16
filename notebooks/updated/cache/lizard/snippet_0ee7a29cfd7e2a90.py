def check_auth(email, password):
    try:
        user = User.get(User.email == email)
    except User.DoesNotExist:
        return False
    return password == user.password