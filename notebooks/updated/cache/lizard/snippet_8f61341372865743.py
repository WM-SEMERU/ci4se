def _reinit_daq_daemons(sender, instance, **kwargs):
    if type(instance) is OneWireDevice:
        post_save.send_robust(sender=Device, instance=instance.onewire_device)
    elif type(instance) is OneWireVariable:
        post_save.send_robust(sender=Variable, instance=instance.
            onewire_variable)
    elif type(instance) is ExtendedOneWireVariable:
        post_save.send_robust(sender=Variable, instance=Variable.objects.
            get(pk=instance.pk))
    elif type(instance) is ExtendedOneWireDevice:
        post_save.send_robust(sender=Device, instance=Device.objects.get(pk
            =instance.pk))