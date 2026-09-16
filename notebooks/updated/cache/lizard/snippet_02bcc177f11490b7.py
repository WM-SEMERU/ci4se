def get_witnesses(self, source_tree):
    witnesses = []
    witness_elements = source_tree.xpath(
        '/tei:*/tei:teiHeader/tei:fileDesc/tei:sourceDesc/tei:listWit/tei:witness'
        , namespaces=constants.NAMESPACES)
    for witness_element in witness_elements:
        witnesses.append((witness_element.text, witness_element.get(
            constants.XML + 'id')))
    if not witnesses:
        witnesses = [(constants.BASE_WITNESS, constants.BASE_WITNESS_ID)]
    return witnesses