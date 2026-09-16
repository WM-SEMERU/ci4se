def create(embedding_name, **kwargs):
    create_text_embedding = registry.get_create_func(_TokenEmbedding,
        'token embedding')
    return create_text_embedding(embedding_name, **kwargs)