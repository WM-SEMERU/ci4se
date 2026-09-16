def fit(self, features, labels, validation_split, epochs=50):
    self.model.fit(x=features, y=labels, epochs=epochs, verbose=1,
        callbacks=[ReduceLROnPlateau(), EarlyStopping(patience=3)],
        validation_split=validation_split, shuffle=True)
    for layer in self.model.layers[:self._NUM_BOTTOM_LAYERS_TO_RETRAIN]:
        layer.trainable = False
    for layer in self.model.layers[self._NUM_BOTTOM_LAYERS_TO_RETRAIN:]:
        layer.trainable = True
    self.model.compile(optimizer='sgd', loss='categorical_crossentropy',
        metrics=['accuracy'])
    self.model.fit(x=features, y=labels, epochs=50, verbose=1, callbacks=[
        ReduceLROnPlateau(), EarlyStopping(patience=3)], validation_split=
        validation_split, shuffle=True)