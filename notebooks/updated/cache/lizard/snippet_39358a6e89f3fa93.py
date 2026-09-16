def calcMassFromMz(mz, charge):
    mass = (mz - maspy.constants.atomicMassProton) * charge
    return mass