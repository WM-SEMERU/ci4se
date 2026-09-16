def check_constraint(self, pkge=None, constr=None):
    if not pkge is None:
        return javabridge.call(self.jobject, 'checkConstraint',
            '(Lweka/core/packageManagement/Package;)Z', pkge.jobject)
    if not constr is None:
        return javabridge.call(self.jobject, 'checkConstraint',
            '(Lweka/core/packageManagement/PackageConstraint;)Z', pkge.jobject)
    raise Exception('Either package or package constraing must be provided!')