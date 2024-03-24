#!/usr/bin/env python3
import PIL.Image
import io
import platform
import os


start_sequence = bytes.fromhex("FFD8FF")
end_sequence = bytes.fromhex("FFD9")




def check_os():
    return platform.system().lower()

def get_bytes_from_jpg(file_to_get_bytes_from, fmt="hex"):
    file_bytes = []
    with open(file_to_get_bytes_from, "rb") as fl:
        fl = fl.read()
        if fmt in ["hex", "hexa", "hexadecimal"] and check_os() != "linux":
            for byte in fl:
                hex_byte = hex(byte)
                pure_hex_byte = hex_byte[2:]
                file_bytes.append(pure_hex_byte)
        elif fmt in ["hex", "hexa", "hexadecimal"] and check_os() == "linux":
            file_bytes = os.system("hexdump -C " + file_to_get_bytes_from)
        elif fmt in ["rgb", "RGB"]:
            for byte in fl:
                file_bytes.append(byte)

        return file_bytes


def hide_text(file_to_hide_in, text_to_hide):
    encoded_text = bytes(text_to_hide, "utf-8")
    with open(file_to_hide_in, "ab") as fl:
        fl.write(encoded_text)

def read_text(file_to_read_from):
    bytes_end = end_sequence
    with open(file_to_read_from, "rb") as fl:
        fl_content = fl.read()
        fl_offset = fl_content.index(bytes_end)
        fl.seek(fl_offset + 2)
        print(fl.read())

def hide_image(file_to_hide_in, file_to_hide, fmt="PNG"):
    image_file = PIL.Image.open(file_to_hide)
    file_bytes = io.BytesIO()
    image_file.save(file_bytes, format=fmt)

    with open(file_to_hide_in, "ab") as fl:
        fl.write(file_bytes.getvalue())

def read_image(file_to_read_from, new_img_name):
    bytes_end = end_sequence
    with open(file_to_read_from, "rb") as fl:
        fl_content = fl.read()
        fl_offset = fl_content.index(bytes_end)

        fl.seek(fl_offset + 2)
        f = fl.read()
        img = PIL.Image.open(io.BytesIO(f))
        img.save(new_img_name)

def hide_exe(file_to_hide_in, executable_file):
    with open(file_to_hide_in, "ab") as fl, open(executable_file, "rb") as exe:
        fl.write(exe.read())

def read_exe(file_to_read_from, new_file_name):
    bytes_end = end_sequence
    with open(file_to_read_from, "rb") as fl:
        fl_content = fl.read()
        fl_offset = fl_content.index(bytes_end)

        fl.seek(fl_offset + 2)
        with open(new_file_name, "wb") as new_exe:
            new_exe.write(fl.read())

def execute_from_img(img_src, exe_name):
    if check_os() == "linux":
        read_exe(img_src, exe_name)
        os.system("chmod +x " + exe_name)
        os.system("./" + exe_name)

