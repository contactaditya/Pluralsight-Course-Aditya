import subprocess

command = 'dir'
pl = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True).communicate()[0]
print(pl.decode('utf-8'))
