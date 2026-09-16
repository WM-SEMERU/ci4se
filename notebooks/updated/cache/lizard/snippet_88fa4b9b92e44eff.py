def get_outbound_entity(entity: BaseEntity, private_key: RsaKey):
    if getattr(entity, 'outbound_doc', None):
        return entity
    outbound = None
    cls = entity.__class__
    if cls in [DiasporaPost, DiasporaImage, DiasporaComment, DiasporaLike,
        DiasporaProfile, DiasporaRetraction, DiasporaContact, DiasporaReshare]:
        outbound = entity
    elif cls == Post:
        outbound = DiasporaPost.from_base(entity)
    elif cls == Comment:
        outbound = DiasporaComment.from_base(entity)
    elif cls == Reaction:
        if entity.reaction == 'like':
            outbound = DiasporaLike.from_base(entity)
    elif cls == Follow:
        outbound = DiasporaContact.from_base(entity)
    elif cls == Profile:
        outbound = DiasporaProfile.from_base(entity)
    elif cls == Retraction:
        outbound = DiasporaRetraction.from_base(entity)
    elif cls == Share:
        outbound = DiasporaReshare.from_base(entity)
    if not outbound:
        raise ValueError(
            "Don't know how to convert this base entity to Diaspora protocol entities."
            )
    if isinstance(outbound, DiasporaRelayableMixin) and not outbound.signature:
        outbound.sign(private_key)
        outbound.parent_signature = outbound.signature
    return outbound