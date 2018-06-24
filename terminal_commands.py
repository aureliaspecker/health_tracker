import os
import glob
import subprocess

def pwd():
    return os.getcwd()

def ls(pattern="*"):
    return [f for f in glob.glob(pattern)]

def cp(f_orig,f_copy):
    cmd="cp {:} {:}".format(f_orig,f_copy)
    execute_command(cmd)

def mv(f_orig,f_copy):
    cmd="mv {:} {:}".format(f_orig,f_copy)
    execute_command(cmd)

def mkdir(dir):
    cmd="mkdir -p {:}".format(dir)
    execute_command(cmd)

def execute_command(command):
    subprocess.call(command,shell=True)

if __name__=="__main__":
    mkdir("a")