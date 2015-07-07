from pywave.requester import Requester

__author__ = 'ilya'
import unittest

class TeestRequester(unittest.TestCase):

    def setUp(self):
        self.requester = Requester("10.8.0.12")

    def test_get_all_devices(self):
        devices = self.requester.get_all_devices()
        print(devices['devices']['2'])