from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup

#try:
#    from distutils.command.build_py import build_py_2to3 as build_py
#except ImportError:
#    from distutils.command.build_py import build_py

setup_args = generate_distutils_setup(
    packages = ['pyaudio_analysis','data'],
    scripts = ['pyaudio_analysis/audioAnalysis.py'],
#    cmdclass={'build_py': build_py},
#    package_dir={'': 'src'},
    long_description=open('README.md').read(),
    install_requires=[
        "hmmlearn",
        "simplejson",
        "eyed3",
        "alsaaudio",
        "audioop"
    ]
)

setup(**setup_args)
