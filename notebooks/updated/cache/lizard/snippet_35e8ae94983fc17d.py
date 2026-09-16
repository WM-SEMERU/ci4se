def main():
    usage = """

  %prog [options] XML_PATH

Arguments:

  XML_PATH              the directory containing the GermaNet .xml files"""
    parser = optparse.OptionParser(usage=usage)
    parser.add_option('--host', default=None, help=
        'hostname or IP address of the MongoDB instance where the GermaNet database will be inserted (default: %default)'
        )
    parser.add_option('--port', type='int', default=None, help=
        'port number of the MongoDB instance where the GermaNet database will be inserted (default: %default)'
        )
    parser.add_option('--database', dest='database_name', default=
        'germanet', help=
        'the name of the database on the MongoDB instance where GermaNet will be stored (default: %default)'
        )
    options, args = parser.parse_args()
    if len(args) != 1:
        parser.error('incorrect number of arguments')
        sys.exit(1)
    xml_path = args[0]
    client = MongoClient(options.host, options.port)
    germanet_db = client[options.database_name]
    lex_files, gn_rels_file, wiktionary_files, ili_files = (
        find_germanet_xml_files(xml_path))
    insert_lexical_information(germanet_db, lex_files)
    insert_relation_information(germanet_db, gn_rels_file)
    insert_paraphrase_information(germanet_db, wiktionary_files)
    insert_lemmatisation_data(germanet_db)
    insert_infocontent_data(germanet_db)
    compute_max_min_depth(germanet_db)
    client.close()