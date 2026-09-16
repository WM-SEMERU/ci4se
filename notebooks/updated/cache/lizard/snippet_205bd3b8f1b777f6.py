def _get_id2obj_high(self, id2obj_user, id_sources, fnc_fill):
    for idid_user in id_sources:
        idobj_user = self.id2obj_all[idid_user]
        fnc_fill(id2obj_user, idobj_user)
        id2obj_user[idobj_user.item_id] = idobj_user
        if idid_user != idobj_user.item_id:
            id2obj_user[idid_user] = idobj_user