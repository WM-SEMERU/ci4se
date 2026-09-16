def autoprefixCSS(sassPath):
    print('Autoprefixing CSS')
    cssPath = os.path.splitext(sassPath)[0] + '.css'
    command = (
        "postcss --use autoprefixer --autoprefixer.browsers '> 5%' -o" +
        cssPath + ' ' + cssPath)
    subprocess.call(command, shell=True)