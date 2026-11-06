# -*- coding: utf-8 -*-
"""Recorta os prints do Instagram, removendo toda a interface."""
from pathlib import Path
from PIL import Image

ATT = Path(r"C:\Users\clebe\.dsh\attachments\v1\objects")
OUT = Path(r"C:\Users\clebe\jobeleza-site\assets\img")
OUT.mkdir(parents=True, exist_ok=True)

# (origem, nome final, caixa de recorte)
JOBS = [
    ("00/00843926cc4824ef29e39d0d439ef4f16e9b02beedc9cdee900216cb78bb9b0e",
     "cabelo-longo.jpg", (0, 244, 591, 1080)),
    ("19/198977a7f48e93afd8ba2ff0c55a73fb9953f4ec96adc312cba8b0e64cba09d4",
     "hidratacao-1.jpg", (0, 176, 591, 1038)),
    ("bf/bf6a0c7c4715308d8a65e98fc277df93a038a32f4980a349931304c53902fc26",
     "hidratacao-2.jpg", (0, 176, 591, 1038)),
    ("be/be882069acd3e3f4991f830682edc4676c063f148cda7196862f2cd11bd6b3bd",
     "massagem-costas.jpg", (0, 208, 591, 1030)),
    ("1b/1b620820b87c56151b985fd2e7f5e8284fbfc7ea525deae08ee5d7dbce7d4d3e",
     "cabelo-preto.jpg", (0, 250, 591, 1000)),
    ("ad/ad2962f87a3550cf992e7393d74d26c2170d5b7f6cbae3f4231d01f631d38d30",
     "massagem-pernas.jpg", (0, 312, 591, 908)),
    ("fe/fe56b0a3fc4acbb7095edbbe2fd8b9a34f4ceff3adb2c06a5b8e648188d6137c",
     "antes-depois.jpg", (0, 250, 591, 1000)),
    ("42/42ee732b6ca6da0213c2dc285e81aa6041655f19b285d139c77fa568f16797ef",
     "retrato-cabelo.jpg", None),
]

for src_rel, name, box in JOBS:
    src = ATT / src_rel
    if not src.exists():
        print(f"[falta] {src}")
        continue
    img = Image.open(src).convert("RGB")
    if box:
        img = img.crop(box)
    # limita a 1200px de altura mantendo proporcao
    if img.height > 1200:
        ratio = 1200 / img.height
        img = img.resize((int(img.width * ratio), 1200), Image.LANCZOS)
    dest = OUT / name
    img.save(dest, "JPEG", quality=92, optimize=True, progressive=True)
    print(f"[ok] {name:22s} {img.width}x{img.height}  {dest.stat().st_size // 1024} KB")

print("total:", len(list(OUT.glob('*.jpg'))), "imagens")
