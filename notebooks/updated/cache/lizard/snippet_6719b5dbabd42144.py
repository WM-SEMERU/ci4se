def millis_offset_between_epochs(reference_epoch, target_epoch):
    assert isinstance(reference_epoch, int)
    assert isinstance(target_epoch, int)
    return (target_epoch - reference_epoch) * 1000