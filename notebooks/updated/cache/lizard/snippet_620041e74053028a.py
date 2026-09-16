def from_file(file_path, elem_delim=' ', encoding='utf8', **kwargs):
    embedding = TokenEmbedding(**kwargs)
    embedding._load_embedding(file_path, elem_delim=elem_delim, encoding=
        encoding)
    return embedding