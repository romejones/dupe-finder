# 🧹 dupe-finder

`dupe-finder` is a lightweight, cross-platform command-line tool designed to identify duplicate files—especially images—across folders. It supports CSV reporting and an interactive HTML gallery with thumbnail previews.

Great for photographers, archivists, and digital minimalists.

---

## 🔧 Features

* 🔎 Detects duplicates using content-based hashing (MD5)
* 🗁 Generates thumbnail previews for image files (JPG, PNG)
* 🌐 Interactive HTML gallery with expandable duplicate groups
* 📄 CSV report of all duplicate file paths
* 🗃️ Skip corrupt or unreadable files automatically
* 📂 Supports recursive search across multiple directories
* 💬 Optional `--verbose` flag for CLI output
* 📝 Optionally logs thumbnail errors to a file

---

## 📦 Installation

**1. Clone the repo:**

```bash
git clone https://github.com/romejones/dupe-finder.git
cd dupe-finder
```

**2. Create a virtual environment:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

**3. Install dependencies:**

```bash
pip install -r requirements.txt
```

---

## 🚀 Usage

```bash
python main.py \
  --paths ~/Pictures ~/Downloads \
  --ext .jpg .jpeg .png \
  --html-gallery dupes.html \
  --report report.csv \
  --thumb-log thumb_errors.txt \
  --verbose
```

---

## 🔍 CLI Options

| Option           | Type | Description                                                           |
| ---------------- | ---- | --------------------------------------------------------------------- |
| `--paths`        | List | One or more folders to scan recursively for files                     |
| `--ext`          | List | File extensions to include (e.g., `.jpg`, `.png`)                     |
| `--report`       | Path | (Optional) Path to write CSV report with duplicate groups             |
| `--html-gallery` | Path | (Optional) Path to output HTML gallery of duplicate images            |
| `--thumb-log`    | Path | (Optional) Path to write errors encountered during thumbnail creation |
| `--verbose`      | Flag | (Optional) Show duplicate groups in the terminal                      |

---

## 📁 Output

* **CSV Report**: Lists all duplicate groups with their full paths
* **HTML Gallery**: Expandable list of duplicates with image previews
* **Thumbnail Log**: Lists unreadable, corrupted, or unsupported image files

---

## 📈 Example Output

```text
🔍 Scanning for duplicate files...

📦 Found 8 duplicate groups.

🗁 Generating thumbnails...
Could not create thumbnail for /Users/me/Photos/broken.jpg: cannot identify image file
🌐 Generating HTML report at dupes.html...
✅ Done!
```

---

## 🔐 Notes

* Thumbnails are saved in a hidden `.thumbnails/` directory (auto-created)
* Skips unreadable or 0-byte image files
* Works best with JPEG and PNG files

---

## 🧰 Dependencies

* `Pillow` – for image thumbnailing
* `argparse`, `hashlib`, `os`, `csv` – standard Python libs

---

## 🧠 Ideas for the Future

* File deduplication (auto-delete or symlink mode)
* Duplicate video/audio detection
* Browser-based viewer with filter/search
* Drag-and-drop GUI

---

## 📄 License

MIT License