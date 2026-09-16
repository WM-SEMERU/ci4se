def DataCopyWithOverlay(self, dcmfilelist, out_dir, overlays):
    dcmlist = dcmfilelist
    for i in range(len(dcmlist)):
        onefile = dcmlist[i]
        logger.info(onefile)
        data = dicom.read_file(onefile)
        for i_overlay in overlays.keys():
            overlay3d = overlays[i_overlay]
            data = self.encode_overlay_slice(data, overlay3d[(-1 - i), :, :
                ], i_overlay)
        head, tail = os.path.split(os.path.normpath(onefile))
        filename_out = os.path.join(out_dir, tail)
        data.save_as(filename_out)