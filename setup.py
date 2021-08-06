from setuptools import setup
import setuptools
setup(
    name='topmine',
    version='0.1.0',
    description='topic mining',
    url='https://github.com/WangHexie/topmine',
    author='UNKNOWN',
    author_email='test@test.com',
    license='BSD 2-clause',
    package_dir={"": "topmine"},
    packages=setuptools.find_packages(where="topmine"),
    install_requires=[
                      'numpy',
                      ],

    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',

    ],
)
