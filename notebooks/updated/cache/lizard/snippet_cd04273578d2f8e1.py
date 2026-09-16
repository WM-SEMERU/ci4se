def DBundle_for_Ntubes_Phadkeb(Ntubes, Do, pitch, Ntp, angle=30):
    r
    if angle == 30 or angle == 60:
        Ns = triangular_Ns[-1]
    elif angle == 45 or angle == 90:
        Ns = square_Ns[-1]
    s = Ns + 1
    r = s ** 0.5
    DBundle_max = (Do + 2.0 * pitch * r) * (1.0 - 1e-08)

    def to_solve(DBundle):
        ans = Ntubes_Phadkeb(DBundle=DBundle, Do=Do, pitch=pitch, Ntp=Ntp,
            angle=angle) - Ntubes
        return ans
    return sp_bisect(to_solve, 0, DBundle_max)