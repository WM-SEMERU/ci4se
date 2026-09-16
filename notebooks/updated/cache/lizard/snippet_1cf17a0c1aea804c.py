def _get_links(network_id, template_id=None):
    extras = {'types': [], 'attributes': []}
    link_qry = db.DBSession.query(Link).filter(Link.network_id ==
        network_id, Link.status == 'A').options(noload('network'))
    if template_id is not None:
        link_qry = link_qry.filter(ResourceType.link_id == Link.id, 
            TemplateType.id == ResourceType.type_id, TemplateType.
            template_id == template_id)
    link_res = db.DBSession.execute(link_qry.statement).fetchall()
    links = []
    for l in link_res:
        links.append(JSONObject(l, extras=extras))
    return links