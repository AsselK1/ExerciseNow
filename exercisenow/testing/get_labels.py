import tensorflow as tf
from movinet import model
from load_gif import load_gif
import tqdm
from top_label import get_top_k


def get_labels(video_path):
    video = load_gif(video_path)
    init_states = model.init_states(video[tf.newaxis].shape)
    images = tf.split(video[tf.newaxis], video.shape[0], axis=1)
    all_logits = []
    # To run on a video, pass in one frame at a time
    states = init_states
    for image in tqdm.tqdm(images):
        # predictions for each frame
        logits, states = model({**states, 'image': image})
        all_logits.append(logits)

    # concatinating all the logits
    logits = tf.concat(all_logits, 0)
    # estimating probabilities
    probs = tf.nn.softmax(logits, axis=-1)
    label_prob = []
    for prob in probs:
        top = get_top_k(prob, 1)
        label_prob.append(top[0])

    return label_prob

# print(get_labels('your_gif.gif'))
