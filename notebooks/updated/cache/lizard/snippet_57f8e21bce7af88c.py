def run(self):
    df = ArtistsInputData().load()
    base_data = self.client.df_query(self.session.query(models.ArtistBase))
    df = df.merge(base_data, on='wiki_id')
    df.rename(columns={'artistLabel': 'name', 'genderLabel': 'gender'},
        inplace=True)
    columns = ['name', 'id']
    if config.EXTENDED:
        columns += ['gender', 'year_of_birth']
    df = df[columns]
    df.to_sql(name=models.Artist.__tablename__, con=self.client.engine,
        if_exists='append', index=False)
    self.done()