def copy_all_lines_from_to(inputFile, outputFile):
    currentLine = inputFile.readline()
    while currentLine:
        outputFile.write(currentLine)
        currentLine = inputFile.readline()