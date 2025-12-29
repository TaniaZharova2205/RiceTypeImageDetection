import json
from pathlib import Path

import fire
import numpy as np
import onnx
import onnxruntime as ort
from hydra import compose, initialize
from PIL import Image

from utilities.data_handler import ensure_data_unpacked
from utilities.model_getter import get_processor


def main(model_path: Path, images_to_analyze: Path) -> None:
    with initialize(config_path="../configs", version_base="1.1"):
        config = compose(config_name="config")
        ensure_data_unpacked(model_path)
        onnx.load(model_path)
        ort_session = ort.InferenceSession(model_path)
        with open(
            config["data_loading"]["id2labels_meta"]
        ) as labels_meta_file:
            class_names = json.load(labels_meta_file)

        processor = get_processor()

        for image_path in Path(images_to_analyze).glob("**/*"):
            image = Image.open(image_path).convert("RGB")
            inputs = processor(images=image, return_tensors="pt")
            input_data = {"pixel_values": inputs["pixel_values"].numpy()}

            outputs = ort_session.run(None, input_data)
            predicted_class = np.argmax(outputs[0])

            print(
                "For image: {0}, got breed: {1}".format(
                    image_path, class_names[str(predicted_class)]
                )
            )


if __name__ == "__main__":
    fire.Fire(main)
