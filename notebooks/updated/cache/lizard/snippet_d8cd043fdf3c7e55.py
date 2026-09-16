def set_render_manager(self, agent: BaseAgent):
    rendering_manager = self.game_interface.renderer.get_rendering_manager(self
        .index, self.team)
    agent._set_renderer(rendering_manager)