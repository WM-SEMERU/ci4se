def provider_of(iface):

    def check(value):
        return iface.providedBy(value
            ), '{value!r} does not provide {interface!s}'.format(value=
            value, interface=fullyQualifiedName(iface))
    return check