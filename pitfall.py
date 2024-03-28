#!/usr/bin/env python3

from steganalysis import jpg, png
import cryptanalysis.analysis as analysis
import argparse

def greeting():
    intro = """

_____________________________________________________________________________________

░▒▓███████▓▒░░▒▓█▓▒░▒▓████████▓▒░▒▓████████▓▒░▒▓██████▓▒░░▒▓█▓▒░      ░▒▓█▓▒░
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░  ░▒▓█▓▒░   ░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░  ░▒▓█▓▒░   ░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░
░▒▓███████▓▒░░▒▓█▓▒░  ░▒▓█▓▒░   ░▒▓██████▓▒░░▒▓████████▓▒░▒▓█▓▒░      ░▒▓█▓▒░
░▒▓█▓▒░      ░▒▓█▓▒░  ░▒▓█▓▒░   ░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░
░▒▓█▓▒░      ░▒▓█▓▒░  ░▒▓█▓▒░   ░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░
░▒▓█▓▒░      ░▒▓█▓▒░  ░▒▓█▓▒░   ░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░▒▓████████▓▒░▒▓████████▓▒░

-------------------------------------------------------------------------------------
                       A cryptanalysis and steganography tool
-------------------------------------------------------------------------------------
                                     CREDITS:
                       https://www.github.com/Aiclys/pitfall

    """
    print(intro)



if __name__ == "__main__":
    greeting()
    parser = argparse.ArgumentParser(prog="pitfall", description="Steganography and cryptanalysis tool")
    parser.add_argument("-v", "--version", action="version", version="pitfall 0.1.0")
    parser.add_argument("-md", "--mode", action="store", help="cryptanalysis or steganography functions")

    crypt = parser.add_argument_group("cryptanalysis flags")
    crypt.add_argument("-msg", "--message", action="store", nargs="?", help="input file to get frequencies from")
    crypt.add_argument("-lng", "--language", action="store", nargs="?", help="language to output frequencies from")
    crypt.add_argument("-frq", "--frequency", action="store", nargs="?", help="stores which kind of frequency you want to get")
    crypt.add_argument("-out", "--output", action="store", nargs="?", help="type either visual or text")

    steg = parser.add_argument_group("steganography flags")
    steg.add_argument("-tp", "--type", action="store", nargs="?", help="image type: jpg or png")
    steg.add_argument("-pth", "--path", action="store", nargs="?", help="image path")
    steg.add_argument("-op", "--operation", action="store", nargs="?", help="hide, read or execute_from_img operations")

    args = parser.parse_args()

    print(args)
