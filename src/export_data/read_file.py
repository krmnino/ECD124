import numpy as np

def parse_file(path):
    header = True
    header_index = {}
    contents = {}
    with open(path) as file:
        for line in file:
            if header:
                header_split = line.split(',')
                for i, elem in enumerate(header_split):
                    header_index[i] = elem
                header = False
                continue
            line_split = line.split(',')
            for i, elem in enumerate(line_split):
                if header_index[i] not in contents.keys():
                    contents[header_index[i]] = np.array([elem])
                else:
                    contents[header_index[i]] = np.append(contents[header_index[i]], elem)
    return contents

parse_file('data/test.csv')