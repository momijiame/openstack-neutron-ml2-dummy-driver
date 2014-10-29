#!/usr/bin/env python
# -*- coding: utf-8 -*-

from neutron.common import exceptions as exc
from neutron.plugins.ml2.driver_api import TypeDriver
from neutron.plugins.ml2 import driver_api as api

from dummyml2.lib.interceptor import interceptor
from dummyml2.lib.interceptor import logging_wrapper


@interceptor(logging_wrapper)
class DummyTypeDriver(TypeDriver):

    def __init__(self):
        self._type = 'dummytype'

    def get_type(self):
        return self._type

    def initialize(self):
        pass

    def is_partial_segment(self, segment):
        return False

    def validate_provider_segment(self, segment):
        for key, value in segment.iteritems():
            if value and key != api.NETWORK_TYPE:
                msg = _("%s prohibited for dummy provider network") % key
                raise exc.InvalidInput(error_message=msg)

    def reserve_provider_segment(self, session, segment):
        return segment

    def allocate_tenant_segment(self, session):
        return {
            api.NETWORK_TYPE: self._type,
        }

    def release_segment(self, session, segment):
        pass
