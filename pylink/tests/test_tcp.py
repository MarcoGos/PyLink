# -*- coding: utf-8 -*- 
'''
    pylink.tests
    ------------
    
    The pylink test suite.

    :copyright: Copyright 2012 Salem Harrache and contributors, see AUTHORS.
    :license: BSD.

'''
from __future__ import unicode_literals

from ..link import TCPLink

class TestTCPLink:
    
    def setup_class(self):
        """Setup common data."""
        # echo service
        self.link = TCPLink('localhost', 7)

    def test_hello_echo(self):
        """Test echo."""
        self.link.write("hello")
        assert self.link.read(5) == "hello"
#        self.link.write('\x06\xFF', byte=True)
#        assert self.link.read(2, byte=True) == '\x06\xFF'
