from http import HTTPStatus


def bad_request_exception_handler(error):
    return {'code': HTTPStatus.BAD_REQUEST, 'message': str(error)}, HTTPStatus.BAD_REQUEST


def not_found_exception_handler(error):
    return {'code': HTTPStatus.NOT_FOUND, 'message': str(error)}, HTTPStatus.NOT_FOUND