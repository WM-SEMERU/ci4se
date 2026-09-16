def listing(parser, token):
    var_name, parameters = listing_parse(token.split_contents())
    return ListingNode(var_name, parameters)