import base64


def fixed_xor(input1, input2):
    """
    XOR two equal hex strings.
    """
    b1 = bytes.fromhex(input1)
    b2 = bytes.fromhex(input2)
    result = xor_bytes(b1, b2)
    return result.hex()


def xor_bytes(b1, b2):
    """
    XOR two byte arrays.
    """
    return bytes([_a ^ _b for _a, _b in zip(b1, b2)])
