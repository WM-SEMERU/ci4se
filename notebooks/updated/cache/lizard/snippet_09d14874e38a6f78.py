def init_db(self):
    db_url = self.config.get('database_url', 'sqlite:///nautilus.db')
    nautilus.database.init_db(db_url)