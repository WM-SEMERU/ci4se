def _get_instance_key(self, host, namespace, wmi_class, other=None):
    if other:
        return '{host}:{namespace}:{wmi_class}-{other}'.format(host=host,
            namespace=namespace, wmi_class=wmi_class, other=other)
    return '{host}:{namespace}:{wmi_class}'.format(host=host, namespace=
        namespace, wmi_class=wmi_class)