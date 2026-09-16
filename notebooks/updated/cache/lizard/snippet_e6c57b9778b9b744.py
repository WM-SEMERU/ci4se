def nss(prediction, fix):
    prediction = prediction - np.mean(prediction)
    prediction = prediction / np.std(prediction)
    return np.mean(prediction[fix[0], fix[1]])