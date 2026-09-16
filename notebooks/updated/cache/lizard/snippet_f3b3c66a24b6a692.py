def generate_single_seasonal_average(args):
    qout_file = args[0]
    seasonal_average_file = args[1]
    day_of_year = args[2]
    mp_lock = args[3]
    min_day = day_of_year - 3
    max_day = day_of_year + 3
    with RAPIDDataset(qout_file) as qout_nc_file:
        time_indices = []
        for idx, t in enumerate(qout_nc_file.get_time_array()):
            var_time = gmtime(t)
            compare_yday = var_time.tm_yday
            if isleap(var_time.tm_year) and compare_yday > 60:
                compare_yday -= 1
            if max_day > compare_yday >= min_day:
                time_indices.append(idx)
        if not time_indices:
            raise IndexError('No time steps found within range ...')
        streamflow_array = qout_nc_file.get_qout(time_index_array=time_indices)
    avg_streamflow_array = np.mean(streamflow_array, axis=1)
    std_streamflow_array = np.std(streamflow_array, axis=1)
    max_streamflow_array = np.amax(streamflow_array, axis=1)
    min_streamflow_array = np.min(streamflow_array, axis=1)
    mp_lock.acquire()
    seasonal_avg_nc = Dataset(seasonal_average_file, 'a')
    seasonal_avg_nc.variables['average_flow'][:, (day_of_year - 1)
        ] = avg_streamflow_array
    seasonal_avg_nc.variables['std_dev_flow'][:, (day_of_year - 1)
        ] = std_streamflow_array
    seasonal_avg_nc.variables['max_flow'][:, (day_of_year - 1)
        ] = max_streamflow_array
    seasonal_avg_nc.variables['min_flow'][:, (day_of_year - 1)
        ] = min_streamflow_array
    seasonal_avg_nc.close()
    mp_lock.release()