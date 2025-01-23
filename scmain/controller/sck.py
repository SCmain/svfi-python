# sck.py: Global definitions and types

# Constants
TRUE = 1
FALSE = 0
ON = 1
OFF = 0
SUCCESS = 0
FAILURE = -1
BLANKLINE = -2
MACRO = -3

CR = 13
LF = 10
CTRL_Z = 26
ESC = 27

# Enums
class ATTRIB:
    NORMAL = 0
    RDONLY = 1
    HIDDEN = 2
    SYSTEM = 4

# Type aliases
INT8 = int
INT16 = int
INT32 = int

UINT8 = int
UINT16 = int
UINT32 = int

BYTE = int
WORD = int
DWORD = int

UCHAR = int
USHORT = int
UINT = int
ULONG = int

BOOL = int
STATUS = int
ARGINT = int
VOID = None

# Device types
DFSAP4 = 1       # Single axis pre-aligner for 4-axis controller
DFVACPRE = 2     # Vacuum prealigner
DFPRE = 4        # Generic pre-aligner
DFAK = 8         # KLA Stage controller
DFSS = 16        # Track servo Axis
DFVAC514 = 32    # VAC514 robot

# Emulator types
DFEMULATORP = 1
DFEMULATORM = 2
DFEMULATORA = 4
DFEMULATORC = 8
DFEMULATORG = 16
DFEMULATORB = 32
