import sys
import subprocess
import os
import shlex

os.system(f'PYTHONHASHSEED=50 {sys.executable} -m compare50 {" ".join(shlex.quote(arg) for arg in sys.argv[1:])}')
