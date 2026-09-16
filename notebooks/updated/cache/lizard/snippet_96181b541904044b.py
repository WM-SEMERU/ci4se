def e(self, k, n, τ, σ):
    d = self._dichalcogenide
    at, Δ, λ = d.at, d.Δ, d.λ
    sqrt = numpy.sqrt
    α = τ * σ
    return 0.5 * (λ * α + n * sqrt((2 * at * k) ** 2 + (Δ - λ * α) ** 2))