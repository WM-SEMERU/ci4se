def _uniform_sample(self):
    ep_ind = random.choice(self.demo_list)
    states = self.demo_file['data/{}/states'.format(ep_ind)].value
    state = random.choice(states)
    if self.need_xml:
        model_xml = self._xml_for_episode_index(ep_ind)
        xml = postprocess_model_xml(model_xml)
        return state, xml
    return state