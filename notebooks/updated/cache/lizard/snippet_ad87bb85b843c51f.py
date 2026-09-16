def process_jwt(jwt):
    header, claims, _ = jwt.split('.')
    parsed_header = json_decode(base64url_decode(header))
    parsed_claims = json_decode(base64url_decode(claims))
    return parsed_header, parsed_claims