# Moodify

Moodify is a Python application that detects your mood using your webcam and plays a YouTube audio track that matches your mood. It uses facial emotion recognition and maps detected emotions to curated music playlists for different moods.

## Features
- Detects emotion from your face using DeepFace and OpenCV
- Maps detected emotions to moods (happy, sad, focus, sleepy)
- Randomly selects a YouTube track for your mood from a JSON playlist
- Extracts direct audio stream from YouTube using yt-dlp
- Plays audio using VLC for up to 1 hour

## How It Works
1. The app opens your webcam and analyzes your face for about 10 seconds.
2. It uses DeepFace to detect your dominant emotion (happy, sad, angry, neutral, fear, surprise, disgust).
3. The detected emotion is mapped to a mood (e.g., angry → sad, neutral → focus).
4. A random YouTube link for that mood is selected from `moods.json`.
5. The direct audio stream is extracted and played using VLC.

## Requirements
- Python 3.7+
- Webcam
- Internet connection

### Python Packages
- `opencv-python`
- `deepface`
- `python-vlc`
- `yt-dlp`

Install dependencies:
```powershell
pip install opencv-python deepface python-vlc yt-dlp
```

## Usage
1. Place `mood_detector.py` and `moods.json` in the same directory.
2. Run the script:
   ```powershell
   python mood_detector.py
   ```
3. Allow webcam access. The app will analyze your face and play music matching your mood.

## File Descriptions
- `mood_detector.py`: Main script for mood detection and music playback.
- `moods.json`: JSON file containing YouTube links for each mood category.

## Customization
- Add or change YouTube links in `moods.json` to personalize playlists.
- Modify the `emotion_to_mood` mapping in `mood_detector.py` to adjust how emotions are mapped to moods.

## Troubleshooting
- If no mood is detected, ensure your webcam is working and you are visible in the frame.
- Make sure all required Python packages are installed.
- VLC must be installed on your system for audio playback.

## License
This project is for educational and personal use.
