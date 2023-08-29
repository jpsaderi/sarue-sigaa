import sys

args = sys.argv
TYPE_BASE = 'BASE' if len(args) <= 1 else args[1]

MAX_THREADS = 1

TYPES_SEARCH = ['PARALLEL', 'CONCURRENT', 'LINEAR']
TYPES_PERIOD = ['YEAR', 'SEMESTER', 'QUARTER', 'TRIMESTER']
TYPE_SEARCH = TYPES_SEARCH[1] # 0 - PARALLEL, 1 - CONCURRENT. 2 - LINEAR
TYPE_PERIOD = TYPES_PERIOD[3] # 0 - YEAR, 1 - SEMESTER, 2 - QUARTER, 3 - TRIMESTER

TYPES_VISIBILITY = ['VISIBLE', 'INVISIBLE']
TYPE_VISIBILITY = TYPES_VISIBILITY[1] # 0 - VISIBLE, 1 - INVISIBLE

SEARCHS_METHODS = ['ID', 'XPATH', 'CLASS']
SEARCH_METHODS = SEARCHS_METHODS[1] # 0 - ID, 1 - XPATH, 2 - CLASS

SEARCHS_TYPES = ['DIRECTLY', 'TRY_EXCEPT']
SEARCH_TYPES = SEARCHS_TYPES[1] # 0 - DIRECTLY, 1 - TRY_EXCEPT