def load_txt_to_sql(tbl_name, src_file_and_path, src_file, op_folder):
    if op_folder == '':
        pth = ''
    else:
        pth = op_folder + os.sep
    fname_create_script = pth + 'CREATE_' + tbl_name + '.SQL'
    fname_backout_file = pth + 'BACKOUT_' + tbl_name + '.SQL'
    fname_control_file = pth + tbl_name + '.CTL'
    cols = read_csv_cols_to_table_cols(src_file)
    create_script_staging_table(fname_create_script, tbl_name, cols)
    create_file(fname_backout_file, 'DROP TABLE ' + tbl_name +
        ' CASCADE CONSTRAINTS;\n')
    create_CTL(fname_control_file, tbl_name, cols, 'TRUNCATE')