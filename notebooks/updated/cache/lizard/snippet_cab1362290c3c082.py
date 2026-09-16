def from_eocube(eocube, ji):
    eocubewin = EOCubeChunk(ji, eocube.df_layers, eocube.chunksize, eocube.wdir
        )
    return eocubewin