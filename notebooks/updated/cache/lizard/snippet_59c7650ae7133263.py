def add_gt_proposals(self, proposals, targets):
    device = proposals[0].bbox.device
    gt_boxes = [target.copy_with_fields([]) for target in targets]
    for gt_box in gt_boxes:
        gt_box.add_field('objectness', torch.ones(len(gt_box), device=device))
    proposals = [cat_boxlist((proposal, gt_box)) for proposal, gt_box in
        zip(proposals, gt_boxes)]
    return proposals