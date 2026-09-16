def _contains_blinded_text(stats_xml):
    tree = ET.parse(stats_xml)
    root = tree.getroot()
    total_tokens = int(root.find('size/total/tokens').text)
    unique_lemmas = int(root.find('lemmas').get('unique'))
    return unique_lemmas / total_tokens < 0.01