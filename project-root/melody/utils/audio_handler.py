import ffmpeg
from pydub import AudioSegment

class AudioHandler:
    """Handles audio manipulation tasks like format conversion and volume adjustment."""

    def __init__(self):
        pass

    def convert_format(self, input_file, output_format, output_file=None):
        """Converts audio between different formats using ffmpeg.

        Args:
            input_file (str): Path to the input audio file.
            output_format (str): The desired output format (e.g., "mp3", "wav").
            output_file (str, optional): Path to the output file. If not provided, the output file name will be based on the input file name with the new format.

        Returns:
            str: Path to the output audio file.
        """
        if not output_file:
            output_file = f"{input_file[:-4]}.{output_format}"

        try:
            (
                ffmpeg
                .input(input_file)
                .output(output_file, format=output_format)
                .run(overwrite_output=True)
            )
            return output_file
        except ffmpeg.Error as e:
            print(f"Error converting audio format: {e}")
            return None

    def adjust_volume(self, input_file, volume_factor, output_file=None):
        """Adjusts the volume of an audio file using pydub.

        Args:
            input_file (str): Path to the input audio file.
            volume_factor (float): The volume adjustment factor (e.g., 1.5 for 150% volume, 0.5 for 50% volume).
            output_file (str, optional): Path to the output file. If not provided, the output file name will be based on the input file name with "_adjusted" appended.

        Returns:
            str: Path to the output audio file.
        """
        if not output_file:
            output_file = f"{input_file[:-4]}_adjusted.{input_file[-3:]}"

        try:
            audio = AudioSegment.from_file(input_file)
            audio = audio.apply_gain(volume_factor * 10)  # Apply gain in dB
            audio.export(output_file, format=input_file[-3:])
            return output_file
        except Exception as e:
            print(f"Error adjusting audio volume: {e}")
            return None

    def get_audio_duration(self, input_file):
        """Retrieves the duration of an audio file using pydub.

        Args:
            input_file (str): Path to the input audio file.

        Returns:
            float: Duration of the audio in seconds.
        """
        try:
            audio = AudioSegment.from_file(input_file)
            return audio.duration_seconds
        except Exception as e:
            print(f"Error getting audio duration: {e}")
            return None