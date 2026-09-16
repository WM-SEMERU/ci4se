def create_helper_trans_node(op_name, input_node, node_name):
    node_name = op_name + '_' + node_name
    trans_node = onnx.helper.make_node('Transpose', inputs=[input_node],
        outputs=[node_name], name=node_name)
    return trans_node