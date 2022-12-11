import imageio
from tensorflow_docs.vis import embed


def to_gif(images, fps):
    imageio.mimsave('./animation.gif', images, fps=fps)
    return embed.embed_file('./animation.gif')