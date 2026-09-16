def generate_exact(self, model, vcpu_num, host_cpu):
    nested = {'Intel': 'vmx', 'AMD': 'svm'}
    cpu = ET.Element('cpu', match='exact')
    ET.SubElement(cpu, 'model').text = model
    cpu.append(self.generate_topology(vcpu_num))
    vendor = host_cpu.findtext('vendor')
    if not nested.get(vendor):
        LOGGER.debug(
            'Unknown vendor: {0}, did not configure nested virtualization cpu flag on guest.'
            .format(vendor))
        return cpu
    model_vendor = LibvirtCPU.get_cpu_vendor(family=model)
    if vendor != model_vendor:
        LOGGER.debug(
            'Not enabling nested virtualization feature, host vendor is: {0}, guest vendor: {1}'
            .format(vendor, model_vendor))
        return cpu
    flag = nested[vendor]
    if host_cpu.find('feature/[@name="{0}"]'.format(flag)) is not None:
        cpu.append(self.generate_feature(name=flag))
    else:
        LOGGER.debug(
            'missing {0} cpu flag on host, nested virtualization will probably not work.'
            .format(flag))
    return cpu