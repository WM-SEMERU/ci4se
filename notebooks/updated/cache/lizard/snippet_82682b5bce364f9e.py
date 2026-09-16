def plotCurve(self):
    try:
        attenuations, freqs = self.datafile.get_calibration(str(self.ui.
            calChoiceCmbbx.currentText()), self.calf)
        self.pw = SimplePlotWidget(freqs, attenuations, parent=self)
        self.pw.setWindowFlags(QtCore.Qt.Window)
        self.pw.setLabels('Frequency', 'Attenuation', 'Calibration Curve')
        self.pw.show()
    except IOError:
        QtGui.QMessageBox.warning(self, 'File Read Error',
            'Unable to read calibration file')
    except KeyError:
        QtGui.QMessageBox.warning(self, 'File Data Error',
            'Unable to find data in file')