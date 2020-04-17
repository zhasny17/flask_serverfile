from flask import jsonify


def error_treatment(app):
    @app.errorhandler(ThrowError)
    def error_exception(error):
        return jsonify({'error_description': error.get_message(), 'error': error.get_error_code()}), error.get_status_code()


class ThrowError(Exception):
    def __init__(self, message=None, error_code=None, status_code=None):
        Exception.__init__(self)
        self.message = message
        self.error_code = error_code
        self.status_code = status_code

    def get_message(self):
        return self.message

    def get_status_code(self):
        return self.status_code

    def get_error_code(self):
        return self.error_code


class BadRequestException(ThrowError):
    def __init__(self, message):
        super().__init__(status_code=400, error_code='bad_request', message=message)


class UnauthorizedException(ThrowError):
    def __init__(self, message):
        super().__init__(status_code=401, error_code='unauthorized', message=message)


class ConflictException(ThrowError):
    def __init__(self, message):
        super().__init__(status_code=409, error_code='conflict', message=message)


class NotFoundException(ThrowError):
    def __init__(self, message):
        super().__init__(status_code=404, error_code='not_found', message=message)


class ForbiddenException(ThrowError):
    def __init__(self, message):
        super().__init__(status_code=403, error_code='forbidden', message=message)
