# Purpose: HTTP Error responses as exceptions
# Source: http://flask.pocoo.org/docs/1.0/patterns/apierrors/


class ClientError(Exception):
    status_code = 400

    def __init__(self, message, status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        response = dict(self.payload or ())
        response['message'] = self.message
        return response


class ServerError(Exception):
    status_code = 500

    def __init__(self, message, status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        response = dict(self.payload or ())
        response['message'] = self.message
        return response
