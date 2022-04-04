from __future__ import absolute_import, division, print_function


class ApiResponseBase(object):
    def __init__(self, code, headers):
        self.code = code
        self.headers = headers

class ApiResponse(ApiResponseBase):
    def __init__(self, code, headers, body, interface):
        # super(ApiResponse, self).__init__(code, headers)
        ApiResponseBase.__init__(self, code, headers)
        self.data = interface.apply(body.get('data'))
