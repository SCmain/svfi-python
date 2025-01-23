#!/usr/bin/env python3
"""
 * ****************************************************************************************
 *              Copyright (c) SVFI Automation automation systems
 *
 * Program:     readsnpar
 * File:        readsnpar.py
 * Author :     Georges Sancosme <georges@sancosme.net>
 * Functions:   main
 *
 * Description: This script reads the values of glSN and gucAddr from 
 *              the binary file snpar.par and displays them.
 *
 *  File passed as argument:
 *      The program expects a file path as a parameter, which allows reading
 *      any file containing data in the expected format.
 *      If the argument is missing, an error is displayed with the correct usage.
 *   
 *  Validation of file opening:
 *      Uses Python's open(file_path, "rb") to open the file passed as parameter.
 *
 *  Display structure:
 *      glSN is displayed as a long integer.
 *      gucAddr is displayed as hexadecimal values (useful for inspecting binary data).
 *
 *  Example of use:
 *      Command to read the file:
 *
 *          python3 readsnpar.py /root/controller/scmain/snpar.par
 *
 *  This program remains compatible with all files containing data in the expected format:
 *      - A long integer followed by 10 bytes.
 *      If the file is malformed or does not contain enough data, appropriate error 
 *      messages will be displayed.
 *
 *  This flexibility makes the program useful for reading different files containing 
 *  structured data.
 *
 *  Printing gucAddr in hexadecimal:
 *      Each byte is printed using Python's string formatting: f"{byte:02x}".
 *
 *  Printing gucAddr in ASCII:
 *      Printable characters are displayed directly.
 *      Non-printable characters (e.g., unreadable bytes) are replaced with a dot (.) 
 *      to avoid erroneous characters in the console.
 *
 *  Output (for example):
 *
 *  If the file contains:
 *
 *      glSN = 12345
 *      gucAddr = "ABCDEFGHIJ"
 *
 *  The output will be:
 *
 *      glSN: 12345
 *      gucAddr (hex): 41 42 43 44 45 46 47 48 49 4a
 *      gucAddr (ASCII): ABCDEFGHIJ
 *
 *  If the file contains non-printable characters in gucAddr:
 *
 *      glSN: 12345
 *      gucAddr (hex): 41 42 43 00 45 46 47 48 49 1a
 *      gucAddr (ASCII): ABC.EFGHI.
 *
 *   This program remains robust for different types of content in gucAddr.
 *   Non-readable characters are represented by dots, making it easier to read binary data.
 *
 * Environment: Python 3, OpenSUSE Tumbleweed i386 (32-bit)
 *
 * Modification history:
 *
 * Rev      Date        Brief Description
 * 0.1      20250118    Initial version
 * 0.2      20250118    Added filename as argument
 * 0.3      20250118    Added output in human-readable format for hex
 *
 * ****************************************************************************************
"""

import struct
import sys
import os

# Fonction principale
def main():
    # Vérification du nombre d'arguments
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <file_path>", file=sys.stderr)
        sys.exit(1)

    file_path = sys.argv[1]

    # Vérification de l'existence du fichier
    if not os.path.isfile(file_path):
        print(f"Error: File '{file_path}' does not exist.", file=sys.stderr)
        sys.exit(1)

    try:
        # Ouverture du fichier en mode binaire
        with open(file_path, "rb") as f:
            # Lecture de glSN (long sur 4 octets, format '<l' pour little-endian long)
            glSN_data = f.read(4)
            if len(glSN_data) != 4:
                print("Error reading glSN", file=sys.stderr)
                sys.exit(1)
            glSN = struct.unpack('<l', glSN_data)[0]

            # Lecture de gucAddr (10 octets)
            gucAddr_data = f.read(10)
            if len(gucAddr_data) != 10:
                print("Error reading gucAddr", file=sys.stderr)
                sys.exit(1)

    except IOError as e:
        print(f"Error opening/reading file: {e}", file=sys.stderr)
        sys.exit(1)

    # Affichage des valeurs
    print(f"glSN: {glSN}")

    # Affichage de gucAddr en hexadécimal
    gucAddr_hex = " ".join(f"{byte:02x}" for byte in gucAddr_data)
    print(f"gucAddr (hex): {gucAddr_hex}")

    # Affichage de gucAddr en ASCII
    gucAddr_ascii = "".join(chr(byte) if 32 <= byte <= 126 else '.' for byte in gucAddr_data)
    print(f"gucAddr (ASCII): {gucAddr_ascii}")

if __name__ == "__main__":
    main()
