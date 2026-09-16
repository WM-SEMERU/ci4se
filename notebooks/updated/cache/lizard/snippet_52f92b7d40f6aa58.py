def options(self, context, module_options):
    self.threads = 3
    self.csv_path = 'C:\\'
    self.collection_method = 'Default'
    self.neo4j_URI = ''
    self.neo4j_user = ''
    self.neo4j_pass = ''
    if module_options and 'THREADS' in module_options:
        self.threads = module_options['THREADS']
    if module_options and 'CSVPATH' in module_options:
        self.csv_path = module_options['CSVPATH']
    if module_options and 'COLLECTIONMETHOD' in module_options:
        self.collection_method = module_options['COLLECTIONMETHOD']
    if module_options and 'NEO4JURI' in module_options:
        self.neo4j_URI = module_options['NEO4JURI']
    if module_options and 'NEO4JUSER' in module_options:
        self.neo4j_user = module_options['NEO4JUSER']
    if module_options and 'NEO4JPASS' in module_options:
        self.neo4j_pass = module_options['NEO4JPASS']
    if (self.neo4j_URI != '' and self.neo4j_user != '' and self.neo4j_pass !=
        ''):
        self.opsec_safe = True
    self.ps_script = obfs_ps_script('BloodHound-modified.ps1')