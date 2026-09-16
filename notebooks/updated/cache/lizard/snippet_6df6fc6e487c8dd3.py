def load(filename):
    file_root, file_ext = os.path.splitext(filename)
    if file_ext.lower() != INTR_EXTENSION:
        raise ValueError(
            'Extension %s not supported for CameraIntrinsics. Must be stored with extension %s'
             % (file_ext, INTR_EXTENSION))
    f = open(filename, 'r')
    ci = json.load(f)
    f.close()
    return CameraIntrinsics(frame=ci['_frame'], fx=ci['_fx'], fy=ci['_fy'],
        cx=ci['_cx'], cy=ci['_cy'], skew=ci['_skew'], height=ci['_height'],
        width=ci['_width'])