# Run TestScript1 in 50% of threads, TestScript2 in 25% of threads,
# and TestScript3 in 25% of threads.
 
from net.grinder.script.Grinder import grinder
import os

def getFiles():
  size=0
  os.chdir("/home/khyati/Grinder311Scripts")
  print os.listdir("/home/khyati/Grinder311Scripts")
  #for files in os.listdir("/home/khyati/Grinder/NewScripts"):
  #  print files
  #  if files.endswith(".py"):
  #  print files
  #  scripts[size]=files
  # size=size+1
  return os.listdir("/home/khyati/Grinder311Scripts")
  
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
    exec("x = %s.TestRunner()" % script)
    return x
 
class TestRunner:
    def __init__(self):
        tid = grinder.threadNumber
 
        if tid % 4 == 2:
            self.testRunner = createTestRunner(scripts[1])
        elif tid % 4 == 3:
            self.testRunner = createTestRunner(scripts[2])
        else:
            self.testRunner = createTestRunner(scripts[0])
 
    # This method is called for every run.
    def __call__(self):
        self.testRunner()
 
