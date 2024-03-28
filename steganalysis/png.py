#!/usr/bin/env python3
import PIL.Image
import io
import os
import numpy as np


start_sequence = b"\x89\x50\x4e\x47\x0d\x0a\x1a\x0a"
end_sequence = b"\x00\x00\x00\x00\x49\x45\x4e\x44\xae\x42\x60\x82"


def check_os():
    return platform.system().lower()

def get_bytes_from_png(file_to_get_bytes_from, fmt="hex"):
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

def hide_text(img_src, text):
    encoded_text = bytes(text, "utf-8")
    with open(img_src, "ab") as fl:
        fl.write(encoded_text)

def read_text(img_src):
    bytes_end = end_sequence
    with open(img_src, "rb") as fl:
        fl_content = fl.read()
        fl_offset = fl_content.index(bytes_end)
        fl.seek(fl_offset + len(bytes_end))
        print(fl.read())

def hide_image(img_to_hide_in, img_to_hide, fmt="PNG"):
    image_file = PIL.Image.open(img_to_hide)
    file_bytes = io.BytesIO()
    image_file.save(file_bytes, format=fmt)

    with open(img_to_hide_in, "ab") as fl:
        fl.write(file_bytes.getvalue())

def read_image(img_src, new_img_name):
    bytes_end = end_sequence
    with open(img_src, "rb") as fl:
        fl_content = fl.read()
        fl_offset = fl_content.index(bytes_end)

        fl.seek(fl_offset + len(bytes_end))
        f = fl.read()
        img = PIL.Image.open(io.BytesIO(f))
        img.save(new_img_name)

def hide_exe(img_src, exe_src):
    with open(img_src, "ab") as fl, open(exe_src, "rb") as exe:
        fl.write(exe.read())

def read_exe(img_src, new_file_name):
    bytes_end = end_sequence
    with open(img_src, "rb") as fl:
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

def lsb_encode(img_src, msg_to_hide, new_img_name, password):
    img = PIL.Image.open(img_src, "r")

    width, height = img.size
    img_array = np.array(list(img.getdata()))
    channel_num = 0
    if img.mode == "RGBA":
        channel_num == 4
    elif img.mode == "RGB":
        channel_num = 3
    else:
        print("Image mode is not supported")
        exit()
    img_pixels = img_array.size // channel_num

    msg_to_hide += password
    msg_in_bits = "".join(f"{ord(i):08b}" for i in msg_to_hide)
    bits_num = len(msg_in_bits)

    if bits_num > img_pixels:
        print("Not enough pixels to encode the message")
    else:
        ind = 0
        for i in range(img_pixels):
            for j in range(0, channel_num):
                if ind < bits_num:
                    img_array[i][j] = int(bin(img_array[i][j])[2:-1] + msg_in_bits[ind], 2)
                    ind += 1

    img_array = img_array.reshape(height, width, channel_num)
    encoded_img = PIL.Image.fromarray(img_array.astype("uint8"), img.mode)
    encoded_img.save(new_img_name)

def lsb_decode(img_src, password):
    img = PIL.Image.open(img_src, "r")
    img_array = np.array(list(img.getdata()))
    if img.mode == "RGBA":
        channel_num == 4
    elif img.mode == "RGB":
        channel_num = 3
    else:
        print("Image mode is not supported")
        exit()
    img_pixels = img_array.size // channel_num

    encoded_bits = [bin(img_array[i][j])[-1] for i in range(img_pixels) for j in range(0, channel_num)]
    encoded_bits = "".join(encoded_bits)
    encoded_bytes = [encoded_bits[i:i+8] for i in range(0, len(encoded_bits), 8)]

    msg = [chr(int(encoded_bytes[i], 2)) for i in range(len(encoded_bytes))]
    msg = "".join(msg)

    if password in msg:
        print(msg[:msg.index(password)])
    else:
        print("Can't find hidden message, wrong password")
