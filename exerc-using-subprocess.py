import shlex, subprocess, sys

def executeCommand(args):
    p = subprocess.Popen(args) # Success!
    print("Command: ", args)
    
command_line = sys.argv[1]

executeCommand(command_line)



