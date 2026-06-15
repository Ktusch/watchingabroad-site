#!/usr/bin/env python3
"""
WatchingAbroad Pre-Publish Compliance Checker
Run BEFORE pushing any new content to the site.
Checks content against SOURCE_OF_TRUTH.md
"""
import re, sys, os

# ── Load source of truth ──
# Known valid emails (from SOURCE_OF_TRUTH.md)
VALID_EMAILS = {"admin@watchingabroad.com", "atlas@watchingabroad.com"}
VALID_PATHS = {"/", "/guides/why-we-built-watchingabroad.html", "/guides/smart-dns-vs-vpn.html",
               "/guides/how-to-setup-smart-dns-apple-tv-fire-tv-router.html",
               "/guides/best-smart-dns-streaming.html",
               "/guides/watch-streaming-while-travelling-checklist.html",
               "/guides/vpn-apple-tv-options-limitations-setup.html",
               "/guides/", "/SOURCE_OF_TRUTH.md"}

def check_file(path):
    """Run all compliance checks against an HTML file."""
    if not os.path.exists(path):
        return [f"❌ File not found: {path}"]

    with open(path) as f:
        content = f.read()

    issues = []

    # 1. Check for invalid email addresses
    emails = set(re.findall(r'[\w.+-]+@[\w-]+\.[\w.-]+', content))
    if emails:
        # Filter out common false positives (code comments, etc.)
        for e in emails:
            if e not in VALID_EMAILS and not e.startswith("example"):
                issues.append(f"❌ Invalid/unknown email: {e}")

    # 2. Check for internal links that might be broken
    internal_links = re.findall(r'href="(/[^"]*)"', content)
    for link in internal_links:
        # Skip anchors and known paths
        if link.startswith("#"):
            continue
        if link not in VALID_PATHS and "mailto:" not in link:
            # It might be a new page being added - just flag it
            if not link.endswith(".html") and not link == "/":
                continue
            # Check if the file exists in the repo
            repo_root = os.path.dirname(os.path.dirname(path)) if "/guides/" in path else os.path.dirname(path) or "."
            local_path = os.path.join(repo_root, link.lstrip("/"))
            if not os.path.exists(local_path):
                issues.append(f"⚠️ Internal link may not exist: {link}")

    # 3. Check for placeholder content
    placeholders = ["coming soon", "under construction", "lorem ipsum", "todo", "tbd", 
                    "placeholder", "🚧", "replace me"]
    for ph in placeholders:
        if ph.lower() in content.lower():
            issues.append(f"⚠️ Possible placeholder content: '{ph}' detected")

    # 4. Check affiliate disclosure
    has_affiliate_links = "sponsored" in content or "nofollow" in content
    has_disclosure = "affiliate" in content.lower() or "commission" in content.lower()
    if has_affiliate_links and not has_disclosure:
        issues.append("❌ Affiliate links found but no disclosure")

    # 5. Check for overclaims (skip CSS and negations)
    # Strip style blocks to avoid CSS false positives
    clean_content = re.sub(r'<style[^>]*>.*?</style>', '', content, flags=re.DOTALL)
    overclaims = ["always works", "100%", "unblock any", "bypass all",
                  "never detected", "works with every"]
    for oc in overclaims:
        if oc.lower() in clean_content.lower():
            # Skip negated versions ("no X can guarantee", "cannot guarantee")
            for line in clean_content.split('\n'):
                if oc.lower() in line.lower():
                    negations = ["no service can", "cannot guarantee", "no tool can",
                                 "no guarantee", "can't guarantee"]
                    is_negated = any(n in line.lower() for n in negations)
                    if not is_negated:
                        issues.append(f"⚠️ Possible overclaim: '{oc}' in: {line.strip()[:80]}")

    return issues

if __name__ == "__main__":
    files = sys.argv[1:] if len(sys.argv) > 1 else []
    if not files:
        # Default: check guides/ directory
        guides_dir = os.path.join(os.path.dirname(__file__) or ".", "guides")
        files = [os.path.join(guides_dir, f) for f in os.listdir(guides_dir) 
                 if f.endswith(".html")]

    all_issues = []
    for f in files:
        issues = check_file(f)
        for issue in issues:
            print(f"{issue}")
            all_issues.append(issue)

    if all_issues:
        print(f"\n{'='*50}")
        print(f"❌ {len(all_issues)} issue(s) found — fix before publishing!")
        sys.exit(1)
    else:
        print("✅ All compliance checks passed!")
        sys.exit(0)
