import os, sys


def asm(arg):
    for f in os.scandir(arg):
        try:
            if f.path.lower().endswith(".cso"):
                command = f'cmd_decompiler.exe -D -d --disassemble-ms -V "{f.path}"'
                os.system(command)
        except Exception as e:
            pass


def force_all(arg):
    try:
        if arg.lower().endswith(".cso"):
            command = f'cmd_decompiler.exe -D -d --disassemble-ms "{arg}"'
            os.system(command)
    except Exception as e:
        pass


def decomp(arg):
    for f in os.scandir(arg):
        try:
            if f.path.lower().endswith(".cso"):
                command = f'.\\cmd_decompiler.exe -D -V "{f.path}"'
                os.system(command)
        except Exception as e:
            pass


def disassemble(arg):
    for f in os.scandir(arg):
        try:
            if f.path.lower().endswith(".cso"):
                command = f'.\\cmd_decompiler.exe -d --disassemble-ms -V "{f.path}"'
                os.system(command)
        except Exception as e:
            pass
