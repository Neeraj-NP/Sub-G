# Video Subtitle Generator

A Python-based application that automatically generates subtitles for video files using OpenAI's Whisper model.

## Features

- Upload video files (supports .mp4, .avi, .mkv)
- Automatic speech-to-text transcription using Whisper
- Generate .srt subtitle files
- Option to embed subtitles directly into the video
- Web-based interface for easy use

## Prerequisites

- Python 3.8 or higher
- FFmpeg installed on your system
- GPU recommended for faster processing (but not required)

## Installation

1. Clone this repository:
```bash
git clone <repository-url>
cd video-subtitle-generator
```

2. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install the required packages:
```bash
pip install -r requirements.txt
```

4. Install FFmpeg:
   - Windows: Download from https://ffmpeg.org/download.html and add to PATH
   - Linux: `sudo apt-get install ffmpeg`
   - macOS: `brew install ffmpeg`

## Usage

1. Start the Flask application:
```bash
python app.py
```

2. Open your web browser and navigate to `http://localhost:5000`

3. Upload a video file and wait for processing

4. Download either the .srt file or the video with embedded subtitles

## Project Structure

- `app.py`: Main Flask application
- `utils/video_processor.py`: Core video processing functionality
- `templates/`: HTML templates
- `uploads/`: Temporary storage for uploaded videos
- `outputs/`: Generated subtitle files and processed videos

## Notes

- Processing time depends on video length and system capabilities
- For better transcription results, ensure clear audio quality
- Maximum video file size is set to 1GB by default
