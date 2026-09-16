def write_ply(self, output_file):
    points = np.hstack([self.coordinates, self.colors])
    with open(output_file, 'w') as outfile:
        outfile.write(self.ply_header.format(vertex_count=len(self.
            coordinates)))
        np.savetxt(outfile, points, '%f %f %f %d %d %d')