def _mock_input(self, target, content):
    content = helper.to_str(content)
    for w in content:
        target.send_keys(w)
        rand_block(0.01, 0.01)