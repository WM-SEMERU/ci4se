def bench_factory():


    class TestSchema(BaseSchema):
        attr_1 = StringNode()
        attr_2 = IntegerNode()

        @property
        def attr_3(self):
            return 'FooBar'

        @staticmethod
        def prepare_attr_1(value):
            return 'Attr#{}'.format(value)

        @staticmethod
        def prepare_attr_2(value):
            return 'Attr#2{}'.format(value)
    return [TestSchema(**obj) for obj in object_loader()]