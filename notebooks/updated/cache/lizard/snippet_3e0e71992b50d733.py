def predict_type(self):
    inst_type = self.inst_ref.predict_type()
    if self.prop_ref_type.allowed_inst_type != inst_type:
        self.msg.fatal("'%s' is not a valid property of instance" % self.
            prop_ref_type.get_name(), self.src_ref)
    return self.prop_ref_type