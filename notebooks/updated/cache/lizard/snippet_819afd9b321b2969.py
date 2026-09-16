def pdb(self):
    if self.embed_disabled:
        self.warning_log(
            'Pdb is disabled when runned from the grid runner because of the multithreading'
            )
        return False
    if BROME_CONFIG['runner']['play_sound_on_pdb']:
        say(BROME_CONFIG['runner']['sound_on_pdb'])
    set_trace()