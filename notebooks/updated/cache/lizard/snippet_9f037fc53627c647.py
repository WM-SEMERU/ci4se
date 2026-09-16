def DefineStdSpectraForUnits():
    units.Flam.StdSpectrum = FlatSpectrum(1, fluxunits='flam')
    units.Fnu.StdSpectrum = FlatSpectrum(1, fluxunits='fnu')
    units.Photlam.StdSpectrum = FlatSpectrum(1, fluxunits='photlam')
    units.Photnu.StdSpectrum = FlatSpectrum(1, fluxunits='photnu')
    units.Jy.StdSpectrum = FlatSpectrum(1, fluxunits='jy')
    units.mJy.StdSpectrum = FlatSpectrum(1, fluxunits='mjy')
    scale = 1.0 / _default_waveset.size
    units.Counts.StdSpectrum = FlatSpectrum(1, fluxunits='counts') * scale
    units.OBMag.StdSpectrum = FlatSpectrum(1, fluxunits='counts') * scale
    units.ABMag.StdSpectrum = FlatSpectrum(3.63e-20, fluxunits='fnu')
    units.STMag.StdSpectrum = FlatSpectrum(3.63e-09, fluxunits='flam')
    units.VegaMag.StdSpectrum = Vega