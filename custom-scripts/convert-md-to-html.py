import markdown
from pathlib import Path
import re

# === List of Markdown files to convert ===
md_files = [
    "./docs/classi/Berserker/Istinti del Berserker.md"
    # add more files here...
]

# === Function to normalize nested lists (skip TOC) ===
def normalize_nested_lists(md):
    lines = md.splitlines()
    new_lines = []
    for line in lines:
        if not line.strip():
            new_lines.append(line)
            continue
        line = line.replace("\t", "  ")
        match = re.match(r"^(\s*)-\s", line)
        if match:
            spaces = len(match.group(1))
            spaces = spaces - (spaces % 2)
            line = " " * spaces + "- " + line.lstrip()
        new_lines.append(line)
    return "\n".join(new_lines)

# === Process each Markdown file ===
for md_path_str in md_files:
    md_file = Path(md_path_str)
    html_file = md_file.with_suffix(".html")

    print(f"[INFO] Converting Markdown file: {md_file}")

    if not md_file.exists():
        print(f"[ERROR] Markdown file not found: {md_file}")
        continue

    # Read Markdown
    try:
        with md_file.open("r", encoding="utf-8") as f:
            md_content = f.read()
        print(f"[INFO] Read {len(md_content)} characters from Markdown file")
    except Exception as e:
        print(f"[ERROR] Failed to read file {md_file}: {e}")
        continue

    # === Extract TOC block ===
    toc_match = re.search(r'<!-- TOC START -->(.*?)<!-- TOC END -->', md_content, re.DOTALL)
    if toc_match:
        toc_md = toc_match.group(1).strip()
        md_content_without_toc = md_content[:toc_match.start()] + md_content[toc_match.end():]
        # Convert TOC Markdown to HTML
        toc_html = markdown.markdown(toc_md, extensions=["extra"])
        # Wrap TOC in a collapsible <details>
        toc_html = f'<details class="toc" open><summary>Indice</summary>\n{toc_html}\n</details>'
        print("[INFO] TOC converted to collapsible HTML")
    else:
        toc_html = ""
        md_content_without_toc = md_content
        print("[INFO] No TOC found in this file")

    # Normalize remaining content
    md_content_without_toc = normalize_nested_lists(md_content_without_toc)

    # Convert remaining Markdown to HTML with heading IDs for internal links
    try:
        body_html = markdown.markdown(
            md_content_without_toc,
            extensions=["tables", "fenced_code", "extra", "attr_list", "toc"]
        )
        print("[INFO] Markdown converted to HTML successfully")
    except Exception as e:
        print(f"[ERROR] Failed to convert Markdown to HTML: {e}")
        continue

    # Combine TOC HTML and body HTML
    final_html_content = toc_html + "\n" + body_html

    # Ensure output directory exists
    if not html_file.parent.exists():
        try:
            html_file.parent.mkdir(parents=True)
            print(f"[INFO] Created directory: {html_file.parent}")
        except Exception as e:
            print(f"[ERROR] Failed to create directory: {e}")
            continue

    # HTML template with theme, back-to-top, smooth scrolling, nested list fix
    template = f"""<!doctype html>
<html lang="it">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{md_file.stem} — GDR</title>
<link rel="stylesheet" href="../../styles.css">
</head>
<body>

<header>{md_file.stem}</header>

<!--
<nav>
<a href="../../classi.html">🔙 Indice Classi</a>
<a href="../../index.html">🏠 Home</a>
</nav>
-->

<main>
{final_html_content}
</main>

<footer>© 2025 GDR Docs</footer>
<a id="back-to-top" title="Torna su">↑</a>
<a id="home-button" title="Home">🏠</a>

<script src="../../scripts.js"></script>

</body>
</html>
"""

    # Write HTML
    try:
        with html_file.open("w", encoding="utf-8") as f:
            f.write(template)
        print(f"[SUCCESS] HTML file created: {html_file}")
    except Exception as e:
        print(f"[ERROR] Failed to write HTML file: {e}")
