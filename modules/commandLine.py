import sys
import subprocess

# print('Command Line Arguements:', sys.argv)


completed = subprocess.run(["dir"],
                           shell=True,
                           capture_output=True,
                           text=True
                           )
print(type(completed))

print('args:', completed.args)
print('returncode:', completed.returncode)
print('stderr', completed.stderr)
print('stdout', completed.stdout)


subprocess.run(["python", "-u", "other.py"], shell=True)
