#!/usr/bin/env python3

def get_bytes_from_jpg(file_to_get_bytes_from, fmt="hex"):
    file_bytes = []
    with open(file_to_get_bytes_from, "rb") as fl:
        fl = fl.read()
        if fmt in ["hex", "hexa", "hexadecimal"]:
            for byte in fl:
                hex_byte = hex(byte)
                pure_hex_byte = hex_byte[2:]
                file_bytes.append(pure_hex_byte)
        elif fmt in ["rgb", "RGB"]:
            for byte in fl:
                file_bytes.append(byte)

    return file_bytes

def hide_text(file_to_hide_in, text_to_hide):
    encoded_text = bytes(text_to_hide, "utf-8")
    with open(file_to_hide_in, "ab") as fl:
        fl.write(encoded_text)


print(get_bytes_from_jpg("test.jpeg"))
