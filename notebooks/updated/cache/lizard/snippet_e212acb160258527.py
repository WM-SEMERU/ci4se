def genH264(infile, outfile, T):
    x264opts = '-x264opts keyint=10:min-keyint=10:bframes=0'
    h264_dummystream_flavor = '-pix_fmt yuv420p -vprofile main'
    opts = ('-vcodec h264 ' + h264_dummystream_flavor + ' ' + x264opts +
        ' -fflags +genpts -r 25 -t ' + str(T))
    com = ('ffmpeg -y -loop 1 -fflags +genpts -r 25 -i ' + infile + ' ' +
        opts + ' ' + outfile)
    print(com)
    os.system(com)