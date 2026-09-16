def kml_master():
    kml_doc = KMLMaster(app.config['url_formatter'], app.config[
        'mapsources'].values())
    return kml_response(kml_doc)