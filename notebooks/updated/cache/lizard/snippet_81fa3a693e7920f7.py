def create_qgis_template_output(output_path, layout):
    dirname = os.path.dirname(output_path)
    if not os.path.exists(dirname):
        os.makedirs(dirname)
    context = QgsReadWriteContext()
    context.setPathResolver(QgsProject.instance().pathResolver())
    layout.saveAsTemplate(output_path, context)
    return output_path