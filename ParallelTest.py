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
      names.append(files)
  print names
  return names
  

#scripts = ["TestScript1", "TestScript2", "TestScript3"]

scripts = getFiles()

# Ensure modules are initialised in the process thread.
for script in scripts: 
   if script.endswith(".py"):
    print script
    print os.path.splitext(os.path.basename(script))[0]
    script=os.path.splitext(os.path.basename(script))[0]
    exec("import %s" % script)

 
def createTestRunner(script):
    print "craete Teats Runner "
    print script
    script=script+".py"
    exec("x = %s.TestRunner()" % script)
    return x
 
class TestRunner:
    def __init__(self):
        tid = grinder.threadNumber
        
	for script in scripts:
           self.testRunner = createTestRunner(script)
        
 
    # This method is called for every run.
    def __call__(self):
        self.testRunner()
 
