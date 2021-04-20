import numpy as np

class Table:
    def __init__(self, path):
        self.filename = path
        self.header_index = {}
        self.contents = {}
        self.size = 0
        header = True
        with open(self.filename, 'r') as file:
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
                self.size += 1

    def get_fields(self):
        return [i for i in self.contents]

    def get_column(self, field):
        return self.contents[field]

    def get_latest_entry(self):
        out = {}
        for i in self.contents:
            out[i] = self.contents[i][self.size-1]
        return out
    
    def append_entry(self, data):
        for i in self.contents:
            self.contents[i] = np.append(self.contents[i], data[i])
        self.size += 1

    def save_as_csv(self, path):
        with open(path, 'w') as file:
            out = ''
            for i, val in enumerate(self.contents):
                out += val
                if(i != len(self.contents) - 1):
                    out += ','
                else:
                    out += '\n'
            file.write(out)
            out = ''
            for i in range(0, self.size):
                for j, val in enumerate(self.contents):
                    out += str(self.contents[val][i])
                    if(j != len(self.contents) - 1):
                        out += ','
                    else:
                        out += '\n'
            file.write(out)

    def update_data(self):
        new_data_pool = []
        with open(self.filename) as file:
            for i, line in enumerate(reversed(list(file))):
                line_split = line.split(',')
                if(line_split[0] == 'Date'):
                    break
                if(line_split[0].split(' ')[1] == self.get_latest_entry()['Date']):
                    break
                else:
                    new_data = {}
                    for j, val in enumerate(self.get_fields()):
                        try:
                            temp = float(line_split[j])
                            new_data[val] = temp
                        except:
                            temp = line_split[0].split(' ')[1]
                            new_data[val] = temp
                    new_data_pool.insert(0, new_data)
        for i in new_data_pool:
            print(i['Date'])
            self.append_entry(i)
    