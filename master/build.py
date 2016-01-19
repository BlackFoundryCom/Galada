import subprocess, os

cwd = os.getcwd()

buildPath = os.path.join(os.path.split(cwd)[0], 'build')
fontName = 'Galada.otf'

fontPath = os.path.join(buildPath, fontName)

subprocess.call(['mkdir', buildPath])

subprocess.call(['makeotf', '-f', 'Galada.ufo', '-o', fontPath, '-ff', 'features', '-gf', 'glyphOrder', '-mf', 'menuname', '-r'], cwd=cwd)
