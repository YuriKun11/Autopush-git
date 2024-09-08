import os
import subprocess

def run_command(command):
    """Run a command in the shell and print the output."""
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    if process.returncode == 0:
        print(stdout.decode())
    else:
        print(stderr.decode())

run_command('git pull origin master')
run_command('git add .')
run_command('git commit -m "Resolved merge conflicts"')
<<<<<<< HEAD
run_command('git push -u origin master')
=======
run_command('git push -u origin master')
>>>>>>> 77d3aaf0a59d17685b2220fa358b26003bb03a77
