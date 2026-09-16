def area_faces(self):
    area_faces = triangles.area(crosses=self.triangles_cross, sum=False)
    return area_faces