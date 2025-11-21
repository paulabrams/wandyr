import re

INPUT_FILE = "Wandyr v11.16 img .md"
OUTPUT_FILE = "Wandyr v11.16 img .md"

# Mapping from ID to new descriptive name (without 'image_' prefix, we'll add that)
# Based on the filenames we just used
id_to_name = {
    "1": "wandyr_cover",
    "2": "wandyr_title",
    "3": "oracle_intro",
    "4": "character_creation",
    "5": "gameplay",
    "6": "adventure",
    "7": "camping",
    "8": "time",
    "9": "magic",
    "10": "magic_items",
    "11": "spell_lists",
    "12": "monsters",
    "13": "oracle_reference"
}

def replace_ref(match):
    img_id = match.group(1)
    if img_id in id_to_name:
        return f"[image_{id_to_name[img_id]}]"
    return match.group(0)

print(f"Updating references in {INPUT_FILE}...")

try:
    with open(INPUT_FILE, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace [imageX] with [image_name]
    # We use regex to match [imageX] where X is digits
    # We need to be careful not to match something else, but [image\d+] is pretty specific in this context.
    new_content = re.sub(r'\[image(\d+)\]', replace_ref, content)
    
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write(new_content)
        
    print("Done updating references.")

except Exception as e:
    print(f"Error: {e}")
