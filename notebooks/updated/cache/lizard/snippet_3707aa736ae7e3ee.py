def __get_num_preds(self, num_iteration, nrow, predict_type):
    if nrow > MAX_INT32:
        raise LightGBMError(
            """LightGBM cannot perform prediction for datawith number of rows greater than MAX_INT32 (%d).
You can split your data into chunksand then concatenate predictions for them"""
             % MAX_INT32)
    n_preds = ctypes.c_int64(0)
    _safe_call(_LIB.LGBM_BoosterCalcNumPredict(self.handle, ctypes.c_int(
        nrow), ctypes.c_int(predict_type), ctypes.c_int(num_iteration),
        ctypes.byref(n_preds)))
    return n_preds.value