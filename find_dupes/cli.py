import argparse
import os

def parse_args():
    parser = argparse.ArgumentParser(
        description="Find duplicate files across multiple directories using hash comparison."
    )
    parser.add_argument(
        "--paths",
        nargs="+",
        required=True,
        help="List of directories to scan (e.g. ~/Pictures ~/Downloads)"
    )
    parser.add_argument(
        "--ext",
        nargs="*",
        default=[],
        help="File extensions to include (e.g. .jpg .png .pdf)"
    )
    parser.add_argument(
        "--algo",
        choices=["md5", "sha256"],
        default="sha256",
        help="Hashing algorithm to use (default: sha256)"
    )
    parser.add_argument(
        "--report",
        help="Optional: path to save duplicate report as CSV"
    )
    parser.add_argument(
        "--delete",
        action="store_true",
        help="Delete duplicate files (⚠️ USE WITH CAUTION)"
    )
    return parser.parse_args()

def main():
    args = parse_args()

    print("🔍 Scanning for duplicates...")
    print(f"📂 Directories: {args.paths}")
    print(f"🔎 Extensions: {args.ext if args.ext else 'All'}")
    print(f"🔐 Hash algo: {args.algo}")
    if args.report:
        print(f"📝 Report path: {args.report}")
    if args.delete:
        print("⚠️ Deletion mode enabled")

    # Placeholder for core logic
    # import find_dupes.scanner
    # scanner.find_duplicates(args)
