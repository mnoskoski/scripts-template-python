import shlex, subprocess, sys, os

def executeCommand(args):
    p = subprocess.Popen(args) # Success!
    p = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE ) # nao mostrar o output do comando
    print("Command: ", args)
    
command_line = sys.argv[1]

executeCommand(command_line)



