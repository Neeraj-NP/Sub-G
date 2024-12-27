import os
import whisper
import ffmpeg
import pysrt
from moviepy.editor import VideoFileClip
import tempfile

def extract_audio(video_path):
    """Extract audio from video file"""
    temp_audio = tempfile.NamedTemporaryFile(suffix='.wav', delete=False).name
    video = VideoFileClip(video_path)
    video.audio.write_audiofile(temp_audio)
    return temp_audio

def transcribe_audio(audio_path):
    """Transcribe audio using Whisper"""
    model = whisper.load_model("base")
    result = model.transcribe(audio_path)
    return result

def create_srt(transcription, output_path):
    """Create SRT file from transcription"""
    subs = pysrt.SubRipFile()
    
    for i, segment in enumerate(transcription['segments'], 1):
        start = segment['start']
        end = segment['end']
        text = segment['text'].strip()
        
        # Convert time to SRT format
        start_time = pysrt.SubRipTime(seconds=int(start))
        end_time = pysrt.SubRipTime(seconds=int(end))
        
        sub = pysrt.SubRipItem(i, start_time, end_time, text)
        subs.append(sub)
    
    subs.save(output_path)
    return output_path

def embed_subtitles(video_path, srt_path, output_path):
    """Embed subtitles into video"""
    try:
        (
            ffmpeg
            .input(video_path)
            .output(output_path, vf=f'subtitles={srt_path}')
            .overwrite_output()
            .run(capture_stdout=True, capture_stderr=True)
        )
        return output_path
    except ffmpeg.Error as e:
        print('stdout:', e.stdout.decode('utf8'))
        print('stderr:', e.stderr.decode('utf8'))
        raise e

def process_video(video_path):
    """Main function to process video and generate subtitles"""
    try:
        # Create output directory if it doesn't exist
        output_dir = 'outputs'
        os.makedirs(output_dir, exist_ok=True)
        
        # Extract base filename
        base_name = os.path.splitext(os.path.basename(video_path))[0]
        
        # Extract audio
        audio_path = extract_audio(video_path)
        
        # Transcribe audio
        transcription = transcribe_audio(audio_path)
        
        # Create SRT file
        srt_path = os.path.join(output_dir, f"{base_name}.srt")
        create_srt(transcription, srt_path)
        
        # Create video with embedded subtitles
        output_video_path = os.path.join(output_dir, f"{base_name}_with_subs.mp4")
        embed_subtitles(video_path, srt_path, output_video_path)
        
        # Clean up temporary audio file
        os.unlink(audio_path)
        
        return {
            'srt_file': srt_path,
            'video_file': output_video_path
        }
        
    except Exception as e:
        raise Exception(f"Error processing video: {str(e)}")
