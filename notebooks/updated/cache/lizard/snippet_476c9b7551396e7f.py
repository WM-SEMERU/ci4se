def process_file(self, data, name):
    try:
        return self.process_file_autodetect(data, name)
    except Exception as e:
        logger.debug('Exception processing file %s : %s' % (name, e))
        self.trace_logger.log(e)
    ret = []
    logger.debug('processing %s as PEM' % name)
    ret.append(self.process_pem(data, name))
    logger.debug('processing %s as DER' % name)
    ret.append(self.process_der(data, name))
    logger.debug('processing %s as PGP' % name)
    ret.append(self.process_pgp(data, name))
    logger.debug('processing %s as SSH' % name)
    ret.append(self.process_ssh(data, name))
    logger.debug('processing %s as JSON' % name)
    ret.append(self.process_json(data, name))
    logger.debug('processing %s as APK' % name)
    ret.append(self.process_apk(data, name))
    logger.debug('processing %s as MOD' % name)
    ret.append(self.process_mod(data, name))
    logger.debug('processing %s as LDIFF' % name)
    ret.append(self.process_ldiff(data, name))
    logger.debug('processing %s as JKS' % name)
    ret.append(self.process_jks(data, name))
    logger.debug('processing %s as PKCS7' % name)
    ret.append(self.process_pkcs7(data, name))
    return ret