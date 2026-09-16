def get_chacra_repo(shaman_url):
    shaman_response = get_request(shaman_url)
    chacra_url = shaman_response.geturl()
    chacra_response = get_request(chacra_url)
    return chacra_response.read()