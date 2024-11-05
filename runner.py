import os, sys, cmd_decomp


def decomp_shader(path):
    if os.path.isdir(path):
        for f in os.scandir(path):
            decomp_shader(f.path)
    else:
        cmd_decomp.force_all(path)


def process_shader(path):
    new_path = path
    if path.endswith((".asm", ".msasm")):
        new_path = os.path.splitext(path)[0] + ".txt"
        os.rename(path, new_path)
        return os.path.abspath(new_path)
    elif path.endswith(".txt"):
        return path


def process_inputs(arg):
    decomp_shader(arg)
    command = ""
    if os.path.isdir(arg):
        for f in os.scandir(arg):
            try:
                if (new_f := process_shader(f.path)).endswith(".txt"):
                    out_f = os.path.splitext(f.path)[0] + ".out"
                    command = f'.\\lua\\lua.exe dxbc_reader.lua "{new_f}" -o "{out_f}"'
                print(command)
                os.system(command)
            except Exception as e:
                pass
    elif os.path.isfile(arg):
        try:
            new_f = process_shader(arg)
            out_f = os.path.splitext(arg)[0] + ".out"
            command = f'.\\lua\\lua.exe dxbc_reader.lua "{new_f}" -o "{out_f}"'
            os.system(command)
        except Exception as e:
            pass


basedir = os.getcwd()
lua_dir = os.path.join(basedir, "lua")
lua_path = os.path.join(lua_dir, "lua.exe")
cmd_decompiler = os.path.join(basedir, "cmd_decompiler.exe")
if len(sys.argv) > 1:
    process_inputs(sys.argv[1])
else:
    process_inputs(input("Enter path to shader file or directory: "))
