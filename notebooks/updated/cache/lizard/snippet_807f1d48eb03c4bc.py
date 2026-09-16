def get(self):
    args = self.get_parser.parse_args()
    cred = self.manager.get_credential(args)
    if cred is None:
        return abort(http_client.BAD_REQUEST, message=
            'Unable to decrypt credential value.')
    else:
        return cred