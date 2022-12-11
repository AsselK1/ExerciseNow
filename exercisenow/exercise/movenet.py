import tensorflow as tf
import tensorflow_hub as hub


module = hub.load("https://tfhub.dev/google/movenet/singlepose/lightning/4")
input_size = 192


def movenet(input_image):
    model = module.signatures['serving_default']

    # SavedModel format expects tensor type of int32.
    input_image = tf.cast(input_image, dtype=tf.int32)
    # Run model inference.
    outputs = model(input_image)
    # Output is a [1, 1, 17, 3] tensor.
    keypoints_with_scores = outputs['output_0'].numpy()
    return keypoints_with_scores
