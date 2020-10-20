from build_map import is_valid_map

def encode(map, string):
    # makes sure the map is valid given the rules in 'build_map.py'
    assert is_valid_map(map)
    out = ''
    # maps the char to the new char based on map, if no reference, use old char
    for c in string:
        if c in map:
            out += map[c]
        else:
            out += c
    return out

def decode(map, string):
    # just runs encode with the map flipped
    decode_map = {value: key for key, value in map.items()}
    return encode(decode_map, string)
