def load_robot_execution_failures(multiclass=False):
    if not os.path.exists(data_file_name):
        raise RuntimeError(UCI_MLD_REF_MSG)
    id_to_target = {}
    df_rows = []
    with open(data_file_name) as f:
        cur_id = 0
        time = 0
        for line in f.readlines():
            if line[0] not in ['\t', '\n']:
                cur_id += 1
                time = 0
                if multiclass:
                    id_to_target[cur_id] = line.strip()
                else:
                    id_to_target[cur_id] = line.strip() == 'normal'
            elif line[0] == '\t':
                values = list(map(int, line.split('\t')[1:]))
                df_rows.append([cur_id, time] + values)
                time += 1
    df = pd.DataFrame(df_rows, columns=['id', 'time', 'F_x', 'F_y', 'F_z',
        'T_x', 'T_y', 'T_z'])
    y = pd.Series(id_to_target)
    return df, y