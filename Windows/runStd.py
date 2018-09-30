
import os
import sys
import platform
import subprocess

def main():
    if len(sys.argv)-1 >= 1:
        try:
            toRun = sys.argv[1]
            run("javac -Xlint:unchecked -cp .;stdlib.jar " + toRun)
            toRun = toRun.replace(".java", "")
            if len(sys.argv) > 2:
                for i in range(2, len(sys.argv)):
                    toRun = toRun + " " + sys.argv[i]
            run("java -cp .;stdlib.jar " + toRun)
                
        except Exception:
            print "----Invalid Command----"
    else:
        print "----Please pass file to open----"
        raise SystemExit
 
def run(cmd):
    try:
        os.system(cmd)
        
    except Exception:
            print "----Invalid Command----"
            raw_input("Continue? (Hit Enter) ")
main()
