def _perform_radius_auth(self, client, packet):
    try:
        reply = client.SendPacket(packet)
    except Timeout as e:
        logging.error('RADIUS timeout occurred contacting %s:%s' % (client.
            server, client.authport))
        return False
    except Exception as e:
        logging.error('RADIUS error: %s' % e)
        return False
    if reply.code == AccessReject:
        logging.warning("RADIUS access rejected for user '%s'" % packet[
            'User-Name'])
        return False
    elif reply.code != AccessAccept:
        logging.error("RADIUS access error for user '%s' (code %s)" % (
            packet['User-Name'], reply.code))
        return False
    logging.info("RADIUS access granted for user '%s'" % packet['User-Name'])
    return True