import subprocess, os

cwd = os.getcwd()

#subprocess.call(['makeotf', '-f', 'Galada.ufo', '-o', 'Galada.otf', '-ff', 'features', '-gf', 'glyphOrder', '-mf', 'menuname', '-r'], cwd=cwd)

print os.split(cwd)
