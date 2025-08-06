import os
import hashlib
from PIL import Image, UnidentifiedImageError
from collections import defaultdict

def compute_hash(file_path, algo="md5", chunk_size=4096):
    hash_func = hashlib.new(algo)
    try:
        with open(file_path, "rb") as f:
            while chunk := f.read(chunk_size):
                hash_func.update(chunk)
        return hash_func.hexdigest()
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return None

def find_duplicates(paths, extensions=None, algo="md5"):
    hashes = defaultdict(list)

    for root_path in paths:
        for dirpath, _, filenames in os.walk(os.path.expanduser(root_path)):
            for filename in filenames:
                if extensions and not any(filename.lower().endswith(ext.lower()) for ext in extensions):
                    continue
                file_path = os.path.join(dirpath, filename)
                file_hash = compute_hash(file_path, algo=algo)
                if file_hash:
                    hashes[file_hash].append(file_path)

    duplicates = {h: files for h, files in hashes.items() if len(files) > 1}
    return duplicates

def generate_thumbnail(image_path, output_dir, size=(150, 150)):
    try:
        os.makedirs(output_dir, exist_ok=True)
        with Image.open(image_path) as img:
            img.thumbnail(size)
            base_name = os.path.basename(image_path)
            thumb_path = os.path.join(output_dir, f"{hashlib.md5(image_path.encode()).hexdigest()}_{base_name}")
            img.save(thumb_path, "JPEG")
            return thumb_path
    except (UnidentifiedImageError, OSError):
        return None
