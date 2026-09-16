def create_iam(self):
    utils.banner('Creating IAM')
    iam.create_iam_resources(env=self.env, app=self.app)