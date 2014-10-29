#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    import multiprocessing
except ImportError:
    pass

import setuptools


if __name__ == '__main__':
    setuptools.setup(
        setup_requires=['pbr'],
        pbr=True,
    )

