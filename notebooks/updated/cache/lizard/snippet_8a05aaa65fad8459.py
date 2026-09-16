def get_next_neighbour(i, paragraphs, ignore_neargood):
    return _get_neighbour(i, paragraphs, ignore_neargood, 1, len(paragraphs))