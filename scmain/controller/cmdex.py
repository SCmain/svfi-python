# cmdex.py: Command execution module

def ex_EQUAL(instr):
    """
    Execute math assignment statements, e.g., R10 = R11 + R12.
    :param instr: Instruction pointer
    :return: Success or Failure
    """
    print(f"Executing EQUAL operation for instruction: {instr}")
    return 0  # Simulated success

def ex_QUERY(instr):
    """
    Execute QUERY command to send user-generated status or information to host.
    :param instr: Instruction pointer
    :return: Success or Failure
    """
    print(f"Executing QUERY operation for instruction: {instr}")
    return 0  # Simulated success
