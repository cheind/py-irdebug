

from setuptools import setup

with open("irdebug/version.py") as f: 
    exec(f.read())


install_requires = [
    'numpy'
]

tests_requires = [
    'pytest'
]

setup(name='irdebug',
      version=__version__,
      description='Utilities for infrared signal debugging',
      url='https://github.com/cheind/py-irdebug',
      author='Christoph Heindl',
      author_email='christoph.heindl@gmail.com',
      license='BSD',
      packages=['irdebug'],
      include_package_data=True,
      zip_safe=False,
      setup_requires=['pytest-runner'],
      tests_require=tests_requires,
      install_requires=install_requires
)
