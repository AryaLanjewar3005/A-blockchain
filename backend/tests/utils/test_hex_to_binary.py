from backend.utils.hex_to_binary import hex_to_binary

def test_hex_to_binary():
    original_number = 213
    hex_number = hex(original_number)[2:]
    binary_number = hex_to_binary(hex_number)

    assert int(binary_number, 2) == original_number
