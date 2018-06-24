import os
import glob
import subprocess

def pwd():
    return os.getcwd()

def ls(pattern="*"):
    return [f for f in glob.glob(pattern)]

if __name__=="__main__":
    a=ls("*.md")
    print a