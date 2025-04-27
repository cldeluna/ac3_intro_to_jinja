#!/usr/bin/python -tt
# Project: ac3_intro_to_jinja
# Filename: gen_sw_configs.py
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
import yaml
import os


def main():


    print()
    print("=" * 80)
    print("Generating Switch Configs and Change Request Ticket Summary\n")

    # Step 0 - Load data
    # Load YAML data
    # Payload Data File
    payload_file = 'switches.yml'
    # Build relative path to the payload file in the sample data structures directory
    payload_fp = os.path.join("sample_data_structures", payload_file)
    with open(payload_fp) as f:
        payload = yaml.safe_load(f)

    # Step 1 - Define the environment containing the templates you want to use
    # Here all the templates will be in a directory called "templates" relative to the current directory
    env_obj = jinja2.Environment(
        loader=jinja2.FileSystemLoader("templates", encoding="utf-8")
    )

    # List templates manually by scanning the filesystem
    available_templates = env_obj.loader.list_templates()
    print(f"There are {len(available_templates)} templates available in the FileSystemLoader environment {env_obj.loader.searchpath}:")
    for t in available_templates:
        print(f"\t- {t}")

    # Step 2 - Load the specific template to be used
    template_filename = 'switch_config.j2'
    template = env_obj.get_template(template_filename)

    # Lets put our renderd files in an output directory so things don't get messy
    # Ensure output directory exists
    output_dir = './output_configs'
    os.makedirs(output_dir, exist_ok=True)

    # Step 3 - Render the template with specific payload
    # Iterate through each switch and render individually
    print()
    print("-" * 80)
    for switch_name, switch in payload["switches"].items():
        # Render ONLY this switch
        rendered_output = template.render(payload={"switches": {switch_name: switch}})

        # Write to a file
        output_file = os.path.join(output_dir, f"{switch['hostname']}_config.txt")
        with open(output_file, 'w') as f:
            f.write(rendered_output)
        print(f"Generated config for {switch['hostname']} at {output_file}")

    print(f"\nCompleted generating configs for {len(payload['switches'])} switches.\n")

    print("-" * 80)
    print("Ticket Summary:")
    template = env_obj.get_template('switch_summary.j2')

    output = template.render(payload=payload)
    print(output)

    print("=" * 80)


# Standard call to the main() function.
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Script Description",
                                     epilog="Usage: ' python gen_sw_configs.py' ")

    # parser.add_argument('template', help='Execute all exercises in week 4 assignment')
    # parser.add_argument('-a', '--all', help='Execute all exercises in week 4 assignment', action='store_true',default=False)
    arguments = parser.parse_args()
    main()
