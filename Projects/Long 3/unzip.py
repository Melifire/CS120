def unzip(data):
    out = ''
    for item in data:
        # makes sure we have the right item types
        assert type(item) == str or type(item) == tuple
        # if its a string, just add the string
        if type(item) == str:
            assert len(item) == 1
            out += item
        if type(item) == tuple:
            # makes sure tuple is valid, len 2, ints, and positive non 0
            assert len(item) == 2
            assert type(item[0]) == type(item[1]) == int
            assert item[0] > 0 and item[1] > 0
            # used to store a tmp string if the length is greater than the dist
            tmp = ''
            distance, length = item
            assert distance <= len(out)
            # while theres more data that need to be copied than actually exist
            while length >= distance:
                # coppies however many characters there are left untill we run
                # out of distance
                tmp += out[-1*distance:]
                length -= distance
            # adds the string taken from distance from the end to length
            tmp += out[-1*distance:-1*(distance-length)]
            out += tmp
    return out



