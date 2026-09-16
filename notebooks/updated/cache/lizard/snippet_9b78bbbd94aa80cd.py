def alloc_seg(self, net_id):
    segmentation_id = self.service_segs.allocate_segmentation_id(net_id,
        source=fw_const.FW_CONST)
    return segmentation_id