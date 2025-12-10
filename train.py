import sys
import modal

app = modal.App("audio-cnn")

image = (
    modal.Image.debian_slim()
    .pip_install_from_requirements("requirements.txt")
    .apt_install(["wget", "unzip", "ffmpeg", "libsndfile1"])
)

@app.function()
def f(i):
    if i % 2 == 0:
        print("Hello", i)
        return i  
    else:
        print("world", i, file=sys.stderr)
        return i * i

@app.local_entrypoint()
def main():
    print(f.local(10))
    print(f.remote(10))
