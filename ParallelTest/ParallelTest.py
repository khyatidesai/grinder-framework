# Run TestScript1 in 50% of threads, TestScript2 in 25% of threads,
# and TestScript3 in 25% of threads.

import os
from net.grinder.script.Grinder import grinder


def getFiles():
  os.chdir("")
  names=[]
  print os.listdir("")
  for files in os.listdir(""):
   print files
   if files.endswith(".py"):
    if files != "ParallelTest.py":
      print files
      names.append(os.path.splitext(os.path.basename(files))[0])
  print names
  return names
  

scripts = getFiles()

# Ensure modules are initialised in the process thread.
for script in scripts: exec("import %s" % script)

 
def createTestRunner(script):
    print "Executing %s " % script  
    exec("x = %s.TestRunner()" % script)
    return x
 
class TestRunner:
    def __init__(self):
        tid = grinder.threadNumber
        
	scriptname = scripts[tid % len(scripts)]
	self.testRunner = createTestRunner(scriptname)

 
    # This method is called for every run.
    def __call__(self):
        self.testRunner()

