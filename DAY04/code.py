import random

def generate_code(code_len = 6):
    all_chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    last_pos = len(all_chars) - 1

    code = ''
    for _ in range(0, code_len):
        pos = random.randint(0, last_pos)
        code += all_chars[pos]
    return code

if __name__ == '__main__':
    print(generate_code())