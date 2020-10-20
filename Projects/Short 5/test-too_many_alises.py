#! /usr/bin/python3


import proj05_short



def main():
    print("Checking that too_many_aliases() returns the proper structure")
    L = proj05_short.too_many_aliases()


    if len(L) != 4:
        print(f"ERROR: incorrect list length (expected: 4; got: {len(L)})")

    expected_L0 = [[11,22], [33,44]]
    if L[0] != expected_L0:
        print(f"ERROR: incorrect L[0] value (expected: {expected_L0}; got: {L[0]})")

    expected_L1 = [[11,22], [33,44]]
    if L[1] != expected_L1:
        print(f"ERROR: incorrect L[1] value (expected: {expected_L1}; got: {L[1]})")

    if id(L[0][0]) != id(L[1][0]):
        print(f"ERROR: L[0][0] and L[1][0] refer to different values")

    if id(L[0][1]) != id(L[1][1]):
        print(f"ERROR: L[0][1] and L[1][1] refer to different values")

    if id(L[0]) == id(L[1]):
        print(f"ERROR: L[0] and L[1] refer to the same list object")

    if id(L[0]) != id(L[2]):
        print(f"ERROR: L[0] and L[2] refer to different values")

    if id(L[1]) != id(L[3]):
        print(f"ERROR: L[1] and L[3] refer to different values")

    print()
    print("TESTCASE COMPLETED")



if __name__ == "__main__":
    main()


