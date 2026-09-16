def _pick_keywords(db):
    for key, val in tqdm(db.iteritems(), total=len(db)):
        if key == 'last_id':
            continue
        piece = val[:500] if len(val) > 500 else val
        if '<fixfield id="001">ph' not in piece.lower():
            continue
        parsed = MARCXMLRecord(val)
        code = parsed.get('001')
        if not code:
            continue
        if parsed['682i']:
            continue
        if code.lower().startswith('ph'):
            yield KeywordInfo.from_marc(sysno=int(key.split('_')[-1]), marc
                =parsed)