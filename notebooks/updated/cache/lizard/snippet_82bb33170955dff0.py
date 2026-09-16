def apply_inference_graph(model_path):
    pred_config = PredictConfig(session_init=get_model_loader(model_path),
        model=InferenceOnlyModel(), input_names=['input_img_bytes'],
        output_names=['prediction_img_bytes'])
    pred = OfflinePredictor(pred_config)
    buf = open('lena.png', 'rb').read()
    prediction = pred([buf])[0]
    with open('applied_inference_graph.png', 'wb') as f:
        f.write(prediction[0])