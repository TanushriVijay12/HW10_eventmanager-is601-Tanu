# File: tests/dummy_smtp.py
class DummySMTP:
    def __init__(self, *args, **kwargs):
        self.username = "dummy"
        self.password = "dummy"
        self.file = None
        self.sock = None

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, traceback):
        self.quit()

    def starttls(self, *args, **kwargs):
        # Simulate starting TLS; do nothing.
        return

    def login(self, username, password):
        # Simulate a successful login; return a dummy response tuple.
        return (250, b"OK")

    def sendmail(self, from_addr, to_addr, msg, mail_options=[], rcpt_options=[]):
        # Simulate sending an email successfully.
        # The real sendmail normally returns a dictionary of errors (if any). 
        # Here we'll simply return an empty dictionary to indicate no errors.
        return {}

    def docmd(self, cmd, args=""):
        # Simulate a command execution with a successful reply.
        return (250, b"OK")

    def getreply(self):
        # Return a dummy reply code and message.
        return (250, b"OK")

    def quit(self):
        # Nothing to do for cleanup.
        return
