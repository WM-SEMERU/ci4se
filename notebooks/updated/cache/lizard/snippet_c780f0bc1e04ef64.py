def generate_surface_vectors(self, film_millers, substrate_millers):
    vector_sets = []
    for f in film_millers:
        film_slab = SlabGenerator(self.film, f, 20, 15, primitive=False
            ).get_slab()
        film_vectors = reduce_vectors(film_slab.lattice.matrix[0],
            film_slab.lattice.matrix[1])
        for s in substrate_millers:
            substrate_slab = SlabGenerator(self.substrate, s, 20, 15,
                primitive=False).get_slab()
            substrate_vectors = reduce_vectors(substrate_slab.lattice.
                matrix[0], substrate_slab.lattice.matrix[1])
            vector_sets.append((film_vectors, substrate_vectors, f, s))
    return vector_sets