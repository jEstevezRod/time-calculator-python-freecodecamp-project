# This entrypoint file to be used in development. Start by reading README.md
from time_calculator import add_time
from unittest import main


# print(add_time("11:06 PM", "122:59"))
# print(add_time("11:55 AM", "3:12"))

# print( add_time("8:16 PM", "466:02"))
# print('expects 12:04 AM (2 days later)')
# print( add_time("8:16 PM", "466:02", "tuesday"))
# print("expects 12:04 AM, Friday (2 days later)")

# Run unit tests automatically
main(module='test_module', exit=False)