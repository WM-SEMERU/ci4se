def get_version():
    path = os.path.join(os.path.dirname(__file__), 'backrefs')
    fp, pathname, desc = imp.find_module('__meta__', [path])
    try:
        vi = imp.load_module('__meta__', fp, pathname, desc).__version_info__
        return vi._get_canonical(), vi._get_dev_status()
    except Exception:
        print(traceback.format_exc())
    finally:
        fp.close()