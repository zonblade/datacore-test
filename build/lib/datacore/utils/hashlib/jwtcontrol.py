import jwt


class jwtControl:
    def __init__(self,document:dict={'error':True}):
        self.data = document

    def create(self):
        jwt_result = jwt.encode(self.data,key='dummy-secret',algorithm='ES512')
        return jwt_result