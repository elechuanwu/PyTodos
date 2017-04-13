# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

entry_points = [
    "add=pytodos.todo:add",
    "list=pytodos.todo:list",
    "got=pytodos.todo:kill"
]

setup(
    name="pytodos",
    version='1.0.8',
    description="a command line lightweight todos tool.",
    long_description="",
    author="chuanwu",
    author_email="chuanwusun@gmail.com",
    packages=["pytodos"],
    url="https://github.com/chuanwu/PyToDos.py",
    entry_points={"console_scripts": entry_points},
    install_requires=[
        "click==6.7"
    ],
)
