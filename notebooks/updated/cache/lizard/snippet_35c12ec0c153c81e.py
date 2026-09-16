def check_collections_are_supported(saved_model_handler, supported):
    for meta_graph in saved_model_handler.meta_graphs:
        used_collection_keys = set(meta_graph.collection_def.keys())
        unsupported = used_collection_keys - supported
        if unsupported:
            raise ValueError(
                """Unsupported collections in graph: %s
Use hub.create_module_spec(..., drop_collections=[...]) as appropriate."""
                 % list(unsupported))