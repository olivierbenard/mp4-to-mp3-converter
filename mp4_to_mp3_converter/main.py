"""
Main module serving the python application.
"""

import argparse
from moviepy.editor import VideoFileClip


def parse_command_line_arguments() -> argparse.Namespace:
    """
    Method parsing the command line arguments
    and returning them in a Namespace object.
    """

    parser = argparse.ArgumentParser(
        description="Extract the audio from the provided video file."
    )
    parser.add_argument("video_file", type=str, help="path to the video file")
    parser.add_argument(
        "audio_file",
        type=str,
        help="path to save the extracted audio file",
    )
    parser.add_argument(
        "-f",
        "--format",
        type=str,
        choices=["mp3", "wav", "ogg"],
        default="mp3",
        help="audio format (default: mp3)",
    )
    parser.add_argument(
        "-b",
        "--bitrate",
        type=str,
        default="192k",
        help="bitrate for the audio file (default: 192k)",
    )

    return parser.parse_args()


def extract_audio_from_video_file(
    video_file: str, audio_file: str, audio_format: str, bitrate: str
) -> None:
    """
    Method extracting the audio file from the video file
    and saving the audio in the given destination.
    """

    video_clip = VideoFileClip(video_file)
    audio_clip = video_clip.audio

    if audio_format:
        audio_file = f"{audio_file}.{audio_format}"

    audio_clip.write_audiofile(audio_file, bitrate=bitrate)

    video_clip.close()
    audio_clip.close()

    print(f"Audio extracted and saved to {audio_file}")


def main() -> None:
    """
    Main method.
    """
    args = parse_command_line_arguments()
    extract_audio_from_video_file(
        video_file=args.video_file,
        audio_file=args.audio_file,
        audio_format=args.format,
        bitrate=args.bitrate,
    )


if __name__ == "__main__":
    main()
