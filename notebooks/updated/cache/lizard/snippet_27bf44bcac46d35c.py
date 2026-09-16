def switch_to_frame_with_class(self, frame):
    elem = world.browser.find_element_by_class_name(frame)
    world.browser.switch_to.frame(elem)