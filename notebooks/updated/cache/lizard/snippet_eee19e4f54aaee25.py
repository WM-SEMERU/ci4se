def setup_fixtures(self, context):
    if getattr(context, 'fixtures', None):
        context.test.fixtures = copy(context.fixtures)
    if getattr(context, 'reset_sequences', None):
        context.test.reset_sequences = context.reset_sequences
    if getattr(context, 'multi_db', None):
        context.test.__class__.multi_db = context.multi_db
    if hasattr(context, 'scenario'):
        load_registered_fixtures(context)