def run(self, *args, **kwargs):
    pm = MayaPluginManager.get()
    guerilla = pm.get_plugin('GuerillaMGMT')
    mayawin = maya_main_window()
    guerilla.run(parent=mayawin)