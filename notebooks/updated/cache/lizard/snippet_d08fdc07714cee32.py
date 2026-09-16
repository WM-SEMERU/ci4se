def initialize_environment(app):
    env = app.builder.env
    if not hasattr(env, 'traceability_all_items'):
        env.traceability_all_items = {}
    update_available_item_relationships(app)