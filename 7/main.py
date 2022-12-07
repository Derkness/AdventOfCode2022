
def handle_input():
    file_structure = {}
    inside_directories = ['/']
    with open("input.txt", "r") as file:
        lines = file.readlines()
        lines = [line.strip() for line in lines]
        index = 0
        while index < len(lines):
            split_line = lines[index].split()
            if '$ cd' in lines[index]:
                target = split_line[2]
                if (target != '..' and target != '/'):
                    inside_directories.append(split_line[2])
                elif (target != '/'):
                    inside_directories.pop()
            elif '$ ls' in lines[index]:
                index+=1
                while lines[index][0] != '$':
                    split_line = lines[index].split()
                    target = split_line[0]
                    if (target.isnumeric()):
                        for key_count in range(len(inside_directories)):
                            directory = '-'.join(inside_directories[:key_count])
                            temp_set = file_structure.get(directory, set())
                            temp_set.add(lines[index])
                            file_structure[directory] = temp_set
                    index+=1
                    if index >= len(lines):
                        break
                index -= 1
            index+=1
    return file_structure

if __name__ == "__main__":
    file_structure = handle_input()
    file_sizes_by_directory = {}
    for key in file_structure:
        file_sizes_by_directory[key] = sum([int(file.split()[0]) for file in file_structure[key]])
        print(key + ':', file_structure[key])
    print('------------')
    print(len(file_structure))
    print('------------') 
    summation = 0
    for key in file_sizes_by_directory:
        if file_sizes_by_directory[key] <= 100000:
            print('---',key+':', file_sizes_by_directory[key])
            summation += file_sizes_by_directory[key]
    print(summation)
    
# above 1263150


# Just turned it into '-' form, somehow now less things are below 100000, which makes no sense bc surely now a LOT will be under 100000 (I get 640221)