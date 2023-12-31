import json

# define the input and output file paths
input_file_path = 'sample_text.txt' # or your txt file path
output_file_path = 'sample_json.json'

# Read text file and split into paragraphs
with open(input_file_path, 'r', encoding='utf-8') as input_file:
    paragraphs = input_file.read().split('\n\n')   # assuming paragraphs are separated by two newlines

# Create a list of JSON sections
sections = [{"content": paragraph.strip()} for paragraph in paragraphs]

# Write the sections to the output JSON file
with open(output_file_path, 'w', encoding='utf-8') as output_file:
    json.dump(sections, output_file, indent=2, ensure_ascii=False)

print(f'Trasnformed {len(paragraphs)} paragraphs into a JSON file: {output_file_path}')



