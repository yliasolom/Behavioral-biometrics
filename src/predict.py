import click
import cv2
import numpy as np
from face_recognition import FaceRecognition
import base64
import matplotlib.pyplot as plt
from pprint import pprint

@click.command()
@click.option('--image-path', type=click.Path(exists=True), required=True, help='Path to the image file for face recognition')

def main(image_path, threshold):
    """
    Perform face recognition on the specified image file.
    """
    # Create a FaceRecognition object and load the pre-trained model
    fr = FaceRecognition()
    fr.load('../weights/lfw_model.pkl')

    # Read the image and convert it to RGB format
    img = cv2.imread(image_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Perform face recognition on the image with the specified threshold
    result = fr.predict(image_path, threshold=0.3)

    # Decode the base64-encoded image from the result
    file_bytes = np.frombuffer(base64.b64decode(result["frame"]), np.uint8)
    output = cv2.imdecode(file_bytes, 1)

    # Display the source and output images using Matplotlib
    plt.figure(figsize=(20, 20))
    plt.subplot(1, 2, 1)
    plt.imshow(img)
    plt.title("Source Image")
    plt.subplot(1, 2, 2)
    plt.imshow(output)
    plt.title("Output Image")
    plt.tight_layout()
    plt.show()

    # Print the predictions
    pprint(result["predictions"])

if __name__ == '__main__':
    main()
