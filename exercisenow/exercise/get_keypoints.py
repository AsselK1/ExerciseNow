import tensorflow as tf
# import numpy as np
# from movenet.to_gif import to_gif
from cropping import init_crop_region, run_inference, determine_crop_region
from movenet import movenet, input_size
# from movenet.draw_prediction_on_image import draw_prediction_on_image


def get_keypoints(image_path):
    image = tf.io.read_file(image_path)
    image = tf.image.decode_gif(image)
    num_frames, image_height, image_width, _ = image.shape
    crop_region = init_crop_region(image_height, image_width)

    # output_images = []
    left_hip_points = []
    left_shoulder_points = []
    for frame_idx in range(num_frames):
        keypoints_with_scores = run_inference(
            movenet, image[frame_idx, :, :, :], crop_region,
            crop_size=[input_size, input_size])
        # output_images.append(draw_prediction_on_image(
        #     image[frame_idx, :, :, :].numpy().astype(np.int32),
        #     keypoints_with_scores, crop_region=None,
        #     close_figure=True, output_image_height=300))
        crop_region = determine_crop_region(
            keypoints_with_scores, image_height, image_width)
        left_hip_points.append(1-keypoints_with_scores[0][0][11][0])
        left_shoulder_points.append(1-keypoints_with_scores[0][0][5][0])

    # Prepare gif visualization.
    # output = np.stack(output_images, axis=0)
    # to_gif(output, fps=10)
    return left_hip_points, left_shoulder_points
