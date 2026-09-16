def update_smag_metadata(col_name):
    smag_units = {'IAGA': 'none', 'N': 'nT', 'E': 'nT', 'Z': 'nT', 'MLT':
        'hours', 'MLAT': 'degrees', 'SZA': 'degrees', 'IGRF_DECL':
        'degrees', 'SMU': 'none', 'SML': 'none', 'datetime':
        'YYYY-MM-DD HH:MM:SS', 'GEOLON': 'degrees', 'GEOLAT': 'degrees',
        'AACGMLON': 'degrees', 'AACGMLAT': 'degrees', 'STATION_NAME':
        'none', 'OPERATOR_NUM': 'none', 'OPERATORS': 'none'}
    smag_name = {'IAGA': 'Station Code', 'N':
        'B along local magnetic North', 'E': 'B along local magnetic East',
        'Z': 'B vertically downward', 'MLT': 'Magnetic Local Time', 'MLAT':
        'Magnetic Latitude', 'SZA': 'Solar Zenith Angle', 'IGRF_DECL':
        'IGRF magnetic declination', 'SMU':
        """Maximum eastward auroral electrojets strength.
Upper envelope of N-component for stations between 40 and 80 degrees magnetic north."""
        , 'SML':
        """Maximum westward auroral electrojets strength.
Lower envelope of N-component for stations between 40 and 80 degrees magnetic north."""
        , 'datetime': 'UT date and time', 'GEOLON': 'geographic longitude',
        'GEOLAT': 'geographic latitude', 'AACGMLON':
        'Altitude-Adjusted Corrected Geomagnetic longitude', 'AACGMLAT':
        'Altitude-Adjusted Corrected Geomagnetic latitude', 'STATION_NAME':
        'Long form station name', 'OPERATOR_NUM':
        'Number of station operators', 'OPERATORS': 'Station operator name(s)'}
    ackn = 'When using this data please include the following reference:\n'
    ackn += 'Gjerloev, J. W., The SuperMAG data processing technique, '
    ackn += 'Geophys. Res., 117, A09213, doi:10.1029/2012JA017683, 2012\n\n'
    ackn += 'For publications and presentations, please include the following'
    ackn += 'acknowledgement:\nFor the ground magnetometer data we gratefully '
    ackn += 'acknowledge: Intermagnet; USGS, Jeffrey J. Love; CARISMA, PI Ian '
    ackn += 'Mann; CANMOS; The S-RAMP Database, PI K. Yumoto and Dr. K. '
    ackn += 'Shiokawa; The SPIDR database; AARI, PI Oleg Troshichev; The '
    ackn += 'MACCS program, PI M. Engebretson, Geomagnetism Unit of the '
    ackn += 'Geological Survey of Canada; GIMA; MEASURE, UCLA IGPP and Florida'
    ackn += ' Institute of Technology; SAMBA, PI Eftyhia Zesta; 210 Chain, PI '
    ackn += 'K. Yumoto; SAMNET, PI Farideh Honary; The institutes who maintain'
    ackn += (
        ' the IMAGE magnetometer array, PI Eija Tanskanen; PENGUIN; AUTUMN,')
    ackn += (
        ' PI Martin Connors; DTU Space, PI Dr. Rico Behlke; South Pole and ')
    ackn += " McMurdo Magnetometer, PI's Louis J. Lanzarotti and Alan T. "
    ackn += (
        'Weatherwax; ICESTAR; RAPIDMAG; PENGUIn; British Artarctic Survey; ')
    ackn += 'McMac, PI Dr. Peter Chi; BGS, PI Dr. Susan Macmillan; Pushkov '
    ackn += 'Institute of Terrestrial Magnetism, Ionosphere and Radio Wave '
    ackn += 'Propagation (IZMIRAN); GFZ, PI Dr. Juergen Matzka; MFGI, PI B. '
    ackn += 'Heilig; IGFPAS, PI J. Reda; University of L’Aquila, PI M. '
    ackn += 'Vellante; BCMT, V. Lesur and A. Chambodut; Data obtained in '
    ackn += 'cooperation with Geoscience Australia, PI Marina Costelloe; '
    ackn += 'SuperMAG, PI Jesper W. Gjerloev.'
    col_dict = {'units': smag_units[col_name], 'long_name': smag_name[
        col_name], 'acknowledgements': ackn}
    return col_dict