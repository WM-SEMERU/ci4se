def getSkeletalReferenceTransforms(self, action, eTransformSpace,
    eReferencePose, unTransformArrayCount):
    fn = self.function_table.getSkeletalReferenceTransforms
    pTransformArray = VRBoneTransform_t()
    result = fn(action, eTransformSpace, eReferencePose, byref(
        pTransformArray), unTransformArrayCount)
    return result, pTransformArray