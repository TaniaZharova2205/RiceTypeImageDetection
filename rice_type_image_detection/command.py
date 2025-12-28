import fire


def train_cmd(*args, **kwargs):
    from train import main

    return main(*args, **kwargs)


def test_cmd(*args, **kwargs):
    from test import main

    return main(*args, **kwargs)


def infer_ckpt_cmd(*args, **kwargs):
    from infer import main

    return main(*args, **kwargs)


def infer_onnx_cmd(*args, **kwargs):
    from infer_onnx import main

    return main(*args, **kwargs)


def infer_triton_cmd(*args, **kwargs):
    from infer_triton import main

    return main(*args, **kwargs)


def infer_trt_cmd(*args, **kwargs):
    from infer_trt import main

    return main(*args, **kwargs)


if __name__ == "__main__":
    fire.Fire(
        {
            "train": train_cmd,
            "test": test_cmd,
            "infer": {
                "from_checkpoint": infer_ckpt_cmd,
                "onnx": infer_onnx_cmd,
                "tensorrt": infer_trt_cmd,
                "triton": infer_triton_cmd,
            },
        }
    )
