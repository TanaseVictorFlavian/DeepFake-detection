from Classes.FrameExtractor import FrameExtractor
import argparse

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

    faceExtractor = FrameExtractor(args.video_path, args.output_path)
    faceExtractor.extract_faces(args.num_bins, args.sample_size)

    # python ./utils/extract_frames.py -i ../VideoData/Forensics_pp//NeuralTextures/ -o ./ExtractedFaces/Forensicspp/NeuralTextures/ -b 20 -s 2
    # faceExtractor = FrameExtractor("../VideoData/Forensics_pp//NeuralTextures/", "./ExtractedFaces/Forensicspp/NeuralTextures/")
    # faceExtractor.extract_faces(20, 2)

    