def get_local_serial():
    return [x for x in [subprocess.Popen(
        "system_profiler SPHardwareDataType |grep -v tray |awk '/Serial/ {print $4}'"
        , shell=True, stdout=subprocess.PIPE).communicate()[0].strip()] if x]