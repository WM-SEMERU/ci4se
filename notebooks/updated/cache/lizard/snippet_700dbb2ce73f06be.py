def profile(self, frame, event, arg):
    if self.events == None or event in self.events:
        frame_info = inspect.getframeinfo(frame)
        cp = frame_info[0], frame_info[2], frame_info[1]
        if self.codepoint_included(cp):
            objects = muppy.get_objects()
            size = muppy.get_size(objects)
            if cp not in self.memories:
                self.memories[cp] = [0, 0, 0, 0]
                self.memories[cp][0] = 1
                self.memories[cp][1] = size
                self.memories[cp][2] = size
            else:
                self.memories[cp][0] += 1
                if self.memories[cp][1] > size:
                    self.memories[cp][1] = size
                if self.memories[cp][2] < size:
                    self.memories[cp][2] = size