import re
import os

def camel_to_snake_case(camel_str):
    snake_str = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', camel_str)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', snake_str).lower()

def convert_proto_file(input_file, output_file):
    with open(input_file, 'r') as f:
        lines = f.readlines()

    with open(output_file, 'w') as f:
        for line in lines:
            if '=' in line and not line.startswith('enum'):
                line_parts = line.split('=')
                field_parts = line_parts[0].strip().split()
                field_parts[-1] = camel_to_snake_case(field_parts[-1])
                line_parts[0] = ' '.join(field_parts)
                line = ' ='.join(line_parts)
            f.write(line)

def process_directory(directory):
    for root, dirs, files in os.walk(directory):
     for file in files:
      if file.endswith('.proto'):
                input_file = os.path
