def build_map(file_location):
    map_dict = {}
    map_file = open(file_location, 'r')
    for line in map_file:
        line = line.strip()
        # checks for blank lines and comments
        if not line or line[0] == '#':
            continue
        split_line = line.split()
        # makes sure 2 elements, doesnt already appear in map, char len 1
        assert len(split_line) == 2
        key, value = split_line
        assert key not in map_dict
        assert len(key) == len(value) == 1
        # adds val to map dictionary
        map_dict[key] = value

    return map_dict
        



def is_valid_map(map):
    # sets used due to their properties of being unordered and unique
    keys = set()
    values = set()
    for key, value in map.items():
        # makes sure strings, len 1, doesnt have ' ' newline or tab, and unique
        if not (type(key) == type(value) == str):
            return False
        if not (len(key) == len(value) == 1):
            return False
        if key in ' \n\t' or value in ' \n\t':
            return False
        if key in keys:
            return False
        keys.add(key)
        values.add(value)
    # makes sure all values are also keys
    return values == keys
        

