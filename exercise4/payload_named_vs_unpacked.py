#!/usr/bin/python -tt
# Project: ac3_intro_to_jinja
# Filename: payload_named_vs_unpacked.py
# claudiadeluna
# PyCharm

from __future__ import absolute_import, division, print_function

__author__ = "Claudia de Luna (claudia@indigowire.net)"
__version__ = ": 1.0 $"
__date__ = "11/3/24"
__copyright__ = "Copyright (c) 2025 Claudia"
__license__ = "Python"


import jinja2


def main():
    """
    Short script to illustrate the differences between passing a named variable (data structure or payload) to
    a Jinja2 template vs passing the variable itself and using the default ** (unpacking) behavior.

    While the un-named strategy exposes the keys directly, it is harder to troubleshoot and handle lists.

    :return:
    """

    # Step 0 - Data
    # Template Payload
    payload_dict = {
        "list": [1, 2, 3, 4, 5],
        "maxstack": 9,
        "hostname": "myswitch-01",
        "mydict": {
            "subnet": "192.168.0.0/24",
            "gw": "192.168.0.1",
            "mask": "255.255.255.0",
        },
    }

    print(payload_dict.keys())

    # Step 1 - Define the environment containing the templates you want to use
    # Here all the templates will be in a directory called "templates" relative to the current directory

    env_obj = jinja2.Environment(
        loader=jinja2.FileSystemLoader("templates", encoding="utf-8")
    )

    # Step 2 - Load the specific template to be used
    template_obj_upacked = env_obj.get_template("test_unpacked.j2")

    template_obj_named = env_obj.get_template("test_named.j2")

    # You cannot directly access unnamed positional arguments in standalone Jinja2 templates.
    # payload_list = [-1, 0, 1, 2, 3, 4, 5, 6]
    # rendered_unpacked = template_obj_unpacked.render(payload_list)

    # Step 3 - Render the template with specific payload
    # The unpacked template will need to know the keys
    rendered_unpacked = template_obj_upacked.render(payload_dict)
    print()
    print("=" * 80)
    print("\n----- Passing Un-named and Unpacked variable -----")
    # Access the raw source
    source, filename, uptodate = env_obj.loader.get_source(env_obj, "test_unpacked.j2")
    print(source)  # <--- this is the raw text!
    print("\nRendered Template:")
    print(rendered_unpacked)

    # The named template will just dump whatever is in the named variable cfg
    rendered_named = template_obj_named.render(cfg=payload_dict)
    print()
    print("=" * 80)
    print("\n----- Passing named variable -----")
    # Access the raw source
    source, filename, uptodate = env_obj.loader.get_source(env_obj, "test_named.j2")
    print(source)  # <--- this is the raw text!
    print("\nRendered Template:")
    print(rendered_named)


# Standard call to the main() function.
if __name__ == "__main__":
    main()
