def verify_checksum(message, previous_csum=0):
    if message.message_type in CHECKSUM_MSG_TYPES:
        csum = compute_checksum(message.checksum[0], message.args,
            previous_csum)
        if csum == message.checksum[1]:
            return True
        else:
            return False
    else:
        return True