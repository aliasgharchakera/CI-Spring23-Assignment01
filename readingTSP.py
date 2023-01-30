

def read_tsp(file_path):
    with open(file_path, 'r') as file:
        data = {}
        line = file.readline().strip()
        while line:
            if line.startswith('NAME'):
                data['name'] = line.split(':')[1].strip()
            elif line.startswith('TYPE'):
                data['type'] = line.split(':')[1].strip()
            elif line.startswith('COMMENT'):
                data['comment'] = line.split(':')[1].strip()
            elif line.startswith('DIMENSION'):
                data['dimension'] = int(line.split(':')[1].strip())
            elif line.startswith('EDGE_WEIGHT_TYPE'):
                data['edge_weight_type'] = line.split(':')[1].strip()
            elif line.startswith('NODE_COORD_SECTION'):
                nodes = []
                for i in range(data['dimension']):
                    line = file.readline().strip()
                    node = [float(x) for x in line.split()[1:]]
                    nodes.append(node)
                data['nodes'] = nodes
                return data
            line = file.readline().strip()

file_path = "qa194.tsp"
data = read_tsp(file_path)
print(data)