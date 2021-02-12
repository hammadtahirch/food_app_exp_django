class EmailService:
    _dependency = 'Hello'

    @staticmethod
    def send_email():
        print("Hello how are you " + EmailService._dependency)
