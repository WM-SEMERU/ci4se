def _no_answer_do_retry(self, pk, pattern):
    logger.info('Resending for pattern %s', pattern)
    self.send_packet(pk, expected_reply=pattern, resend=True)