"""Validate the included YOLO annotations and write a portable training YAML."""
import argparse
import json
import math
from pathlib import Path


def validate(root):
    root = Path(root).resolve()
    counts = {}
    for split in ("train", "valid", "test"):
        images = [p for p in (root / split / "images").glob("*") if p.suffix.lower() in (".jpg", ".jpeg", ".png")]
        if not images:
            raise ValueError(f"No images found in {split}")
        for image in images:
            label = root / split / "labels" / (image.stem + ".txt")
            if not label.exists():
                raise ValueError(f"Missing annotation for {image.name}")
            for number, row in enumerate(label.read_text().splitlines(), 1):
                fields = row.split()
                if len(fields) != 5:
                    raise ValueError(f"Invalid annotation: {label.name}:{number}")
                class_id, x, y, width, height = map(float, fields)
                if not (class_id in (0, 1, 2, 3) and all(math.isfinite(v) for v in (x,y,width,height))
                        and 0 <= x <= 1 and 0 <= y <= 1 and 0 < width <= 1 and 0 < height <= 1):
                    raise ValueError(f"Invalid class or coordinates: {label.name}:{number}")
        counts[split] = len(images)
    return counts


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--data", default="DATA")
    parser.add_argument("--yaml", default="data.local.yaml")
    args = parser.parse_args()
    print(json.dumps(validate(args.data), indent=2))
    absolute = Path(args.data).resolve().as_posix()
    Path(args.yaml).write_text(f"path: {json.dumps(absolute)}\ntrain: train/images\nval: valid/images\ntest: test/images\nnc: 4\nnames: ['Left-Turn', 'Right-Turn', 'straight', 'unexpected']\n")
