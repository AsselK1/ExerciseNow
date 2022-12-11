import tensorflow as tf


def load_gif(file_path, image_size=(224, 224)):
    """Loads a gif file into a TF tensor.

  Use images resized to match what's expected by your model.
  The model pages say the "A2" models expect 224 x 224 images at 5 fps

  Args:
    file_path: path to the location of a gif file.
    image_size: a tuple of target size.

  Returns:
    a video of the gif file
  """

    raw = tf.io.read_file(file_path)
    video = tf.io.decode_gif(raw)

    video = tf.image.resize(video, image_size)

    video = tf.cast(video, tf.float32) / 255.
    return video
