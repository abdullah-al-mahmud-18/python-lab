import os

cwd = os.getcwd() # current working directory = directory where this script is executed from
print(cwd)

modules_dir = os.path.join(cwd, "modules")

print(modules_dir, type(modules_dir))

os.makedirs(modules_dir, exist_ok=True)

if os.path.isdir(modules_dir):
    print("modules exists")
else:
    print("modules not found")



if os.path.isfile(f"{modules_dir}/os_module.py"):
    print("os_module.py exists")
else:
    print("os_module.py not found")

path_env = os.getenv("PATH")
print(path_env)


os.environ["KEY"] = "12345"

key_env = os.getenv("KEY")
print(key_env)

