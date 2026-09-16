def get_urn(self):
    try:
        type_ctsurn = self.session.get_resource(BASE_URI_TYPES % 'CTS_URN',
            self.session.get_class(surf.ns.ECRM['E55_Type']))
        urn = [CTS_URN(urnstring.rdfs_label.one) for urnstring in self.
            ecrm_P1_is_identified_by if urnstring.uri == surf.ns.ECRM[
            'E42_Identifier'] and urnstring.ecrm_P2_has_type.first ==
            type_ctsurn][0]
        return urn
    except Exception as e:
        return None