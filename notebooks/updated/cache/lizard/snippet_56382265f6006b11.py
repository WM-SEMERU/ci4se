def make_checksum_validation_script(stats_list):
    if not os.path.exists('./hash_check'):
        os.mkdir('./hash_check')
    with open('./hash_check/curl.sh', 'w') as curl_f, open(
        './hash_check/md5.txt', 'w') as md5_f, open('./hash_check/sha1.txt',
        'w') as sha1_f:
        curl_f.write('#!/usr/bin/env bash\n\n')
        for stats_dict in stats_list:
            for sysmeta_xml in stats_dict['largest_sysmeta_xml']:
                print(sysmeta_xml)
                sysmeta_pyxb = (d1_common.types.dataoneTypes_v1_2.
                    CreateFromDocument(sysmeta_xml))
                pid = sysmeta_pyxb.identifier.value().encode('utf-8')
                file_name = re.sub('\\W+', '_', pid)
                size = sysmeta_pyxb.size
                base_url = stats_dict['gmn_dict']['base_url']
                if size > 100 * 1024 * 1024:
                    logging.info('Ignored large object. size={} pid={}')
                curl_f.write('# {} {}\n'.format(size, pid))
                curl_f.write('curl -o obj/{} {}/v1/object/{}\n'.format(
                    file_name, base_url, d1_common.url.encodePathElement(pid)))
                if sysmeta_pyxb.checksum.algorithm == 'MD5':
                    md5_f.write('{} obj/{}\n'.format(sysmeta_pyxb.checksum.
                        value(), file_name))
                else:
                    sha1_f.write('{} obj/{}\n'.format(sysmeta_pyxb.checksum
                        .value(), file_name))
    with open('./hash_check/check.sh', 'w') as f:
        f.write('#!/usr/bin/env bash\n\n')
        f.write('mkdir -p obj\n')
        f.write('./curl.sh\n')
        f.write('sha1sum -c sha1.txt\n')
        f.write('md5sum -c md5.txt\n')