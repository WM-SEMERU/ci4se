def bio_EventRelated(epoch, event_length, window_post_ecg=0,
    window_post_rsp=4, window_post_eda=4, ecg_features=['Heart_Rate',
    'Cardiac_Phase', 'RR_Interval', 'RSA', 'HRV']):
    bio_response = {}
    ECG_Response = ecg_EventRelated(epoch, event_length, window_post=
        window_post_ecg, features=ecg_features)
    bio_response.update(ECG_Response)
    RSP_Response = rsp_EventRelated(epoch, event_length, window_post=
        window_post_rsp)
    bio_response.update(RSP_Response)
    EDA_Response = eda_EventRelated(epoch, event_length, window_post=
        window_post_eda)
    bio_response.update(EDA_Response)
    return bio_response