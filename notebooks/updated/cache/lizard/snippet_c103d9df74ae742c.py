def write_docs(self):
    if self.doc_list:
        dataPath = self.client.local_dir
        dump_file = open('data/' + urllib.parse.quote_plus(self.uri +
            '?view=documents') + '.json', mode='w')
        dump_file.write('[' + json.dumps(self.doc_list[0]))
        for i in range(1, len(self.doc_list)):
            dump_file.write(',' + json.dumps(self.doc_list[i]))
        dump_file.write(']')
        dump_file.close()
        logger.info('Wrote ' + self.uri + '?view=documents to file')
        return True
    else:
        logger.warning('No doclist to write for ' + self.uri)
        return False