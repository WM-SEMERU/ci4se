def _load_isd_file_metadata(download_path, isd_station_metadata):
    isd_inventory = pd.read_csv(os.path.join(download_path,
        'isd-inventory.csv'), dtype=str)
    station_keep = [(usaf in isd_station_metadata) for usaf in
        isd_inventory.USAF]
    isd_inventory = isd_inventory[station_keep]
    year_keep = isd_inventory.YEAR > '2005'
    isd_inventory = isd_inventory[year_keep]
    metadata = {}
    for (usaf_station, year), group in isd_inventory.groupby(['USAF', 'YEAR']):
        if usaf_station not in metadata:
            metadata[usaf_station] = {'usaf_id': usaf_station, 'years': {}}
        metadata[usaf_station]['years'][year] = [{'wban_id': row.WBAN,
            'counts': [row.JAN, row.FEB, row.MAR, row.APR, row.MAY, row.JUN,
            row.JUL, row.AUG, row.SEP, row.OCT, row.NOV, row.DEC]} for i,
            row in group.iterrows()]
    return metadata