status_code = int(input('响应状态码：'))
match status_code:
    case 400: description = 'bad requst'
    case 401: description = 'unauthorized'
    case 403: description = 'forbidden'
    case 404: description = 'not found'
    case 405: description = 'method not allowed'
    case 418: description = 'I am a teapot'
    case 429: description = 'Too many requests'
    case _: description = 'Unknown status code'
print('状态码描述：',description)