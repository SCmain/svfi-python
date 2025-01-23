# romain.py: Global definitions for controller firmware

# Axes definitions for first motion control card
RO_AXIS_T = 0x0001
RO_AXIS_R = 0x0002
RO_AXIS_Z = 0x0004
RO_AXIS_W = 0x0008

# Axes definitions for second motion control card
RO_AXIS_t = 0x0010
RO_AXIS_r = 0x0020
RO_AXIS_z = 0x0040
RO_AXIS_w = 0x0080

# Special axes and their custom codes
RO_NO_COMBINED_AXES = 0x100
RO_NO_SPECIAL = 0
RO_TRACK = 1
RO_FLIPPER = 2
RO_DUAL_ARM = 3
RO_TILTER = 4
RO_SINGLE_PRE = 5
RO_INDEXER_T1 = 6  # Typically 't'
RO_INDEXER_T2 = 7  # Typically 'w'
RO_INDEXER_Z1 = 8  # Typically 'r'
RO_INDEXER_Z2 = 9  # Typically 'z'
RO_ROBOT = 10
RO_3_AXIS_PRE = 11

RO_CONFLICT = 0x88
