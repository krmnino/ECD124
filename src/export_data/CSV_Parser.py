import numpy as np

class Table:
    def __init__(self, path):
        self.filename = path
        self.header_index = {}
        self.contents = {}
        header = True
        with open(self.filename) as file:
            for line in file:
                if header:
                    header_split = line.split(',')
                    for i, elem in enumerate(header_split):
                        self.header_index[i] = elem.replace('\n', '')
                    header = False
                    continue
                line_split = line.split(',')
                for i, elem in enumerate(line_split):
                    try:
                        convert_elem = float(elem)
                    except:
                        convert_elem = elem
                        pass
                    if self.header_index[i] not in self.contents.keys():
                        self.contents[self.header_index[i]] = np.array([convert_elem])
                    else:
                        self.contents[self.header_index[i]] = np.append(self.contents[self.header_index[i]], convert_elem)

    def get_column(self, field):
        return self.contents[field]
    
    def update_data(self):
        for line in reversed(list(open(self.filename))):
            print(line.rstrip())
    