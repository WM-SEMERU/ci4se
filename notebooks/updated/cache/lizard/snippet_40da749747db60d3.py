def ArgList(args, lparen=LParen(), rparen=RParen()):
    node = Node(syms.trailer, [lparen.clone(), rparen.clone()])
    if args:
        node.insert_child(1, Node(syms.arglist, args))
    return node