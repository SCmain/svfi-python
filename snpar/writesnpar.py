#!/usr/bin/env python3
"""
 * **************************************************************
 *
 *              Copyright (c) SVFI Automation automation systems
 *
 * Program:     writesnpar
 * File:        writesnpar.py
 * Author :     Georges Sancosme <georges@sancosme.net>
 * Functions:   main
 *
 * Description: This script takes three command line parameters: an integer for glSN and 
 *              a 10-byte string for gucAddr, and writes them to the file passed as parameter.
 * 
 * To write to snpar.par:
 * 
 * Example usage:
 * Command to write data:
 * 
 *     python3 writesnpar.py <filename> <12345> <ABCDEFGHIJ>
 * 
 * - 12345: The value for glSN.
 * - ABCDEFGHIJ: The 10-character ASCII string for gucAddr.
 * 
 * Contents of <filename> after execution:
 * 
 * - The binary value of glSN (e.g., 12345).
 * - The 10 ASCII characters (A through J), each stored as a byte.
 * 
 * Points to note:
 * - Each ASCII character in gucAddr is transformed into its raw value 
 *   (e.g., 'A' becomes 0x41, 'B' becomes 0x42, etc.).
 * - This behavior is useful if you want to write ASCII characters to the file while 
 *   storing them in binary hexadecimal form.
 * 
 * v0.3 Changes made:
 * 
 * - Added a parameter for the file:
 *   The file path is passed as the first argument on the command line.
 * 
 * - Reading and displaying after writing:
 *   The file is reopened after writing to check its contents.
 *   The values of glSN and gucAddr are displayed again, in hexadecimal and ASCII.
 * 
 * - Improved ASCII display:
 *   Non-printable characters are replaced by dots (.).
 * 
 * Example of use:
 * Command to write and display the contents:
 * 
 *     python3 writesnpar.py file.snpar 12345 ABCDEFGHIJ
 * 
 * Output (for example):
 * 
 *     The data has been written to the file 'file.snpar' successfully.
 *     Contents of file 'file.snpar':
 *     glSN: 12345
 *     gucAddr (hex): 41 42 43 44 45 46 47 48 49 4a
 *     gucAddr (ASCII): ABCDEFGHIJ
 * 
 * Points to note:
 * 
 * - This program ensures that written data is immediately verified by reading it back.
 * - The user can specify a custom file path.
 * - The format of the displays makes the output readable and suitable for different types of data.
 * 
 * Environment: Python 3, SUSE LINUX Tumbleweed
 *
 * Modification history:
 *
 * Rev      Date        Brief Description
 * 0.1      20250118    Initial version
 * 0.2      20250118    Added glSN and gucAddr
 * 0.3      20250118    Added parameter for file to output, reading and displaying after writing to check content
 *
 ***************************************************************
"""

import struct
import sys
import os

def main():
    # Vérification des arguments
    if len(sys.argv) != 4:
        print(f"Usage: {sys.argv[0]} <file_path> <glSN> <gucAddr (20 hex characters)>", file=sys.stderr)
        sys.exit(1)

    file_path = sys.argv[1]
    glSN = int(sys.argv[2])  # Conversion de glSN en entier
    gucAddr_hex = sys.argv[3]

    # Validation de gucAddr_hex (10 octets en hexadécimal = 20 caractères)
    if len(gucAddr_hex) != 20:
        print("Error: gucAddr must contain exactly 20 hex characters (10 bytes).", file=sys.stderr)
        sys.exit(1)

    # Conversion de gucAddr_hex en bytes
    try:
        gucAddr = bytes.fromhex(gucAddr_hex)
    except ValueError:
        print("Error: gucAddr contains invalid hexadecimal characters.", file=sys.stderr)
        sys.exit(1)

    # Écriture dans le fichier
    try:
        with open(file_path, "wb") as f:
            # Écriture de glSN (long sur 4 octets en little-endian)
            f.write(struct.pack('<l', glSN))
            # Écriture de gucAddr (10 octets)
            f.write(gucAddr)
        print(f"Data was written to file '{file_path}' successfully.")
    except IOError as e:
        print(f"Error writing to file: {e}", file=sys.stderr)
        sys.exit(1)

    # Lecture et affichage pour vérification
    try:
        with open(file_path, "rb") as f:
            # Lecture de glSN
            glSN_data = f.read(4)
            if len(glSN_data) != 4:
                print("Error reading glSN", file=sys.stderr)
                sys.exit(1)
            read_glSN = struct.unpack('<l', glSN_data)[0]

            # Lecture de gucAddr
            gucAddr_data = f.read(10)
            if len(gucAddr_data) != 10:
                print("Error reading gucAddr", file=sys.stderr)
                sys.exit(1)

        print(f"Contents of file '{file_path}':")
        print(f"glSN: {read_glSN}")

        # Affichage de gucAddr en hexadécimal
        gucAddr_hex = " ".join(f"{byte:02x}" for byte in gucAddr_data)
        print(f"gucAddr (hex): {gucAddr_hex}")

        # Affichage de gucAddr en ASCII
        gucAddr_ascii = "".join(chr(byte) if 32 <= byte <= 126 else '.' for byte in gucAddr_data)
        print(f"gucAddr (ASCII): {gucAddr_ascii}")

    except IOError as e:
        print(f"Error opening/reading file: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
