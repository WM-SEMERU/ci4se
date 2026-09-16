def get_hypervisor():
    hypervisors = ['kvm', 'xen', 'bhyve']
    result = [hyper for hyper in hypervisors if getattr(sys.modules[
        __name__], '_is_{}_hyper'.format(hyper))()]
    return result[0] if result else None