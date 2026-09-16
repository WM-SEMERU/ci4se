def rollback(self, revision):
    print('Rolling back..')
    self.zappa.rollback_lambda_function_version(self.lambda_name,
        versions_back=revision)
    print('Done!')