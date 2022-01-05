# Gesture_Control_using_OpenCV
This project implements the functionality of volume control, based on the position of your fingers in the video frame. To analyse the video frame I have used OpenCV. The hand-tracking module is from the Google's Mediapipe library which tracks the position of a hand in the video frame based on keypoint detection. Distance between the index and the thumb finger modulates the volume of the PC. 
I have done this on a Mac device, and used the Osascript library to leverage the volume modulation functionality. For windows use: PyCaw library 
