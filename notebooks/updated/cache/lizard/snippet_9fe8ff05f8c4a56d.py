def scene_interpreter(self, scene):
    anatomy = {'path': None, 'row': None, 'sat': None, 'scene': scene}
    if isinstance(scene, str) and len(scene) == 21:
        anatomy['path'] = scene[3:6]
        anatomy['row'] = scene[6:9]
        anatomy['sat'] = 'L' + scene[2:3]
        return anatomy
    else:
        raise IncorrectSceneId('Received incorrect scene')