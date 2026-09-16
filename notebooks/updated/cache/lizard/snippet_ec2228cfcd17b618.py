def global_id_field(type_name, id_fetcher=None):
    return GraphQLField(GraphQLNonNull(GraphQLID), description=
        'The ID of an object', resolver=lambda obj, args, context, info:
        to_global_id(type_name or info.parent_type.name, id_fetcher(obj,
        context, info) if id_fetcher else obj.id))