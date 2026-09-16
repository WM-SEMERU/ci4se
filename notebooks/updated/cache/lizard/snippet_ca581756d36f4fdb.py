def search(self, **kwargs):
    region = kwargs.get('region', self.region)
    kwargs.update({'region': region})
    return AmazonSearch(self.api, self.aws_associate_tag, **kwargs)