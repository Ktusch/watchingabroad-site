#!/usr/bin/env python3
"""Add Open Graph and Twitter Card meta tags to all WatchingAbroad pages."""
import os
import re

SITE_DIR = os.path.dirname(os.path.abspath(__file__))
DOMAIN = "https://watchingabroad.com"

PAGES = [
    ("index.html", "WatchingAbroad — Watch TV Abroad, Clearly Explained",
     "Clear, practical guides for watching your home TV and streaming services while abroad. Smart DNS, VPNs, device setup, and troubleshooting explained without hype.",
     "website"),
    ("guides/best-smart-dns-streaming.html", "Best Smart DNS Services for Streaming Devices — 2026 Comparison",
     "Compare the best Smart DNS services for streaming TV abroad. Tested on Apple TV, Fire TV, smart TVs, and routers. Speed, channel support, and honest limitations.",
     "article"),
    ("guides/best-vpn-for-expats-2026.html", "Best VPNs for Expats 2026 — 7 Tested for Streaming TV Abroad",
     "Live-tested 7 VPNs for expats: NordVPN, Surfshark, ExpressVPN, and more. Find the best VPN for streaming BBC iPlayer, Netflix, and UK TV abroad.",
     "article"),
    ("guides/how-to-setup-smart-dns-apple-tv-fire-tv-router.html", "How to Set Up Smart DNS on Apple TV, Fire TV, and Router — Device Setup Guide",
     "Step-by-step guide to configuring Smart DNS on Apple TV, Amazon Fire TV, and your home router. Get streaming services working abroad in minutes.",
     "article"),
    ("guides/how-to-watch-bbc-iplayer-abroad.html", "How to Watch BBC iPlayer Abroad in 2026 — Step-by-Step Guide",
     "Watch BBC iPlayer from anywhere in the world. Tested step-by-step guide for expats and travellers using VPN and Smart DNS. Works in 2026.",
     "article"),
    ("guides/smart-dns-vs-vpn.html", "Smart DNS vs VPN for Streaming TV Abroad — Which Actually Works?",
     "Smart DNS or VPN for watching your home TV abroad? Speed, privacy, device support, streaming access, and realistic limitations — tested and explained.",
     "article"),
    ("guides/vpn-apple-tv-options-limitations-setup.html", "VPN on Apple TV — Options, Limitations, and Setup Guide",
     "Apple TV doesn't support VPN apps natively. How to use a VPN on Apple TV — router-level VPN, Smart DNS, media streaming DNS, and the honest trade-offs.",
     "article"),
    ("guides/watch-streaming-while-travelling-checklist.html", "How to Watch Streaming Apps While Travelling — Practical Checklist",
     "A complete checklist for watching your home streaming apps while travelling abroad. Pre-trip prep, device setup, Smart DNS, VPN tips, and troubleshooting steps.",
     "article"),
    ("guides/why-we-built-watchingabroad.html", "Why We Built WatchingAbroad — Transparency in VPN & Smart DNS Reviews",
     "Most VPN review sites are owned by the companies they recommend. WatchingAbroad is different — here's why we built this, who we are, and what we promise.",
     "article"),
]

def make_og_tags(filename, title, desc, og_type):
    url = f"{DOMAIN}/{filename}" if filename != "index.html" else DOMAIN
    tags = [
        f'    <meta property="og:title" content="{title.replace(chr(34), chr(39))}" />',
        f'    <meta property="og:description" content="{desc.replace(chr(34), chr(39))}" />',
        f'    <meta property="og:url" content="{url}" />',
        f'    <meta property="og:type" content="{og_type}" />',
        f'    <meta property="og:site_name" content="WatchingAbroad" />',
        f'    <meta name="twitter:card" content="summary_large_image" />',
        f'    <meta name="twitter:title" content="{title.replace(chr(34), chr(39))}" />',
        f'    <meta name="twitter:description" content="{desc.replace(chr(34), chr(39))}" />',
    ]
    return '\n'.join(tags)

def add_meta_to_file(filepath, og_block):
    with open(filepath, 'r') as f:
        content = f.read()

    # Check if OG tags already exist
    if 'og:title' in content:
        print(f"  SKIP {filepath}: already has OG tags")
        return False

    # Insert after the description meta tag or before </head>
    # Find the description meta tag and insert after it
    desc_pattern = r'(<meta name="description"[^>]*/>)'
    match = re.search(desc_pattern, content)
    if match:
        content = content.replace(match.group(1), match.group(1) + '\n' + og_block, 1)
    else:
        # Fallback: insert before </head>
        content = content.replace('</head>', f'{og_block}\n  </head>')

    with open(filepath, 'w') as f:
        f.write(content)

    print(f"  DONE {filepath}: OG + Twitter tags added")
    return True

def main():
    updated = []
    for filename, title, desc, og_type in PAGES:
        filepath = os.path.join(SITE_DIR, filename)
        if not os.path.exists(filepath):
            print(f"  SKIP {filename}: file not found")
            continue

        og_block = make_og_tags(filename, title, desc, og_type)
        if add_meta_to_file(filepath, og_block):
            updated.append(filename)

    print(f"\nUpdated {len(updated)} files: {', '.join(updated)}")

if __name__ == '__main__':
    main()
