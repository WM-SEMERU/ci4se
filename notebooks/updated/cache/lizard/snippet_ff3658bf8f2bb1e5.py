def make_user_role_table(table_name='user', id_column_name='id'):
    return db.Table('fp_user_role', db.Column('user_id', db.Integer, db.
        ForeignKey('{}.{}'.format(table_name, id_column_name))), db.Column(
        'role_id', db.Integer, db.ForeignKey('fp_role.id')),
        extend_existing=True)