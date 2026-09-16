def main():
    buff = ''
    for line in fileinput.input():
        buff += line
    parser = jbossparser.JbossParser()
    result = parser.parse(buff)
    print(json.dumps(result))