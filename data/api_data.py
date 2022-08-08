from cfg.config import USER_NAME, PASSWORD, INVALID_USER_NAME, INVALID_PASS


class AuthData:
    valid_auth_data = {
        "userName": f"{USER_NAME}",
        "password": f"{PASSWORD}"
    }

    invalid_user_name = {
        "userName": f"{INVALID_USER_NAME}",
        "password": f"{PASSWORD}"
    }

    invalid_pass = {
        "userName": f"{USER_NAME}",
        "password": f"{INVALID_PASS}"
    }
