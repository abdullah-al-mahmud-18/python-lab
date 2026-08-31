import glob
import os

cwd = os.getcwd()

# all files in current folder
md_files = glob.glob(f"{cwd}/*.md")
print(md_files)

# all files in folder, subfolders
module_files = glob.glob(f"{cwd}/**/*module.py", recursive=True)
print(module_files)
