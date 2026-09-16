def check_cmfcc(cls):
    if gf.can_run_c_extension('cmfcc'):
        gf.print_success('aeneas.cmfcc   AVAILABLE')
        return False
    gf.print_warning('aeneas.cmfcc   NOT AVAILABLE')
    gf.print_info(
        '  You can still run aeneas but it will be significantly slower')
    gf.print_info(
        '  Please refer to the installation documentation for details')
    return True