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