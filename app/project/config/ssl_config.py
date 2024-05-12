import os

class SSLConfig:
    def __init__(self):
        self.current_dir = os.path.dirname(os.path.abspath(__file__))
        self.cert_file = os.path.join(self.current_dir, 'cert.pem')
        self.key_file = os.path.join(self.current_dir, 'key.pem')

    def get_ssl_context(self):
        return (self.cert_file, self.key_file)
