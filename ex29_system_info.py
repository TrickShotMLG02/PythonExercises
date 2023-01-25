# Write a function sys_info that gets no arguments but returns the following information as dict:
#
#
# {
#    "cpu_count": number_of_cpus,
#    "cpu_load": (load_for_1min, load_for_5min, load_for_15min),
#    "python_version":{
#       "major": "python_major_version",
#       "minor": "python_minor_version",
#       "micro": "python_micro_version"
#    },
#    "c_api_version": "python_c_interpreter_version"
# }
#
#
# You must use the os and the sys library.

import os, sys

def sys_info():
    data = {}

    data['cpu_count'] = os.cpu_count()
    data['cpu_load'] = os.getloadavg()
    data['python_version'] = {
        'major': sys.version_info.major,
        'minor': sys.version_info.minor,
        'micro': sys.version_info.micro
    }
    data['c_api_version'] = sys.api_version

    return data

def main():
    # Note: This is only for student-side debugging
    print(sys_info())

if __name__ == '__main__':
    main()