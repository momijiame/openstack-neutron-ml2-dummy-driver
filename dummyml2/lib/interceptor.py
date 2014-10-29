#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import inspect

LOG = logging.getLogger(__name__)


def interceptor(wrapper):
    def _interceptor(cls):
        members = inspect.getmembers(
            cls,
            lambda v: inspect.isfunction(v) or inspect.ismethod(v)
        )
        for name, method in members:
            setattr(cls, name, wrapper(method))

        return cls
    return _interceptor


def logging_wrapper(func):
    def _logging_wrapper(*args, **kwargs):
        fmt = 'CALLED: {name}(*args={args}, **kwargs={kwargs})'
        msg = fmt.format(
            name=func.__name__,
            args=args,
            kwargs=kwargs,
        )
        LOG.info(msg)
        return func(*args, **kwargs)
    return _logging_wrapper
