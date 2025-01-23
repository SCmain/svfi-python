# scstat.py: Status utility interface

# Status bits
CMD_NOT_EXED = 0x0001
CMD_INVAL = 0x0002
VACUUM_SEN = 0x0004
VACUUM_SW = 0x0008
MOT_ERROR = 0x0010
LIMIT_SW = 0x0020
HOME_NOT_EXED = 0x0040
ALIGNING = 0x0080
RUNNING_MACRO = 0x0100
RBT_MOVING = 0x0200
SERVO_OFF = 0x0400
COM2_ERR = 0x0800
NVSRAM_ST = 0x2000
CTRL_ERR = 0x4000
COM1_ERR = 0x8000

# Macro status
MACRO_IDLE = 0
MACRO_RUNNING = 1
FROZEN = 2
ABORTED_BY_USER = 3
STACK_OVERFLOW = 4
OTHERS = 5

# System initialization status
MATH_EROR_HANDLER = 0x0001
SYSTEM_TIMER = 0x0002
STATUS_MODULE = 0x0004
COM1_PORT = 0x0008
COM2_PORT = 0x0010
COM3_PORT = 0x0020
IO_MODULE = 0x1000
ALIGNER_MODULE = 0x2000
MACRO_MODULE = 0x8000

# Function stubs
def SSSetStatusWord(mask, flag):
    """Set system status word."""
    print(f"Setting status word with mask={mask}, flag={flag}")

def SSReadStatusBits(mask):
    """Read system status bits."""
    print(f"Reading status bits with mask={mask}")
    return 0  # Simulated value

def SSGetVacuumBits():
    """Get vacuum bits."""
    print("Getting vacuum bits")
    return 0  # Simulated value
