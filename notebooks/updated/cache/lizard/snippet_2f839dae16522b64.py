def _store_gui_setting(self, databox, name):
    try:
        databox.insert_header(name, eval(name + '.get_value()'))
    except:
        print('ERROR: Could not store gui setting ' + repr(name))