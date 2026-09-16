def set_hue(self, hue, duration=0, rapid=False):
    color = self.get_color()
    color2 = hue, color[1], color[2], color[3]
    try:
        if rapid:
            self.fire_and_forget(LightSetColor, {'color': color2,
                'duration': duration}, num_repeats=1)
        else:
            self.req_with_ack(LightSetColor, {'color': color2, 'duration':
                duration})
    except WorkflowException as e:
        raise