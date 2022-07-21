from setuptools import setup

version = '0.0.1'

with open("README.md", "r") as fh:
        long_description = fh.read()

setup(
        name="pstl-tools",
        description="Tools for working with instruments/analysis in lab",
        version=version,
        author="tyjoto",
        author_email="tyjoto@gmail.com",
        url="htpps://github.com/tyjoto/pstl-tools",
        packages=['pstl_tools'],
        license="Apache-2.0",
        long_description=long_description,
        install_requires=['pyvisa','pyserial','numpy','scipy','matplotlib'],

        classifiers=[
            'Development Status :: 4 - Beta',
            'Intended Audience :: Science/Research',
            'License :: OSI Approved :: Apache Software License',
            'Natural Language :: English',
            'Operating System :: POSIX',
            'Operating System :: Microsoft :: Windows',
            'Operating System :: MacOS :: MacOS X',
            'Programming Language :: Python',
            'Programming Language :: Python :: 3',
        ],


)
