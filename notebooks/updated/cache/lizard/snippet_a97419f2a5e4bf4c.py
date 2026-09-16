def find_third_party_modules():
    parent = os.path.dirname(os.path.dirname(__file__))
    third_party = os.path.join(parent, 'third_party')
    if os.path.isdir(third_party):
        sys.path.append(os.path.join(third_party, 'dnspython'))