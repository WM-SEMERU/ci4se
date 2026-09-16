def get_asn_verbose_dns(self, asn=None):
    if asn[0:2] != 'AS':
        asn = 'AS{0}'.format(asn)
    zone = '{0}.asn.cymru.com'.format(asn)
    try:
        log.debug('ASN verbose query for {0}'.format(zone))
        data = self.dns_resolver.query(zone, 'TXT')
        return str(data[0])
    except (dns.resolver.NXDOMAIN, dns.resolver.NoNameservers, dns.resolver
        .NoAnswer, dns.exception.Timeout) as e:
        raise ASNLookupError('ASN lookup failed (DNS {0}) for {1}.'.format(
            e.__class__.__name__, asn))
    except:
        raise ASNLookupError('ASN lookup failed for {0}.'.format(asn))