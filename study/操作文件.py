def read_file_to_map(filename):
    result_map = {}
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line:
                key, value = line.split('=')
                result_map[key.strip()] = value.strip()
    f.close()
    return result_map




def read_file_to_list(filename):
    result_list = []
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line:
                result_list.append(line.strip())

    f.close()
    return result_list


file_name = './study/a.txt'
print(read_file_to_list(file_name))
