def audio_graph(chunksize_bytes=DEFAULT_CHUNK_SIZE, resample_to=SR44100(),
    store_fft=False):
    band = FrequencyBand(20, resample_to.nyquist)


    class AudioGraph(BaseModel):
        meta = JSONFeature(MetaData, store=True, encoder=AudioMetaDataEncoder)
        raw = ByteStreamFeature(ByteStream, chunksize=chunksize_bytes,
            needs=meta, store=False)
        ogg = OggVorbisFeature(OggVorbis, needs=raw, store=True)
        pcm = AudioSamplesFeature(AudioStream, needs=raw, store=False)
        resampled = AudioSamplesFeature(Resampler, needs=pcm, samplerate=
            resample_to, store=False)
        windowed = ArrayWithUnitsFeature(SlidingWindow, needs=resampled,
            wscheme=HalfLapped(), wfunc=OggVorbisWindowingFunc(), store=False)
        dct = ArrayWithUnitsFeature(DCT, needs=windowed, store=True)
        fft = ArrayWithUnitsFeature(FFT, needs=windowed, store=store_fft)
        bark = ArrayWithUnitsFeature(BarkBands, needs=fft, frequency_band=
            band, store=True)
        centroid = ArrayWithUnitsFeature(SpectralCentroid, needs=bark,
            store=True)
        chroma = ArrayWithUnitsFeature(Chroma, needs=fft, frequency_band=
            band, store=True)
        bfcc = ArrayWithUnitsFeature(BFCC, needs=fft, store=True)
    return AudioGraph