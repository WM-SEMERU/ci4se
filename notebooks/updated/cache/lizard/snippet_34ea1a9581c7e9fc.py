def or_by_masks(df, masks):
    if len(masks) < 1:
        return df
    if len(masks) == 1:
        return df[masks[0]]
    overall_mask = masks[0] | masks[1]
    for mask in masks[2:]:
        overall_mask = overall_mask | mask
    return df[overall_mask]