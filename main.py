import json
import sys
def del_lasts_comms(text): #удалить все запятые перед }
    for i in range(1, 10):
        text = text.replace(",\n{0}}}".format('\t' * i), "\n{0}}}".format('\t' * i))
    return text

def parse_json(file): #json -> python dict
    buf = open('%s' % file)
    text_file = ""
    for i in buf:
        text_file += i
    text_file = del_lasts_comms(text_file)
    try:
        text_file = json.loads(text_file)
    except json.JSONDecodeError:
        error = {"error" : {"message" : "Входные файлы некорректны"}}
        f = open("error123.json", 'w')
        for line in json.dumps(error, indent = 4, ensure_ascii = False):
            f.write(line)
        f.close()
        sys.exit()
    return text_file


if __name__ == "__main__":
    testcase = parse_json('TestcaseStructure.json')
    values = parse_json('Values.json')

    for i in values['values']:
        for j in testcase['params']:
            if i['id'] == j['id']:
                if 'values' not in j:
                    j['value'] = str(i['value'])
                else:
                    for m in j['values']:
                        if i['value'] == m['id']:
                            j['value'] = m['title']
    f = open('StructureWithValues.json', 'w')
    for line in json.dumps(testcase, indent = 4, ensure_ascii=False):
        f.write(line)
    f.close()
