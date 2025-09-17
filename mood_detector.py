import cv2
from deepface import DeepFace
import vlc
import time
import random
import json
import yt_dlp

# Load moods and links
with open("moods.json", "r") as f:
    mood_links = json.load(f)

# Map emotions → moods
emotion_to_mood = {
    "happy": "happy",
    "sad": "sad",
    "angry": "sad",
    "neutral": "focus",
    "fear": "focus",
    "surprise": "happy",
    "disgust": "sad"
}

# Function to extract direct audio stream from YouTube link
def get_youtube_audio_url(yt_url):
    ydl_opts = {"format": "bestaudio/best", "quiet": True}
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(yt_url, download=False)
        return info["url"]

# Open webcam for ~10 seconds
cap = cv2.VideoCapture(0)
start_time = time.time()
detected_emotion = None

while True:
    ret, frame = cap.read()
    if not ret:
        break

    try:
        # Detect emotion
        result = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)
        detected_emotion = result[0]['dominant_emotion']

        # Draw face box
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            cv2.putText(frame, detected_emotion, (x, y-10),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    except Exception as e:
        print("Error detecting face:", e)

    # Show window
    cv2.imshow("Mood Detector", frame)

    # Exit after 10 seconds
    if time.time() - start_time > 10:
        break
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

if not detected_emotion:
    print("⚠️ No mood detected.")
    exit()

# Map emotion → mood
mood = emotion_to_mood.get(detected_emotion, "focus")
print(f"Detected emotion: {detected_emotion}, mapped mood: {mood}")

# Pick YouTube link for that mood
yt_url = random.choice(mood_links[mood])

# Extract direct audio stream
audio_url = get_youtube_audio_url(yt_url)
print(f"🎵 Playing audio from: {yt_url}")

# Play with VLC (audio only)
player = vlc.MediaPlayer(audio_url)
player.play()

# Keep playing for 1 hour
time.sleep(3600)
