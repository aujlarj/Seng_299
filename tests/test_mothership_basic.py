
import unittest
import codecs
import os

from mothership.base import MothershipServer


class TestMothershipBasic(unittest.TestCase):

    def test_connection(self):
	server = MothershipSever()

	self.assertRaises(ConnectionRefusedError, server.run)
