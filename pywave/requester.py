import json
from urllib.request import urlopen
from pywave import ALL_DATA

__author__ = 'ilya'


class Requester(object):

    def __init__(self, host, port=8083):
        self.host = host
        self.port = port

    def get_all_devices(self):
        req_str = ALL_DATA
        return self._api_request(req_type=req_str)

    def _api_request(self, req_type):
        req_str = "http://{}:{}/{}".format(
            self.host,
            self.port,
            req_type
        )
        res = urlopen(req_str).read().decode()
        return json.loads(res, "utf-8")
