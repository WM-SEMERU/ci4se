def didl_metadata(self):
    if not self.can_play:
        message = (
            'This item is not meant to be played and therefore also not to create its own didl_metadata'
            )
        raise DIDLMetadataError(message)
    for key in ['extended_id', 'title', 'item_class']:
        if not hasattr(self, key):
            message = (
                "The property '{}' is not present on this item. This indicates that this item was not meant to create didl_metadata"
                .format(key))
            raise DIDLMetadataError(message)
    if 'description' not in self.content:
        message = (
            "The item for 'description' is not present in self.content. This indicates that this item was not meant to create didl_metadata"
            )
        raise DIDLMetadataError(message)
    item_attrib = {'xmlns:dc': 'http://purl.org/dc/elements/1.1/',
        'xmlns:upnp': 'urn:schemas-upnp-org:metadata-1-0/upnp/', 'xmlns:r':
        'urn:schemas-rinconnetworks-com:metadata-1-0/', 'xmlns':
        'urn:schemas-upnp-org:metadata-1-0/DIDL-Lite/'}
    xml = XML.Element('DIDL-Lite', item_attrib)
    item_attrib = {'parentID': '', 'restricted': 'true', 'id': self.extended_id
        }
    if self.parent_id:
        item_attrib['parentID'] = self.parent_id
    item = XML.SubElement(xml, 'item', item_attrib)
    XML.SubElement(item, 'dc:title').text = self.title
    XML.SubElement(item, 'upnp:class').text = self.item_class
    desc_attrib = {'id': 'cdudn', 'nameSpace':
        'urn:schemas-rinconnetworks-com:metadata-1-0/'}
    desc = XML.SubElement(item, 'desc', desc_attrib)
    desc.text = self.content['description']
    return xml