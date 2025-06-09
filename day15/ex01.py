"""

随机验证码，验证码由数字何英文大小写字母构成，长度可以通过参数设置

"""

import random
import string
print(string.digits)

ALL_CHARS = string.digits + string.ascii_letters

def generate_code(*, code_len=4): # 入参
    """
    生成指定长度的验证码
    :param code_len: 验证码的长度（默认4个字符）
    :return: 由大小写英文字母何数字构成的随机验证码字符串
    """
    return ''.join(random.choices(ALL_CHARS, k = code_len))

for _ in range(5):
    print(generate_code())