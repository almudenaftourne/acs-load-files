import json
import openai
import time
import os
from openai.embeddings_utils import get_embedding
from dotenv import load_dotenv

# add embeddings extracted from text content and additional fields for the acs index

embedding_model = 'text-embedding-ada-002'
input_json_path = 'sample_json.json' # or your json file generated from the original txt file
output_json_path = 'json_file.json'
unique_id = 1

load_dotenv()
openai.api_key = os.environ["OPENAI_API_KEY"]
openai.api_type = os.environ["OPENAI_API_TYPE"]
openai.api_base = os.environ["OPENAI_API_BASE"]
openai.api_version = os.environ["OPENAI_API_VERSION"]

def apply_embedding(x):
    time.sleep(1)
    return get_embedding(x, engine=embedding_model)

# Load the JSON data from the file 
with open(input_json_path, 'r', encoding='utf-8') as file:
    data = json.load(file)

# Iterate through the JSON items
for item in data:

    # add unique id for each item
    id = str(unique_id)
    item["id"] = id
    unique_id += 1

    # category for filtering - here sample
    item["category"] = "sample_category"

    # extract embeddings and save them in field content_vector
    section_text = item["content"]
    embedding = apply_embedding(section_text)
    item["content_vector"] = embedding

    # add search.action to load docs in acs index
    item["@search.action"] = "upload"

# write JSON data to a file 
with open(output_json_path, 'w', encoding='utf-8') as json_file:
    json.dump(data, json_file, ensure_ascii=False, indent=4)

print("embeddings extraction and storage complete")






