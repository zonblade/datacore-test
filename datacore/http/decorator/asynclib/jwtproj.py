import jwt
from django.http import JsonResponse

def async_jwt():
    def wrapper(view_func):
        async def wrapped(request, *args, **kwargs):
            async def __sync_to_async(data,status_code=200): 
                rs = JsonResponse(data,safe=False,status=status_code)
                return rs
            authorization = None
            origin = None
            try:
                authorization = request.headers['Authorization']
                authorization = jwt.decode(authorization,f'dummy-secret',algorithms=['ES512'])
                request.JWT = authorization
                # return the function
                return await view_func(request, *args, **kwargs)
            except Exception as E:
                return await __sync_to_async({'has_access':False},status_code=401)
        return wrapped
    return wrapper

class asynctable_jwt:
    jwt = async_jwt()