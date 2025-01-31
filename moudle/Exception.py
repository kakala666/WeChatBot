class HttpError(Exception):
    """自定义的HTTP错误异常类"""
    def __init__(self, message="HTTP error occurred"):
        super().__init__(message)
        self.message = message