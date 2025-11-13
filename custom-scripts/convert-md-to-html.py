import markdown
from pathlib import Path
import re

# === List of Markdown files to convert ===
md_files = [
    "./docs/classi/Console/Console.md"
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
<style>
body {{ margin:0; font-family: system-ui, sans-serif; background:#0b0c10; color:#e0e0e0; padding:0 20px; }}
header {{ background:#111; color:#ffd54a; padding:16px; text-align:center; font-size:22px; font-weight:700; border-bottom:1px solid #333; position: sticky; top:0; z-index:1000; }}
nav {{ display:flex; justify-content:center; gap:12px; flex-wrap:wrap; padding:12px; background:#141414; margin-bottom:20px; position: sticky; top:56px; z-index:999; }}
nav a {{ text-decoration:none; color:#ffd54a; border:1px solid #ffd54a44; padding:6px 12px; border-radius:6px; transition: all .2s; }}
nav a:hover {{ background:#ffd54a; color:#111; }}
main {{ max-width:900px; margin:auto; padding-bottom:40px; }}
h1, h2, h3, h4 {{ color:#ffd54a; }}
table {{ border-collapse: collapse; width:100%; margin-bottom:20px; }}
th, td {{ border:1px solid #ffd54a44; padding:8px; text-align:left; }}
th {{ background:#222; }}
img {{ max-width:100%; height:auto; margin:20px 0; }}
footer {{ text-align:center; font-size:14px; padding:16px; border-top:1px solid #222; margin-top:40px; color:#888; }}
#back-to-top {{ position: fixed; bottom:24px; right:24px; width:44px; height:44px; background:#ffd54a; color:#111; border-radius:50%; text-align:center; line-height:44px; font-size:24px; font-weight:bold; cursor:pointer; z-index:9999; opacity:0; pointer-events:none; transition: opacity .3s; }}
#back-to-top.show {{ opacity:1; pointer-events:auto; }}
#back-to-top:hover {{ opacity:0.8; }}
main a {{ color: #ffd54a; text-decoration:none; transition: color 0.2s ease; }}
main a:hover {{ color: #ffcc00; text-decoration: underline; }}

/* TOC accordion */
.toc {{ background: #111; border:1px solid #333; border-radius:8px; padding:16px; margin:20px 0; }}
.toc summary {{ cursor: pointer; font-weight: bold; font-size:16px; color:#ffd54a; margin-bottom:8px; }}
.toc summary:hover {{ color:#ffcc00; }}
.toc ul {{ list-style:none; padding-left:0; }}
.toc li {{ margin:4px 0; }}
.toc li ul {{ padding-left:16px; }}
.toc a {{ color:#ffd54a; text-decoration:none; }}
.toc a:hover {{ color:#ffcc00; text-decoration: underline; }}

/* Nested list fix for main content */
main ul {{ list-style-type: disc; margin:8px 0 8px 20px; padding-left:20px; }}
main ul ul {{ list-style-type: circle; margin:4px 0 4px 20px; padding-left:20px; }}
main ul ul ul {{ list-style-type: square; margin:2px 0 2px 20px; padding-left:20px; }}
main ul li {{ display:list-item; }}
</style>
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

<script>
// Back-to-top button
const backToTop = document.getElementById('back-to-top');
window.addEventListener('scroll', () => {{
    if(window.scrollY > 200) backToTop.classList.add('show');
    else backToTop.classList.remove('show');
}});
backToTop.addEventListener('click', () => {{
    window.scrollTo({{ top: 0, behavior: 'smooth' }});
}});

// Smooth scroll for internal links accounting for sticky header
document.querySelectorAll('main a[href^="#"]').forEach(anchor => {{
    anchor.addEventListener('click', function(e) {{
        const targetId = this.getAttribute('href').substring(1);
        const targetEl = document.getElementById(targetId);
        const headerOffset = document.querySelector('header').offsetHeight + 8;
        if (targetEl) {{
            e.preventDefault();
            const elementPosition = targetEl.getBoundingClientRect().top + window.pageYOffset;
            const offsetPosition = elementPosition - headerOffset;
            window.scrollTo({{ top: offsetPosition, behavior: 'smooth' }});
        }}
    }});
}});
</script>

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
