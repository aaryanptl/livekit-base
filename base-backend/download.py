from huggingface_hub import snapshot_download
from livekit.plugins import silero

print("Downloading Silero VAD model...")
silero.VAD.load()

print("Downloading multilingual turn detection model...")
snapshot_download(repo_id="livekit/turn-detector",
                  revision="v0.2.0-intl",
                  repo_type="space")

print("All models downloaded.") 