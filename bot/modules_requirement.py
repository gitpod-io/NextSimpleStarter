from modulefinder import ModuleFinder
import os
f = ModuleFinder()
# Run the main script
os.chdir(os.path.dirname(__file__))
f.run_script('bot.py')
# Get names of all the imported modules
names = list(f.modules.keys())
# Get a sorted list of the root modules imported
basemods = sorted(set([name.split('.')[0] for name in names]))
# Print it nicely
print ("\n".join(basemods))