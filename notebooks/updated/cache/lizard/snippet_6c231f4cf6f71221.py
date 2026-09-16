def add_nodes(self, kind, num, image_id, image_user, flavor, security_group,
    image_userdata='', **extra):
    for i in range(num):
        self.add_node(kind, image_id, image_user, flavor, security_group,
            image_userdata=image_userdata, **extra)