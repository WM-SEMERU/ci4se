def get_recipe_object(self, mode_name, pipeline_name='default'):
    active_mode = self.modes[mode_name]
    active_pipeline = self.pipelines[pipeline_name]
    recipe = active_pipeline.get_recipe_object(active_mode)
    return recipe