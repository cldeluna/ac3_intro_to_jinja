#!/usr/bin/python -tt
# Project: ac3_intro_to_jinja
# Filename: j2_env_loader_examples.py
# claudiadeluna
# PyCharm

from __future__ import absolute_import, division, print_function

__author__ = "Claudia de Luna (claudia@indigowire.net)"
__version__ = ": 1.0 $"
__date__ = "4/26/25"
__copyright__ = "Copyright (c) 2023 Claudia"
__license__ = "Python"

import argparse
import jinja2


# 1. Load from a STRING VARIABLE (no file needed)
def load_from_string_env(template_string):
    env = jinja2.Environment()
    template = env.from_string(template_string)
    return env, template

# 2. Load from a DIRECTORY / FILE SYSTEM
# Requirements: a folder "templates/" containing "simple_template.j2"
def load_from_filesystem_env():
    env = jinja2.Environment(loader=jinja2.FileSystemLoader("./templates"))
    return env

# 3. Load from a PYTHON PACKAGE
# Requirements: a package "app_templates/" with __init__.py and "simple_template.j2" inside
# (The app_templates folder must be installed or on sys.path)
def load_from_package_env():
    env = jinja2.Environment(loader=jinja2.PackageLoader("app_templates", "/"))
    return env

# 4. Load an INDIVIDUAL TEMPLATE from ANY LOCATION
# Requirements: template file located at ./dir1/dir2/simple_template.j2
def load_from_anywhere_env(full_path):
    with open(full_path, "r", encoding="utf-8") as f:
        template_source = f.read()
    env = jinja2.Environment()
    template = env.from_string(template_source)
    return env, template


def main():

    """
    your_project/
    ├── dir1/
    │   └── dir2/
    │       └── simple_template.j2       # For the 'anywhere' loader
    ├── templates/
    │   └── simple_template.j2           # For the FileSystemLoader
    ├── app_templates/
    │   ├── __init__.py                  # Empty file to make it a Python package
    │   └── simple_template.j2           # For the PackageLoader
    ├── your_script.py                   # (the script we generated)

    :return:
    """

    # 1. Load from string
    print("\n--- Loading from STRING ---")
    string_template_content = "Hello {{ name }}!"
    env_string, template_from_string = load_from_string_env(string_template_content)
    print(template_from_string.render(name="World"))
    print("Available templates: (not applicable for string-based templates)")

    # 2. Load from filesystem
    print("\n--- Loading from FILESYSTEM ---")
    env_filesystem = load_from_filesystem_env()
    try:
        templates_fs = env_filesystem.list_templates()
        print("Available templates:", templates_fs)
    except Exception as e:
        print("Cannot list templates:", e)
    template_fs = env_filesystem.get_template("simple_template.j2")
    print(template_fs.render(name="Filesystem"))

    # 3. Load from package
    print("\n--- Loading from PACKAGE ---")
    env_package = load_from_package_env()
    try:
        templates_pkg = env_package.list_templates()
        print("Available templates:", templates_pkg)
    except Exception as e:
        print("Cannot list templates:", e)
    template_pkg = env_package.get_template("simple_template.j2")
    print(template_pkg.render(name="Package"))

    # 4. Load individual template from anywhere
    print("\n--- Loading from INDIVIDUAL FILE PATH ---")
    full_template_path = "./dir1/dir2/simple_template.j2"
    env_anywhere, template_anywhere = load_from_anywhere_env(full_template_path)
    print("Available templates: (not applicable for direct file loading)")
    print(template_anywhere.render(name="Anywhere"))



# Standard call to the main() function.
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Script Description",
                                     epilog="Usage: ' python j2_env_loader_examples.py or uv run j2_env_loader_examples.py' ")
    arguments = parser.parse_args()
    main()
