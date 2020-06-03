#importing the JWT module
import jwt
#Creating a class name Token
class Token:  
    def encode(payload,key,algorithm):
        """
        Desc:Functions is to encode using jwt
        Params: payload,key,algorithm
        return: encoded 
        """
        encoded = jwt.encode(payload=payload, key=key, algorithm=algorithm).decode('utf-8')
        return encoded
    
    def decode(token,key,algorithm):
        """
        Desc:Functions is to decodes using jwt
        Params: token,key,algorithm
        return: decoded
        """
        decoded= jwt.decode(token,key,algorithms=[algorithm])
        return decoded