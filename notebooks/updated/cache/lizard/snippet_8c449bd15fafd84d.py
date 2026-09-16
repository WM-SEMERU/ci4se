def get_signing_key(self, algorithm, service_context):
    return service_context.keyjar.get_signing_key(alg2keytype(algorithm),
        alg=algorithm)