def local_wnd_proc(self, h_wnd, msg, w_param, l_param):
    if msg in self.__msg_dict:
        if self.__msg_dict[msg](w_param, l_param) == False:
            return
    if msg == WM_DESTROY:
        self.unhook_wnd_proc()
    return CallWindowProc(self.__old_wnd_proc, h_wnd, msg, w_param, l_param)