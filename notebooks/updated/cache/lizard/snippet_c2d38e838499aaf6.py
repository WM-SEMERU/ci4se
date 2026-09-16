def store(self, measurement):
    os.makedirs(self._getPathToMeasurementMetaDir(measurement.idAsPath),
        exist_ok=True)
    output = marshal(measurement, measurementFields)
    with open(self._getPathToMeasurementMetaFile(measurement.idAsPath), 'w'
        ) as outfile:
        json.dump(output, outfile)
    return output