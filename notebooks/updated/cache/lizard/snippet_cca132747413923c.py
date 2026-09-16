def from_client(catalog, client_id, lowcut, highcut, samp_rate, filt_order,
    length, prepick, swin, process_len=86400, data_pad=90, all_horiz=False,
    delayed=True, plot=False, debug=0, return_event=False, min_snr=None):
    EQcorrscanDeprecationWarning(
        'Function is depreciated and will be removed soon. Use template_gen.template_gen instead.'
        )
    temp_list = template_gen(method='from_client', catalog=catalog,
        client_id=client_id, lowcut=lowcut, highcut=highcut, samp_rate=
        samp_rate, filt_order=filt_order, length=length, prepick=prepick,
        swin=swin, process_len=process_len, data_pad=data_pad, all_horiz=
        all_horiz, delayed=delayed, plot=plot, debug=debug, return_event=
        return_event, min_snr=min_snr)
    return temp_list