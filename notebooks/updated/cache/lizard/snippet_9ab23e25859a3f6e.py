def classFactory(iface):
    try:
        from parameters.generic_parameter import GenericParameter
    except ImportError:
        QMessageBox.warning(None, QCoreApplication.translate('@default',
            'InaSAFE submodule not found'), QCoreApplication.translate(
            '@default',
            'InaSAFE could not find the submodule "parameters". You should do "git submodule update" or if you need a new clone, do "git clone --recursive git@github.com:inasafe/inasafe.git". If this is already a new clone, you should do "git submodule init" before "git submodule update".Finally, restart QGIS.'
            ))
    from .safe.plugin import Plugin
    return Plugin(iface)