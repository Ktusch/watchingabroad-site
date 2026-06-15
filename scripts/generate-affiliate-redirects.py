#!/usr/bin/env python3
"""
WatchingAbroad Affiliate Redirect Generator
Regenerates /go/{vendor}/index.html redirect pages from go/config.json.

Usage:
    python3 scripts/generate-affiliate-redirects.py

Run this after updating config.json to rebuild all redirect pages.
"""
import json, os, html

SITE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONFIG_PATH = os.path.join(SITE_DIR, "go", "config.json")
GO_DIR = os.path.join(SITE_DIR, "go")

REDIRECT_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="robots" content="noindex, nofollow">
  <title>Redirecting — {name}</title>
  <style>
    body {{
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Arial, sans-serif;
      background: #08111f; color: #eef5ff; display: flex; align-items: center;
      justify-content: center; min-height: 100vh; margin: 0; text-align: center;
    }}
    .card {{ background: #0f1b2d; border: 1px solid #233149; border-radius: 18px; padding: 32px 40px; max-width: 420px; }}
    h1 {{ font-size: 20px; margin: 0 0 12px; color: #38bdf8; }}
    p {{ color: #9eb0c7; margin: 0 0 16px; font-size: 14px; line-height: 1.5; }}
    .spinner {{ display: inline-block; width: 24px; height: 24px; border: 3px solid #233149; border-top-color: #38bdf8; border-radius: 50%; animation: spin .8s linear infinite; }}
    @keyframes spin {{ to {{ transform: rotate(360deg); }} }}
  </style>
  {meta_redirect}
</head>
<body>
  <div class="card">
    <h1>→ Redirecting to {escaped_name}</h1>
    <p>You are being redirected to {escaped_name}.</p>
    <div class="spinner"></div>
    <p style="font-size: 12px; margin-top: 20px; color: #718096;">
      If you are not redirected automatically, <a href="{target_url}" style="color: #38bdf8;">click here</a>.
    </p>
  </div>
  {js_redirect}
  {tracking_pixel}
</body>
</html>
"""


def load_config():
    with open(CONFIG_PATH) as f:
        return json.load(f)


def build_redirect_html(slug, vendor):
    """Generate a redirect HTML page for a single vendor."""
    target_url = vendor["target_url"]
    name = vendor["name"]

    if not target_url:
        # Placeholder mode — show coming soon instead of redirecting
        return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="robots" content="noindex, nofollow">
  <title>{name} — Affiliate Link</title>
  <style>
    body {{
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Arial, sans-serif;
      background: #08111f; color: #eef5ff; display: flex; align-items: center;
      justify-content: center; min-height: 100vh; margin: 0; text-align: center;
    }}
    .card {{ background: #0f1b2d; border: 1px solid #233149; border-radius: 18px; padding: 32px 40px; max-width: 420px; }}
    h1 {{ font-size: 20px; margin: 0 0 12px; color: #38bdf8; }}
    p {{ color: #9eb0c7; margin: 8px 0; font-size: 14px; line-height: 1.5; }}
    .badge {{ display: inline-block; background: rgba(56, 189, 248, 0.12); color: #38bdf8; padding: 4px 12px; border-radius: 20px; font-size: 12px; font-weight: 600; margin-bottom: 12px; }}
    a {{ color: #38bdf8; }}
  </style>
</head>
<body>
  <div class="card">
    <div class="badge">⏳ Awaits setup</div>
    <h1>{name}</h1>
    <p>The affiliate link for <strong>{name}</strong> is not yet active.</p>
    <p style="font-size: 12px; color: #718096;">
      Status: {vendor["status"]}<br>
      {vendor["note"]}
    </p>
    <p style="font-size: 12px; margin-top: 16px;"><a href="/">← Back to WatchingAbroad</a></p>
  </div>
</body>
</html>"""

    escaped_name = html.escape(name)
    escaped_target = html.escape(target_url, quote=True)
    meta_redirect = f'<meta http-equiv="refresh" content="0; url={escaped_target}">'
    js_redirect = f'<script>window.location.replace("{escaped_target}");</script>'

    # Gauges tracking pixel — placeholder for affiliate network tracking
    tracking_pixel = f'<img src="https://watchingabroad.com/go/_track.gif?v={slug}&c={vendor["campaign"]}" alt="" width="1" height="1" style="position:absolute;left:-9999px;">'

    return REDIRECT_TEMPLATE.format(
        name=escaped_name,
        escaped_name=escaped_name,
        target_url=escaped_target,
        meta_redirect=meta_redirect,
        js_redirect=js_redirect,
        tracking_pixel=tracking_pixel,
    )


def main():
    config = load_config()
    vendors = config.get("vendors", {})

    for slug, vendor in vendors.items():
        html_content = build_redirect_html(slug, vendor)
        dest_dir = os.path.join(GO_DIR, slug)
        os.makedirs(dest_dir, exist_ok=True)
        dest_path = os.path.join(dest_dir, "index.html")
        with open(dest_path, "w") as f:
            f.write(html_content)
        print(f"  ✅ /go/{slug}/ → {vendor['name']}")

    print(f"\n✅ Generated {len(vendors)} redirect pages from config.json")
    print("   Run this script again after updating config.json with real affiliate URLs.")


if __name__ == "__main__":
    main()
