#!/usr/bin/bash
ROOT="$(dirname "$(dirname "$(readlink -fm "$0")")")"
DATA_PATH="$ROOT/data/data"
python3 ../rice_type_image_detection/download_data.py --url muratkokludataset/rice-image-dataset --target_dir $DATA_PATH

dvc add $DATA_PATH
dvc push
