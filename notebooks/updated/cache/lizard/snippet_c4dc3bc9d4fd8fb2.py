def datasets(self):
    return self.session.query(Dataset).filter(Dataset.vid != ROOT_CONFIG_NAME_V
        ).all()