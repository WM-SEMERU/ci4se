def complex_require_condition():
    print('Demonstrating complex require_condition example')
    val = 64
    Buzz.require_condition(is_even(val), 'This condition should pass')
    val = 81
    Buzz.require_condition(is_even(val), 'Value {val} is not even', val=val)