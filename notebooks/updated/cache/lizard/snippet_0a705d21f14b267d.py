def list_publications():
    publications = search_publications(DBPublication(is_public=True))
    return SimpleTemplate(INDEX_TEMPLATE).render(publications=publications,
        compose_path=web_tools.compose_path, delimiter=':')