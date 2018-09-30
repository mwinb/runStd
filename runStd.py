import os
import sys
import platform
import subprocess

def main():
    if len(sys.argv)-1 >= 1:
        try:
            toRun = sys.argv[1]
            raw_input("4: " + something)
            print("\n")
            additionalArgs = "";
            if len(sys.argv) > 2:
                for i in range(2, len(sys.argv)):
                    additionalArgs += " " + sys.argv[i]
                    raw_input("1: " + additionalArgs + "\n")
                    
            run("javac -Xlint:unchecked -cp .:stdlib.jar " + toRun)
            
            toRun = toRun.replace(".java", "")
            toRun = "java -cp .:stdlib.jar " + toRun
            toRun += additionalArgs
            raw_input("2: " + toRun + "\n")
            
            
            run(toRun)
                
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
