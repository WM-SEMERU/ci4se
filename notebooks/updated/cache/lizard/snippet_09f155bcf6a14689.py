def set_intersection(self, division, intersection):
    IntersectRelationship.objects.filter(from_division=self, to_division=
        division).update(intersection=intersection)