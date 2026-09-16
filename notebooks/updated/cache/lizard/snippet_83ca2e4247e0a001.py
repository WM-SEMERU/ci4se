def _check_contact(self):
    collision = False
    for contact in self.sim.data.contact[:self.sim.data.ncon]:
        if self.sim.model.geom_id2name(contact.geom1
            ) in self.finger_names or self.sim.model.geom_id2name(contact.geom2
            ) in self.finger_names:
            collision = True
            break
    return collision