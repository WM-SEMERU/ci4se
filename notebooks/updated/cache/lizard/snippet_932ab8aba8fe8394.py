def convert_path_to_flask(path):
    proxy_sub_path = APIGW_TO_FLASK_REGEX.sub(FLASK_CAPTURE_ALL_PATH, path)
    return proxy_sub_path.replace(LEFT_BRACKET, LEFT_ANGLE_BRACKET).replace(
        RIGHT_BRACKET, RIGHT_ANGLE_BRACKET)