import yaml
from jinja2 import Environment, FileSystemLoader
import os
import sys


def main():
    try:
        # Use current directory instead of __file__
        base = os.getcwd()

        # Check if required files exist
        data_file = os.path.join(base, "data.yml")
        template_file = os.path.join(base, "vhosts.j2")

        if not os.path.exists(data_file):
            print(f"Error: data.yml not found at {data_file}")
            sys.exit(1)

        if not os.path.exists(template_file):
            print(f"Error: vhosts.j2 not found at {template_file}")
            sys.exit(1)

        # Load YAML data
        try:
            with open(data_file, 'r', encoding='utf-8') as f:
                data = yaml.safe_load(f)
        except yaml.YAMLError as e:
            print(f"Error parsing YAML in data.yml: {e}")
            sys.exit(1)
        except Exception as e:
            print(f"Error reading data.yml: {e}")
            sys.exit(1)

        # Validate data structure
        if not data or "vhosts" not in data:
            print("Error: Invalid data structure in data.yml - missing 'vhosts' key")
            sys.exit(1)

        # Load Jinja2 template
        try:
            env = Environment(
                loader=FileSystemLoader(base),
                trim_blocks=True,
                lstrip_blocks=True
            )
            template = env.get_template("vhosts.j2")
        except Exception as e:
            print(f"Error loading template: {e}")
            sys.exit(1)

        # Render template with data
        try:
            result = template.render(vhosts=data["vhosts"])
        except Exception as e:
            print(f"Error rendering template: {e}")
            sys.exit(1)

        # Write output file
        output_file = os.path.join(base, "vhosts.conf")
        try:
            with open(output_file, "w", encoding='utf-8') as f:
                f.write(result)
        except Exception as e:
            print(f"Error writing {output_file}: {e}")
            sys.exit(1)

        print(f"vhosts.conf successfully generated at {output_file}")

    except Exception as e:
        print(f"Unexpected error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
