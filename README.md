Just noticed that app cannot work
This is only README edit, please forgive us


# ExerciseNow
Instructions:
-1. Revert to previous working commit by: `git checkout d9b5b714d61b8ef0c4cbe2911ac91da5437ad6a8`
0. Install following packages:
`pip install django`
`pip install pillow`
`pip install opencv-python`
`pip install scipy`
install tensorflow.

0.1. If you encounter ModuleNotFoundError: No module named 'ExerciseNow', Change: `ExerciseNow.testing.get_keypoints` -> `get_keypoints` in test.py

1. Open the project in the terminal
2. Run `python3 -m venv env`
3. Run `source env/bin/activate`
4. Go to the app folder: exercisenow
5. Run `pip install -r requirements.txt`
6. Run `python manage.py makemigrations`
7. Run `python manage.py migrate`
8. Run `python manage.py runserver`
9. Go to http://127.0.0.1:8000/ on your browser.

Dataset is available at this link: https://drive.google.com/drive/folders/1LhgpEIJPuut4CP6-g_bVFNlPBHbp08fk?usp=sharing. 

Official link of the dataset: https://paperswithcode.com/dataset/infiniterep

To test, add the dataset to the same folder as counter.py
and run `python3 test.py`
