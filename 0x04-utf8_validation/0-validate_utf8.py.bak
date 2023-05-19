#!/usr/bin/python3
"""
0. UTF-8 Validation
"""


def byte_converter(data):
    """
    Returns list of bytes representing data
    """
    bin_data = [f"{byte:b}" for byte in data]
    # print(bin_data)
    byte_list = []
    for byte in bin_data:
        if len(byte) < 8:
            byte_list.append(('0' * (8 - len(byte))) + byte)
        else:
            byte_list.append(byte)
    return byte_list


def validUTF8(data):
    """
    A function that determines if a given data set
    represents a valid UTF-8 encoding.
    """
    if any(item > 255 for item in data):
        return False

    bytes = byte_converter(data)
    appendage = 0

    for byte in bytes:
        if appendage:
            if byte.startswith('10'):
                appendage -= 1
                continue
            else:
                return False

        if byte.startswith('0'):
            continue
        elif byte.startswith('110'):
            appendage = 1
            continue
        elif byte.startswith('1110'):
            appendage = 2
            continue
        elif byte.startswith('11110'):
            appendage = 3
            continue
        else:
            return False

    return True


if __name__ == "__main__":
    data = [229, 65, 127, 256]

    print(byte_converter(data))
