def create_isobaric_quant_lookup(quantdb, specfn_consensus_els, channelmap):
    channels_store = ((name,) for name, c_id in sorted(channelmap.items(),
        key=lambda x: x[1]))
    quantdb.store_channelmap(channels_store)
    channelmap_dbid = {channelmap[ch_name]: ch_id for ch_id, ch_name in
        quantdb.get_channelmap()}
    quants = []
    mzmlmap = quantdb.get_mzmlfile_map()
    for specfn, consensus_el in specfn_consensus_els:
        rt = openmsreader.get_consxml_rt(consensus_el)
        rt = round(float(Decimal(rt) / 60), 12)
        qdata = get_quant_data(consensus_el)
        spectra_id = quantdb.get_spectra_id(mzmlmap[specfn], retention_time=rt)
        for channel_no in sorted(qdata.keys()):
            quants.append((spectra_id, channelmap_dbid[channel_no], qdata[
                channel_no]))
            if len(quants) == DB_STORE_CHUNK:
                quantdb.store_isobaric_quants(quants)
    quantdb.store_isobaric_quants(quants)
    quantdb.index_isobaric_quants()