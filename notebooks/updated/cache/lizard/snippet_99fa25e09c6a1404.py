def get_next_item(self):
    try:
        return self.__local_input_q.get(block=False)
    except queue.Empty:
        pass
    return self.input_q.get(block=False)