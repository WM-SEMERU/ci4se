def TowerContext(tower_name, is_training, vs_name=''):
    if is_training:
        return TrainTowerContext(tower_name, vs_name=vs_name)
    else:
        return PredictTowerContext(tower_name, vs_name=vs_name)