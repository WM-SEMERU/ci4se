def add_post_processing(effect, **options):
    from chemlab.graphics.postprocessing import SSAOEffect, OutlineEffect, FXAAEffect, GammaCorrectionEffect
    pp_map = {'ssao': SSAOEffect, 'outline': OutlineEffect, 'fxaa':
        FXAAEffect, 'gamma': GammaCorrectionEffect}
    pp = viewer.add_post_processing(pp_map[effect], **options)
    viewer.update()
    global _counter
    _counter += 1
    str_id = effect + str(_counter)
    _effect_map[str_id] = pp
    return str_id