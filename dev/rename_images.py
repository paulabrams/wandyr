import os

IMAGE_DIR = "../markdown/images"
ABS_IMAGE_DIR = os.path.abspath(os.path.join(os.getcwd(), IMAGE_DIR))

mapping = {
    "image1.png": "wandyr_cover.png",
    "image2.png": "wandyr_title.png",
    "image3.png": "oracle_intro.png",
    "image4.png": "character_creation.png",
    "image5.png": "gameplay.png",
    "image6.jpg": "adventure.jpg",
    "image7.jpg": "camping.jpg",
    "image8.png": "time.png",
    "image9.png": "magic.png",
    "image10.png": "magic_items.png",
    "image11.png": "spell_lists.png",
    "image12.png": "monsters.png",
    "image13.png": "oracle_reference.png"
}

print(f"Renaming images in {ABS_IMAGE_DIR}...")

for old_name, new_name in mapping.items():
    old_path = os.path.join(ABS_IMAGE_DIR, old_name)
    new_path = os.path.join(ABS_IMAGE_DIR, new_name)
    
    try:
        if os.path.exists(old_path):
            os.rename(old_path, new_path)
            print(f"Renamed {old_name} -> {new_name}")
        else:
            print(f"Skipped {old_name} (not found)")
    except Exception as e:
        print(f"Error renaming {old_name}: {e}")

print("Done.")
