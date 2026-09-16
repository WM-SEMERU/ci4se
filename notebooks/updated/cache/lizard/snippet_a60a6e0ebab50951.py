def _createSchemaFiles(self, destPath, schemasPath):
    ga4ghPath = os.path.join(destPath, 'ga4gh')
    if not os.path.exists(ga4ghPath):
        os.mkdir(ga4ghPath)
    ga4ghSchemasPath = os.path.join(ga4ghPath, 'schemas')
    if not os.path.exists(ga4ghSchemasPath):
        os.mkdir(ga4ghSchemasPath)
    ga4ghSchemasGa4ghPath = os.path.join(ga4ghSchemasPath, 'ga4gh')
    if not os.path.exists(ga4ghSchemasGa4ghPath):
        os.mkdir(ga4ghSchemasGa4ghPath)
    ga4ghSchemasGooglePath = os.path.join(ga4ghSchemasPath, 'google')
    if not os.path.exists(ga4ghSchemasGooglePath):
        os.mkdir(ga4ghSchemasGooglePath)
    ga4ghSchemasGoogleApiPath = os.path.join(ga4ghSchemasGooglePath, 'api')
    if not os.path.exists(ga4ghSchemasGoogleApiPath):
        os.mkdir(ga4ghSchemasGoogleApiPath)
    for root, dirs, files in os.walk(schemasPath):
        for protoFilePath in fnmatch.filter(files, '*.proto'):
            src = os.path.join(root, protoFilePath)
            dst = os.path.join(ga4ghSchemasPath, os.path.relpath(root,
                schemasPath), protoFilePath)
            self._copySchemaFile(src, dst)