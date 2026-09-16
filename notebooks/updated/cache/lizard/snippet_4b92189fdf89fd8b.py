def add_required_resources(resources):
    required = [['variation', 'cosmic'], ['variation', 'clinvar'], [
        'variation', 'dbsnp'], ['variation', 'lcr'], ['variation', 'polyx'],
        ['variation', 'encode_blacklist'], ['variation', 'gc_profile'], [
        'variation', 'germline_het_pon'], ['variation', 'train_hapmap'], [
        'variation', 'train_indels'], ['variation', 'editing'], [
        'variation', 'exac'], ['variation', 'esp'], ['variation',
        'gnomad_exome'], ['variation', '1000g'], ['aliases', 'human']]
    for key in required:
        if not tz.get_in(key, resources):
            resources = tz.update_in(resources, key, lambda x: None)
    return resources