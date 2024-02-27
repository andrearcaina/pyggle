from setuptools import setup, find_packages

with open("../README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name='pyggle',
    version='0.0.1',
    author='Andre Arcaina',
    author_email='dtandre331@gmail.com',
    description='Python-based package that allows you to solve any N x M Boggle board.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/andrearcaina/pyggle',
    py_modules=['boggle'],
    python_requires='>=3.6',
    license='MIT',
    packages=find_packages(),
)
