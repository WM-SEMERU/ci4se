def mri_head_reco_op_32_channel():
    space = odl.uniform_discr(min_pt=[-115.2, -115.2], max_pt=[115.2, 115.2
        ], shape=[256, 256], dtype=complex)
    trafo = odl.trafos.FourierTransform(space)
    return odl.ReductionOperator(odl.ComplexModulus(space) * trafo.inverse, 32)