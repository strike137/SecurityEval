import subprocess

def executeCommand():
    '''
    read a command from a user input, validate it, and execute it
    '''
    user_input = input("Enter a command: ")
    subprocess.call(["application", user_input])