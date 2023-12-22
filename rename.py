"""Renames all the files as safe filenames"""
import os

def fix_name(fullpath: str) -> str:
    "Fixes a filename"
    path, name = os.path.split(fullpath)
    root, ext = os.path.splitext(name)
    return path + "/" + "".join(
        "-" if char == " " or char == "-" else
        char if char.isalnum() or char == "." else
        "" for char in root
     ) + ext

def recurse(path: str, depth: int = 0) -> None:
    "Recurses down directory paths to fix all their filenames"
    tabs = "\t" * depth
    print(tabs + "Recursing down " + path)
    for scan in os.scandir(path):
        path = scan.path
        if scan.is_dir():
            recurse(path, depth + 1)
            continue
        newpath = fix_name(path)
        print(f"\t{tabs}{path} => {newpath}")
        os.rename(path, newpath)

recurse("./")
