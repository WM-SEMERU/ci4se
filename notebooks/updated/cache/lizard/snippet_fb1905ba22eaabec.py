def render(self, model, color, num_turtles):
    self.program.bind()
    glBindVertexArray(self.vao)
    self.model_buffer.load(model.data, model.byte_size)
    self.color_buffer.load(color.data, color.byte_size)
    glDrawArraysInstanced(GL_TRIANGLES, 0, len(self.geometry.edges) // 7,
        num_turtles)
    glBindVertexArray(0)
    self.program.unbind()