import argparse
import csv
from find_dupes.scanner import find_duplicates, generate_thumbnail
from find_dupes.html_report import generate_html_report

def main():
    parser = argparse.ArgumentParser(description="Find duplicate files by hash")
    parser.add_argument("--paths", nargs="+", required=True, help="Root paths to scan")
    parser.add_argument("--ext", nargs="*", help="Only include files with these extensions (e.g., .jpg .png)")
    parser.add_argument("--algo", default="md5", help="Hashing algorithm to use (default: md5)")
    parser.add_argument("--report", help="Optional CSV file to save duplicates")
    parser.add_argument("--html-gallery", help="Optional HTML file for image preview report")
    parser.add_argument("--thumb-log", help="Write unreadable image files to a log file")
    parser.add_argument("--verbose", action="store_true", help="Print unreadable image files to terminal")

    args = parser.parse_args()

    print("🔍 Scanning for duplicate files...\n")
    dupes = find_duplicates(args.paths, extensions=args.ext, algo=args.algo)

    if not dupes:
        print("✅ No duplicates found.")
        return

    print(f"📦 Found {len(dupes)} duplicate groups.\n")

    if args.report:
        with open(args.report, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Hash", "File Paths"])
            for h, paths in dupes.items():
                writer.writerow([h] + paths)
        print(f"📝 Report saved to {args.report}")

    if args.html_gallery:
        print("🖼 Generating thumbnails...")
        thumbnail_dir = "./.thumbnails"
        thumb_map = {}
        unreadable = []

        for h, files in dupes.items():
            thumb_map[h] = []
            for f in files:
                thumb = generate_thumbnail(f, thumbnail_dir)
                if thumb:
                    thumb_map[h].append((f, thumb))
                else:
                    unreadable
