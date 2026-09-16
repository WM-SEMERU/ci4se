def assert_type_equivalent(o1, o2):
    assert o1 == o2
    assert o2 == o1
    assert type(o1) is type(o2)