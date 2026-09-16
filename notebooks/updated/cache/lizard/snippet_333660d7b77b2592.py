def _reduce_opacity(self, watermark, opacity):
    if watermark.type() != ImageType.TrueColorMatteType:
        watermark.type(ImageType.TrueColorMatteType)
    depth = 255 - int(255 * opacity)
    watermark.quantumOperator(ChannelType.OpacityChannel, QuOp.MaxQuantumOp,
        depth)