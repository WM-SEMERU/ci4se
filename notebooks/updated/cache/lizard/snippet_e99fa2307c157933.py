def upgrade():
    op.drop_constraint('fk_oauth2server_client_user_id_accounts_user',
        'oauth2server_client', type_='foreignkey')
    op.create_foreign_key(op.f(
        'fk_oauth2server_client_user_id_accounts_user'),
        'oauth2server_client', 'accounts_user', ['user_id'], ['id'],
        ondelete='CASCADE')
    op.create_index(op.f('ix_oauth2server_client_user_id'),
        'oauth2server_client', ['user_id'], unique=False)
    op.drop_constraint('fk_oauth2server_token_user_id_accounts_user',
        'oauth2server_token', type_='foreignkey')
    op.create_foreign_key(op.f(
        'fk_oauth2server_token_user_id_accounts_user'),
        'oauth2server_token', 'accounts_user', ['user_id'], ['id'],
        ondelete='CASCADE')
    op.create_index(op.f('ix_oauth2server_token_user_id'),
        'oauth2server_token', ['user_id'], unique=False)
    op.drop_constraint('fk_oauth2server_token_client_id_oauth2server_client',
        'oauth2server_token', type_='foreignkey')
    op.create_foreign_key(op.f(
        'fk_oauth2server_token_client_id_oauth2server_client'),
        'oauth2server_token', 'oauth2server_client', ['client_id'], [
        'client_id'], ondelete='CASCADE')
    op.create_index(op.f('ix_oauth2server_token_client_id'),
        'oauth2server_token', ['client_id'], unique=False)