def fetch_node_status(member):
    try:
        response = requests.get(member.api_url, timeout=2, verify=False)
        logger.info('Got response from %s %s: %s', member.name, member.
            api_url, response.content)
        return _MemberStatus.from_api_response(member, response.json())
    except Exception as e:
        logger.warning('Request failed to %s: GET %s (%s)', member.name,
            member.api_url, e)
    return _MemberStatus.unknown(member)