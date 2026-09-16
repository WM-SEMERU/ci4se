def make_assertions(input_pipe, other_pipes, output_pipe):
    assert isinstance(input_pipe, elements.InPypElement
        ), 'Wrong input element type, want a InPypElement!'
    assert isinstance(output_pipe, elements.OutPypElement
        ), 'Wrong output element type, want a OutPypElement!'
    for other_pipe in other_pipes:
        assert isinstance(other_pipe, elements.MidPypElement
            ), 'Wrong middle element type, want a MidPypElement!'