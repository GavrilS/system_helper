"""
Command to find all packages with __init__.py files and enable them to be imported!
Usage: pip install -e .
"""
from setuptools import setup, find_packages

setup(name='system_helper', version='1.0', packages=find_packages())
