from flask import request


def get_client_ip_address():
    return (
        request.environ.get('HTTP_X_FORWARDED_FOR')
        or request.environ.get('X-Real-IP')
        or request.remote_addr
    )
