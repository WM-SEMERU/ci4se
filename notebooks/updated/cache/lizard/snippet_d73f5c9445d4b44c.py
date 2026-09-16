def get_entry_compact_text_repr(entry, entries):
    text = get_shortest_text_value(entry)
    if text is not None:
        return text
    else:
        sources = get_sourced_from(entry)
        if sources is not None:
            texts = []
            for source in sources:
                source_entry = entries[source]
                texts.append(get_shortest_text_value(source_entry))
            return get_shortest_string(texts)