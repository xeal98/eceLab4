"""This script loads a .tflite model into LiteRT and continuously takes pictures with a webcam,
printing if the picture is of a cat or a dog."""

import cv2
import numpy as np
from ai_edge_litert.interpreter import Interpreter, SignatureRunner
import sys


def get_litert_runner(model_path: str) -> SignatureRunner:
    """Opens a .tflite model from path and returns a LiteRT SignatureRunner that can be called for inference

    Args:
        model_path (str): Path to a .tflite model

    Returns:
        SignatureRunner: An AI-Edge LiteRT runner that can be invoked for inference."""

    interpreter = Interpreter(model_path=model_path)
    # Allocate the model in memory. Should always be called before doing inference
    interpreter.allocate_tensors()
    print(f"Allocated LiteRT with signatures {interpreter.get_signature_list()}")

    # Create callable object that runs inference based on signatures
    # 'serving_default' is default... but in production should parse from signature
    return interpreter.get_signature_runner("serving_default")


# Function to resize picture and then convert picture to numpy for model ingest
def image_to_np(image_bytes: bytes) -> np.ndarray:
    """Convert image to proper numpy array"""
    image = np.array(image_bytes, dtype=np.uint8)
    scaled = np.resize(image, (150, 150))
    return scaled


# TODO: Function to conduct inference


def main():

    # Verify arguments
    if len(sys.argv) != 2:
        print("Usage: python litert.py <model_path.tflite>")
        exit(1)

    # Create LiteRT SignatureRunner from model path given as argument
    model_path = sys.argv[1]
    runner = get_litert_runner(model_path)
    # Print input and output details of runner
    print(f"Input details:\n{runner.get_input_details()}")
    print(f"Output details:\n{runner.get_output_details()}")

    # Init webcam
    webcam = cv2.VideoCapture(10)  # 0 is default camera index
    if not webcam.isOpened():
        print("Error: Could not open webcam")

    # TODO: Loop to take pictures and invoke inference. Should loop until Ctrl+C keyboard interrupt.
    while True:

        ret, frame = webcam.read()  # Capture a camera frame

        if ret:
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img_array = image_to_np(frame_rgb)
            output = runner(catdog_input=img_array)
            result = output["output_0"][0][0]
            # cv2.imshow("Captured IMage", frame)
            # cv2.destroyAllWindows()
            print(result)
            if result > 1:
                print("Not Cat")
            else:
                print("Cat")
        # print("Done with loop")
        if cv2.waitKey(1) == ord("q"):
            webcam.release()
            cv2.destroyAllWindows()
            break

    # Release the camera
    webcam.release()
    print("Program complete")


# Executes when script is called by name
if __name__ == "__main__":
    main()
