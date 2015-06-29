from urllib.request import urlopen

__author__ = 'ilya'


class Requester(object):

    def __init__(self, host, port=8083):
        self.host = host
        self.port = port

    def get_all_devices(self):
        req_str
        urlopen()

    def _api_request(self, req_type):
        req_str = "http://{}:{}/{}".format(
            self.host,
            self.port,
            req_type
        )
        data = urlopen(req_str)
