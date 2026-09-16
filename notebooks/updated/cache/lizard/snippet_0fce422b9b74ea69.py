def _read_family(fname, all_cat, template):
    detections = []
    with open(fname, 'r') as f:
        for line in f:
            det_dict = {}
            gen_event = False
            for key_pair in line.rstrip().split(';'):
                key = key_pair.split(': ')[0].strip()
                value = key_pair.split(': ')[-1].strip()
                if key == 'event':
                    if len(all_cat) == 0:
                        gen_event = True
                        continue
                    el = [e for e in all_cat if str(e.resource_id).split(
                        '/')[-1] == value][0]
                    det_dict.update({'event': el})
                elif key == 'detect_time':
                    det_dict.update({'detect_time': UTCDateTime(value)})
                elif key == 'chans':
                    det_dict.update({'chans': ast.literal_eval(value)})
                elif key in ['template_name', 'typeofdet', 'id',
                    'threshold_type']:
                    det_dict.update({key: value})
                elif key == 'no_chans':
                    det_dict.update({key: int(float(value))})
                elif len(key) == 0:
                    continue
                else:
                    det_dict.update({key: float(value)})
            detection = Detection(**det_dict)
            if gen_event:
                detection._calculate_event(template=template)
            detections.append(detection)
    return detections