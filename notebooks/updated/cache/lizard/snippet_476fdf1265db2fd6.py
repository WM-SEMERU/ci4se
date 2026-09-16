def shapeRecords(self):
    return ShapeRecords([ShapeRecord(shape=rec[0], record=rec[1]) for rec in
        zip(self.shapes(), self.records())])