import glob

from PIL import Image
import json
import cv2
import os
from scipy import signal
from ExerciseNow.testing.get_keypoints import get_keypoints
import shutil


def convert_mp4_to_jpgs(path, output_path):
    os.mkdir("./InfinityAI_InfiniteRep_squat_v1/"+output_path)
    video_capture = cv2.VideoCapture(path)
    still_reading, image = video_capture.read()
    frame_count = 0
    while still_reading:
        cv2.imwrite(f"./InfinityAI_InfiniteRep_squat_v1/{output_path}/frame_{frame_count:03d}.jpg",
                    image)

        # read next image
        still_reading, image = video_capture.read()
        frame_count += 1


def make_gif(frame_folder):
    images = glob.glob(f"{frame_folder}/*.jpg")
    images.sort()
    frames = [Image.open(image) for image in images]
    frame_one = frames[0]
    frame_one.save("exerc.gif", format="GIF", append_images=frames,
                   save_all=True, duration=50, loop=0)


def counter(shoulders, prom):
    return len(signal.find_peaks(shoulders, prominence=prom)[0])


def test():
    cnt = -1
    accuracy = 0
    for file in os.listdir("../../InfinityAI_InfiniteRep_squat_v1/data"):
        if not 'mp4' in file:
            continue
        print(file)
        cnt += 1
        convert_mp4_to_jpgs("./InfinityAI_InfiniteRep_squat_v1/data/"+file, "output" + str(cnt))
        make_gif("./InfinityAI_InfiniteRep_squat_v1/output" + str(cnt))
        shutil.copyfile("exerc.gif", "./InfinityAI_InfiniteRep_squat_v1/"+str(cnt)+".gif")
        image_path = './InfinityAI_InfiniteRep_squat_v1/' + str(cnt)+".gif"
        # image = tf.io.read_file(image_path)
        # image = tf.image.decode_gif(image)
        _, shoulder = get_keypoints(image_path)
        number = counter(shoulder, 0.1)
        file_num = file[-10:-4]
        f = open("./InfinityAI_InfiniteRep_squat_v1/data/" + str(file_num) + ".json")
        data = json.load(f)
        correct = int(data["images"][-1]["rep_count"])
        if abs(number - correct) < 2:
            accuracy += 1
        print(number, correct)
    accuracy = accuracy / 100
    return accuracy
test()