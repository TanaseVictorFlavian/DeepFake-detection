import cv2
import os
import dlib
import progressbar
from name_creator import name_creator


class FaceExtractor:
    def __init__(self, video_path, output_path):
        self.video_path = video_path
        self.output_path = output_path

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

    def extract_faces(self, start_frame=1, end_frame=None):
        """
        Gets a video as input and returns a list of faces selected from random
        frames of the video.
        """
        if os.path.exists(self.video_path):
            print(f"Analyzing videos from {self.video_path}")
        else:
            print(f"Path {self.video_path} does not exist.")
            return

        faces_counter = 0
        # Define reader and writer
        for file in os.listdir(self.video_path):
            # If output dir does not exist, create it
            if not os.path.exists(self.output_path):
                os.makedirs(self.output_path)

            # Define reader object
            reader = cv2.VideoCapture(self.video_path + file)
            num_frames = int(reader.get(cv2.CAP_PROP_FRAME_COUNT))

            # Face detector
            face_detector = dlib.get_frontal_face_detector()

            assert start_frame <= num_frames, \
                "Start frame > Total number of frames"

            assert end_frame <= num_frames, \
                "End frame > Total number of frames"

            end_frame = end_frame if end_frame else num_frames

            frame_counter = 0
            # Loop through frames
            while reader.isOpened():
                # Read the current frame
                _, frame = reader.read()

                # Check for the end of the video
                if frame is None:
                    break

                frame_counter += 1

                if frame_counter < start_frame:
                    continue

                if frame_counter > end_frame:
                    break

                height, width = frame.shape[:2]

                # Detect faces with dlib
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                detected_faces = face_detector(gray, 1)

                # Check if any faces were detected
                if len(detected_faces):
                    faces_counter += 1

                    # Process the biggest face
                    face = detected_faces[0]

                    # Get the bounding box of the face
                    x, y, size = self.get_boundingbox(face, width, height)

                    # Crop the face from the frame
                    cropped_face = frame[y:y+size, x:x+size]

                    # Save the face to the output directory
                    cv2.imwrite(
                        f"{self.output_path}/{name_creator(faces_counter)}.jpg", cropped_face)
