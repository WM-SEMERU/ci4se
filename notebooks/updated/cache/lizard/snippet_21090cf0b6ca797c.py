def run_r_script(r_script_filename, cwd='.'):
    p = subprocess.Popen(['R', 'CMD', 'BATCH', r_script_filename], cwd=cwd)
    while True:
        time.sleep(0.3)
        errcode = p.poll()
        if errcode != None:
            break
    rout = '{0}out'.format(r_script_filename)
    rout_contents = None
    if os.path.exists(rout):
        rout_contents = read_file(rout)
        os.remove(rout)
    rdata_file = os.path.join(os.path.split(r_script_filename)[0], '.RData')
    if os.path.exists(rdata_file):
        os.remove(rdata_file)
    if errcode != 0:
        print(rout_contents)
        raise Exception('The R script failed with error code %d.' % errcode)
    return rout_contents