def to_yaml(self, skip_nulls=True):
    return yaml.safe_dump(self.to_dict(skip_nulls=skip_nulls),
        default_flow_style=False)