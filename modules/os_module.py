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

dirs = os.listdir(cwd) # list everything (files and folders) in given folder
print(dirs)

# walk through all folders, subfolders and files
# for root, dir, files in os.walk(cwd):
#     for file in files:
#         full_path = os.path.join(root, file)
#         print(full_path)

main_file_path = os.path.join(cwd, "main.py")

print(main_file_path)

main_file = os.path.basename(main_file_path)
print(main_file)

main_file_dir_name = os.path.dirname(main_file_path)
print(main_file_dir_name)

print(os.path.splitext(main_file))

print(os.path.abspath(main_file))

