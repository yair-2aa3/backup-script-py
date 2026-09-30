#!/usr/bin/env python3
"""Backup folder -> zip dengan rotasi (simpan N terakhir)."""
import os, zipfile, argparse, time
ap = argparse.ArgumentParser(); ap.add_argument("src"); ap.add_argument("-n", type=int, default=5)
a = ap.parse_args()
stamp = time.strftime("%Y%m%d_%H%M")
out = f"{os.path.basename(a.src.rstrip('/'))}_{stamp}.zip"
with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
      for root, _, files in os.walk(a.src):
                for f in files:
                              p = os.path.join(root, f); z.write(p, os.path.relpath(p, a.src))
                  print("backup:", out)
        zips = sorted(f for f in os.listdir(".") if f.startswith(os.path.basename(a.src.rstrip('/'))) and f.endswith(".zip"))
for old in zips[:-a.n]: os.remove(old); print("rotated:", old)
  
