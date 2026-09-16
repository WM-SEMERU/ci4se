def check_chain(chain):
    link = chain[0][0]
    for i in range(1, len(chain) - 1):
        if chain[i][1] == 'R':
            link = hash_function(link + chain[i][0]).digest()
        elif chain[i][1] == 'L':
            link = hash_function(chain[i][0] + link).digest()
        else:
            raise MerkleError('Link %s has no side value: %s' % (str(i),
                str(codecs.encode(chain[i][0], 'hex_codec'))))
    if link == chain[-1][0]:
        return link
    else:
        raise MerkleError('The Merkle Chain is not valid.')