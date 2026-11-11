# Road Turn Detection with YOLOv5

An educational object-detection experiment using Ultralytics YOLOv5 and a road-turn dataset. The repository includes labelled train, validation and test images plus a Colab notebook.

## Workflow

The notebook clones YOLOv5, installs its requirements and Roboflow, downloads dataset version 2, trains from `yolov5s.pt`, and runs detection on validation images. Training uses 640-pixel inputs and 120 epochs in the original experiment. No trained weights are included.

## Configuration and execution

Open `Roads_Turns_detector_Using_YOLO_V5.ipynb` in Colab. Set `ROBOFLOW_API_KEY` in the Python process environment using your own authorised credential before the download cell. Do not paste a credential into a notebook cell or save it in outputs. The original credential was removed from current source and must be revoked by its owner; historic commits may still contain it.

GPU training, Roboflow access and downloads are required for the original workflow. Training has not been rerun in this maintenance pass. The notebook clones upstream's default branch, so exact historical reproduction is not guaranteed; pin a tested YOLOv5 revision before reporting new metrics. Downloaded data.yaml paths and generated `exp` output paths must match your current run.

## Evidence and limitations

The notebook contains training and inference code, not a deployed road-safety system. Do not use it for navigation or safety decisions. Dataset origin, redistribution permission and annotation ownership require confirmation. Retain attribution to [Ultralytics YOLOv5](https://github.com/ultralytics/yolov5) and Roboflow; this project does not claim authorship of the detector architecture.

## Included dataset metadata

`DATA/data.yaml` identifies the source as [road-turn-detections version 2](https://universe.roboflow.com/nust-fjqyh/road-turn-detections/dataset/2), workspace `nust-fjqyh`, and records **CC BY 4.0**. This is the repository's metadata, not a newly verified grant from its author. The four classes are Left-Turn, Right-Turn, straight and unexpected. Preserve the source attribution and verify permissions before redistributing data elsewhere.

## Local data path (no Roboflow credential)

The repository already contains the dataset. Validate annotation values and generate a YAML with absolute local paths:

```sh
python validate_data.py
```

This checks image/label pairing, class IDs and normalised box values in all three splits. It does not evaluate visual annotation quality or detector accuracy.

For a new training experiment, follow [Ultralytics YOLOv5's installation and training documentation](https://github.com/ultralytics/yolov5). A historical source revision is `915bbf294bb74c859f0b41f1c23bc395014ea679` (v7.0). In a separate compatible PyTorch environment, install that revision's requirements and point its `train.py --data` argument at the generated absolute `data.local.yaml` path. Start with a one-epoch smoke run before the notebook's 120-epoch experiment. The external training environment, pretrained weights download and GPU training are not verified here; no new detector metrics or weights are claimed.

Maintenance code and documentation were prepared with AI assistance.
