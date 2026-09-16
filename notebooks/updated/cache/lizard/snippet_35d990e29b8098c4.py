def _set_config(c):
    glfw.glfwWindowHint(glfw.GLFW_RED_BITS, c['red_size'])
    glfw.glfwWindowHint(glfw.GLFW_GREEN_BITS, c['green_size'])
    glfw.glfwWindowHint(glfw.GLFW_BLUE_BITS, c['blue_size'])
    glfw.glfwWindowHint(glfw.GLFW_ALPHA_BITS, c['alpha_size'])
    glfw.glfwWindowHint(glfw.GLFW_ACCUM_RED_BITS, 0)
    glfw.glfwWindowHint(glfw.GLFW_ACCUM_GREEN_BITS, 0)
    glfw.glfwWindowHint(glfw.GLFW_ACCUM_BLUE_BITS, 0)
    glfw.glfwWindowHint(glfw.GLFW_ACCUM_ALPHA_BITS, 0)
    glfw.glfwWindowHint(glfw.GLFW_DEPTH_BITS, c['depth_size'])
    glfw.glfwWindowHint(glfw.GLFW_STENCIL_BITS, c['stencil_size'])
    glfw.glfwWindowHint(glfw.GLFW_SAMPLES, c['samples'])
    glfw.glfwWindowHint(glfw.GLFW_STEREO, c['stereo'])
    if not c['double_buffer']:
        raise RuntimeError(
            'GLFW must double buffer, consider using a different backend, or using double buffering'
            )