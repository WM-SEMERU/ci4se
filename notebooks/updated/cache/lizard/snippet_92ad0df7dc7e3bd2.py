def fix_missing_lang_tags(marc_xml, dom):

    def get_lang_tag(lang):
        lang_str = '\n  <mods:language>\n'
        lang_str += '    <mods:languageTerm authority="iso639-2b" type="code">'
        lang_str += lang
        lang_str += '</mods:languageTerm>\n'
        lang_str += '  </mods:language>\n\n'
        lang_dom = dhtmlparser.parseString(lang_str)
        return first(lang_dom.find('mods:language'))
    for lang in reversed(marc_xml['041a0 ']):
        lang_tag = dom.find('mods:languageTerm', fn=lambda x: x.getContent(
            ).strip().lower() == lang.lower())
        if not lang_tag:
            insert_tag(get_lang_tag(lang), dom.find('mods:language'),
                get_mods_tag(dom))