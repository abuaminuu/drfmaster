import sys

# Get the keys (names) of all currently imported modules
imported_modules_names = sys.modules.keys()

# Optionally, convert to a sorted list for easier viewing
sorted_module_list = sorted(list(imported_modules_names))

for module_name in sorted_module_list:
    print(module_name)
