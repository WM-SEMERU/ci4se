def insert_attribute(self, att, index):
    javabridge.call(self.jobject, 'insertAttributeAt',
        '(Lweka/core/Attribute;I)V', att.jobject, index)