INPUT_DIR = "String_Compression.txt"
INPUT_TEST = "Empty.txt"
OUTPUT_DIR = "Arrays.md"


def write_data(file_adress: str, data: str):
    file = open(file_adress, "w")
    file.write(data)
    file.close()


def prepare_data_for_new_file(problem_name, problem_adress, code, test_code):
    data = ""
    data += "# Arrays\n\n"
    data += "+ [" + problem_name + "](#" + problem_adress[30:-1] + ")\n\n"
    data = append_code(data, problem_name, code, test_code, problem_adress)
    return data


def append_code(data, problem_name, code, test_code, problem_adress):
    data += "## " + problem_name + "\n"
    data += problem_adress + "\n"
    data += "<details><summary>Test cases</summary><blockquote>\n\n"
    data += "```python\n"
    for line in test_code:
        data += line
    data += "\n```\n"
    data += "</blockquote></details>\n\n"
    data += "```python\n"
    for line in code:
        data += line
    data += "\n```"
    return data


def last_problem_link_line(file: list):
    plus_flag = False
    for indx, line in enumerate(file):
        if line and not plus_flag and line[0] == "+":
            plus_flag = True
        if line and plus_flag and line[0] != "+":
            return indx - 1
    return -1


def main():
    try:
        arrays = open(OUTPUT_DIR, "r")
    except IOError:
        arrays = open(OUTPUT_DIR, "w")
        arrays = open(OUTPUT_DIR, "r")
    ARRAYS_SOURCE = arrays.read()
    print("----\n" + ARRAYS_SOURCE + "\n----")
    arrays.close()

    new_data = open(INPUT_DIR, "r")
    problem_name = new_data.readline().strip()
    problem_adress = new_data.readline().strip()
    code = new_data.readlines()
    new_data.close()

    test_data = open(INPUT_TEST, "r")
    test_code = test_data.readlines()
    test_data.close()

    if not ARRAYS_SOURCE:
        data = prepare_data_for_new_file(problem_name, problem_adress, code, test_code)
        write_data(OUTPUT_DIR, data)
    else:
        ARRAYS_SOURCE = ARRAYS_SOURCE.split("\n")
        new_link = last_problem_link_line(ARRAYS_SOURCE)

        ARRAYS_SOURCE.insert(new_link, "+ [" + problem_name + "](#" + problem_adress[30:-1] + ")")
        data = ""
        for line in ARRAYS_SOURCE:
            data += line + "\n"
        data += "\n"
        data = append_code(data, problem_name, code, test_code, problem_adress)

        write_data(OUTPUT_DIR, data)


if __name__ == '__main__':
    main()