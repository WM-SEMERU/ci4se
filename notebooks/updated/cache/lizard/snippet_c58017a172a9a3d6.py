def hosts_remove(hostsfile='/etc/hosts', entries=None):
    with salt.utils.files.fopen(hostsfile, 'r') as fp_:
        hosts = salt.utils.stringutils.to_unicode(fp_.read())
    host_list = entries.split(',')
    with salt.utils.files.fopen(hostsfile, 'w') as out_file:
        for line in hosts.splitlines():
            if not line or line.strip().startswith('#'):
                out_file.write(salt.utils.stringutils.to_str('{0}\n'.format
                    (line)))
                continue
            comps = line.split()
            for host in host_list:
                if host in comps[1:]:
                    comps.remove(host)
            if len(comps) > 1:
                out_file.write(salt.utils.stringutils.to_str(' '.join(comps)))
                out_file.write(salt.utils.stringutils.to_str('\n'))