from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup

setup_args = generate_distutils_setup(
    packages = ['pyaudio_analysis','data'],
    scripts = ['pyaudio_analysis/audioAnalysis.py'],
#    cmdclass={'build_py': build_py},
#    package_dir={'': 'src'},
    long_description=open('README.md').read(),
)

setup(**setup_args)
