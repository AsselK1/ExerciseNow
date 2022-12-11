import tensorflow_hub as hub


def movinet_model():
    id = 'a2'
    mode = 'stream'
    version = '3'
    hub_url = f'https://tfhub.dev/tensorflow/movinet/{id}/{mode}/kinetics-600/classification/{version}'
    movinet_model = hub.load(hub_url)
    return movinet_model


model = movinet_model()
