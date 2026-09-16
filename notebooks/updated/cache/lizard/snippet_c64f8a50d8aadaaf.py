def visitEncapsulatedShape(self, ctx: ShExDocParser.EncapsulatedShapeContext):
    enc_shape = ShexOneOfShapeParser(self.context)
    enc_shape.visit(ctx.innerShape())
    self.expression = enc_shape.expression
    self._card_annotations_and_semacts(ctx)