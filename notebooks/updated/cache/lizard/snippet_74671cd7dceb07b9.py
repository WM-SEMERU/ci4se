def get_template_attributes(template_id, **kwargs):
    try:
        attrs_i = db.DBSession.query(Attr).filter(TemplateType.template_id ==
            template_id).filter(TypeAttr.type_id == TemplateType.id).filter(
            Attr.id == TypeAttr.id).all()
        log.debug(attrs_i)
        return attrs_i
    except NoResultFound:
        return None