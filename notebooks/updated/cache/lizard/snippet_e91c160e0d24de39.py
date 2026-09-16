def convert_translations(self, dest_dir):
    if not os.path.isdir(dest_dir):
        os.makedirs(dest_dir)
    total_translation_rows = 0
    with open(os.path.join(dest_dir, 'translations.txt'), 'w+b') as out_file:
        writer = csv.DictWriter(out_file, fieldnames=NEW_TRANSLATIONS_FIELDS)
        writer.writeheader()
        for filename in sorted(os.listdir(self.src_dir)):
            if not (filename.endswith('.txt') and os.path.isfile(os.path.
                join(self.src_dir, filename))):
                print('Skipping %s' % filename)
                continue
            table_name = filename[:-len('.txt')]
            if table_name == 'translations':
                continue
            total_translation_rows += self._translate_table(dest_dir,
                table_name, writer)
    print('Total translation rows: %s' % total_translation_rows)