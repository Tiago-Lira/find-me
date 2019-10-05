

class IPFinder:

    @staticmethod
    def find(request):
        return (
            request.environ.get('HTTP_X_FORWARDED_FOR')
            or request.environ.get('X-Real-IP')
            or request.remote_addr
        )
