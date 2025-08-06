import os
from pathlib import Path

def generate_html_report(dupes, thumbnail_dir, output_file):
    html = []
    html.append("""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <title>Duplicate Files Report</title>
        <style>
            body { font-family: sans-serif; background: #f4f4f4; padding: 20px; }
            .group { margin-bottom: 10px; border: 2px solid #333; background: #fff; }
            .group > summary { padding: 10px; cursor: pointer; font-weight: bold; }
            .entry { display: flex; padding: 10px; border-top: 1px solid #ccc; }
            .path { width: 60%; font-size: 0.9em; word-break: break-all; padding-right: 10px; }
            .thumb { width: 100px; height: auto; border: 1px solid #ccc; }
        </style>
    </head>
    <body>
        <h1>Duplicate Files Report</h1>
    """)

    for i, files in enumerate(dupes.values(), 1):
        html.append(f"<details class='group'><summary>Duplicate Group {i} ({len(files)} files)</summary>")
        for path in files:
            thumb_name = f"{hash(path)}.jpg"
            thumb_path = os.path.join(thumbnail_dir, thumb_name)
            html.append(
                f"<div class='entry'><div class='path'>{path}</div>"
                f"<img class='thumb' src='{thumb_path}' alt='thumbnail'></div>"
            )
        html.append("</details>")

    html.append("</body></html>")

    with open(output_file, "w", encoding="utf-8") as f:
        f.write("\n".join(html))

    print(f"🌐 HTML report generated: {output_file}")
