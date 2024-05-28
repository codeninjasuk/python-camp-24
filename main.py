import importlib

taskname = input("Type the Activity Number\n:")

print("Running Activity " + taskname.strip())

try:
  importlib.import_module('activity' + taskname.strip())
except Exception as e:
  print("Error: ", e)

print("Execution Ends Here")
