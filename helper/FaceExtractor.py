import cv2
import os
import dlib
import progressbar
from name_creator import name_creator
import argparse
import random
import numpy as np


class FaceExtractor:
    def __init__(self, video_path, output_path):
        
        # "/" at the end is aboslutely necesarry
        if video_path[-1] != "/":
            video_path += "/"
        
        self.video_path = video_path
        self.output_path = output_path
        self.total_frames_captured = 0

    def get_boundingbox(self, face, width, height, scale=1.5):
        """
        Expects a dlib face to generate a quadratic bounding box.
        :param face: dlib face class
        :param width: frame width
        :param height: frame height
        :param scale: bounding box size multiplier to get a bigger face region
        :return: x, y, bounding_box_size in opencv form
        """

        x1 = face.left()
        y1 = face.top()
        x2 = face.right()
        y2 = face.bottom()

        size_bb = int(max(x2 - x1, y2 - y1) * scale)

        center_x, center_y = (x1 + x2) // 2, (y1 + y2) // 2

        # Check for out of bounds, x-y top left corner
        x1 = max(int(center_x - size_bb // 2), 0)
        y1 = max(int(center_y - size_bb // 2), 0)

        # Check for too big bb size for given x, y
        size_bb = min(width - x1, size_bb)
        size_bb = min(height - y1, size_bb)

        return x1, y1, size_bb

    def extract_faces(self, num_bins = 10, sample_size = 10):
        """
        Gets a video as input and samples consecutive frames from a starting point
        chosen randomly from a predefined list.

        """
        if os.path.exists(self.video_path):
            print(f"Analyzing videos from {self.video_path}")
        else:
            print(f"Path {self.video_path} does not exist.")
            return

        # Define reader and writer
        for file in os.listdir(self.video_path):
            if not (file.endswith(".mp4") or file.endswith(".avi")):
                continue
            
            # If output dir does not exist, create it
            if not os.path.exists(self.output_path):
                os.makedirs(self.output_path)

            # Define reader object
            reader = cv2.VideoCapture(self.video_path + file)

            # Check if reader works
            if not reader.isOpened():
                print("Error: Could not open video.")
                exit()
            
            # Number of frames of the video
            num_frames = int(reader.get(cv2.CAP_PROP_FRAME_COUNT))
            
            # Check if video file is empty
            if num_frames == 0:
                print("Error: Video file possibly empty.")
                exit()

            # HOG based face detector
            face_detector = dlib.get_frontal_face_detector()

            # Create a list of starting points in the video to sample from
            frame_bins = np.linspace(1, num_frames, num_bins, dtype=int)
            
            # Randomly select the starting point for sampling frames
            start_frame = random.choice(frame_bins)

            # Set the starting point at the selected sampled frame
            reader.set(cv2.CAP_PROP_POS_FRAMES, start_frame)

            frames_captured = 0

            # Loop through frames
            while reader.isOpened() and frames_captured < sample_size:
                # Read the current frame
                _, frame = reader.read()

                # Check for the end of the video
                if frame is None:
                    break

                height, width = frame.shape[:2]

                # Detect faces 
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                detected_faces = face_detector(gray, 1)

                # Check if any faces were detected
                if len(detected_faces):
                    
                    frames_captured += 1
                    self.total_frames_captured += 1

                    # Process only the biggest face
                    face = detected_faces[0]

                    # Get the bounding box of the face
                    x, y, size = self.get_boundingbox(face, width, height)

                    # Crop the face from the frame
                    cropped_face = frame[y:y+size, x:x+size]

                    # Save the face to the output directory
                    cv2.imwrite(
                        f"{self.output_path}/{name_creator(self.total_frames_captured)}.png", cropped_face)
        

if __name__ == "__main__":

    p = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    
    p.add_argument('--video_path', '-i',
                   type=str,
                   help='Path to the directory containing the videos')

    p.add_argument('--output_path', '-o',
                   type=str,
                   default='./Extracted_Faces/',
                   help='Path to the directory where data is saved')

    p.add_argument("--num_bins", '-b',
                   type=int,
                   default=10,
                   help="Number of starting points in the video to sample from")
    
    p.add_argument("--sample_size", '-s',
                    type=int,
                    default=10,
                    help="Number of frames to sample from the videos")

    args = p.parse_args()

    faceExtractor = FaceExtractor(args.video_path, args.output_path)
    faceExtractor.extract_faces(args.num_bins, args.sample_size)
    
