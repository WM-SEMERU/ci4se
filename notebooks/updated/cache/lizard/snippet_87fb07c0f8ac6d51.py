def add_attachment_viewer_widget(self, attachment_property, custom_title=
    False, height=None):
    if isinstance(attachment_property, Property):
        attachment_property_id = attachment_property.id
    elif isinstance(attachment_property, text_type) and is_uuid(
        attachment_property):
        attachment_property_id = attachment_property
        attachment_property = self._client.property(id=attachment_property_id)
    else:
        raise IllegalArgumentError(
            'When using the add_attachment_viewer_widget, attachment_property must be a Property or Property id. Type is: {}'
            .format(type(attachment_property)))
    property_type = attachment_property.type
    if property_type != PropertyType.ATTACHMENT_VALUE:
        raise IllegalArgumentError(
            'When using the add_attachment_viewer_widget, attachment_property must have type {}. Type found: {}'
            .format(PropertyType.ATTACHMENT_VALUE, property_type))
    property_category = attachment_property._json_data['category']
    if property_category != Category.INSTANCE:
        raise IllegalArgumentError(
            'When using the add_attachment_viewer_widget, attachment_property must have category {}. Category found: {}'
            .format(Category.INSTANCE, property_category))
    if custom_title is False:
        show_title_value = 'Default'
        title = attachment_property.name
    elif custom_title is None:
        show_title_value = 'No title'
        title = ''
    else:
        show_title_value = 'Custom title'
        title = str(custom_title)
    config = {'propertyId': attachment_property_id, 'showTitleValue':
        show_title_value, 'xtype': ComponentXType.
        PROPERTYATTACHMENTPREVIEWER, 'title': title, 'filter': {
        'activity_id': str(self.activity.id)}, 'height': height if height else
        500}
    meta = {'propertyInstanceId': attachment_property_id, 'activityId': str
        (self.activity.id), 'customHeight': height if height else 500,
        'showTitleValue': show_title_value, 'customTitle': title}
    self._add_widget(dict(config=config, meta=meta, name=WidgetNames.
        ATTACHMENTVIEWERWIDGET))