import base64


def hex_to_base64(input):
    b = bytes.fromhex(input)
    result = base64.b64encode(b)
    return result

