from get_keypoints import get_keypoints
from get_labels import get_labels
from scipy import signal


exercises = ['push up', 'situp', 'pull ups', 'squat']


def main(video_path, required):
    _, shoulder_points = get_keypoints(video_path)
    top_labels = get_labels(video_path)
    ex_time = {'push up': [], 'situp': [], 'pull ups': [], 'squat': []}
    is_exer = False
    for exercise in exercises:
        time = 0
        for label, prob in top_labels:
            if exercise == label:
                if is_exer:
                    ex_time[label][-1][-1] += 1
                else:
                    ex_time[label].append([time, time])
                    is_exer = True
            else:
                is_exer = False
            time += 1
    # i = 0
    for label in exercises:
        local_count = count(ex_time[label], shoulder_points)
        print(label, local_count)
        if local_count >= required[label]:
            continue
        return False
    return True


def count(ex_time, shoulder_points):
    total = 0
    for start, end in ex_time:
        total += len(signal.find_peaks(shoulder_points[start:end + 1], prominence=0.1)[0])
    return total
