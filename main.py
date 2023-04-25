import subprocess
import time

downloaded_songs = set()
URL_MUSIC_FILE = "download.music"
MUSIC_PATH = "music"
SUCCESS_DOWNLOAD = 0

def get_music_urls():
    with open(URL_MUSIC_FILE, "r") as f:
        urls = [url.strip() for url in f.readlines()]
    
    return urls

def download_song(url):
    command = [
        "yt-dlp", 
        "--extract-audio", 
        "--audio-format", 
        "mp3", 
        "--output", 
        f"{MUSIC_PATH}/%(title)s.%(ext)s", 
        url
    ]

    return subprocess.run(command, capture_output=True)

def remove_url_of_file(url):
    with open(URL_MUSIC_FILE, "r") as f:
        lines = f.readlines()
    
    if url + "\n" in lines:
        lines.remove(url + "\n")
    elif url in lines:
        lines.remove(url)
    
    with open(URL_MUSIC_FILE, "w") as f:
        f.writelines(lines)

def main():
    while True:
        for url in get_music_urls():
            if url in downloaded_songs:
                print(f"{url} ya ha sido descargado. Saltando...")
                continue

            print(f"Descargando {url}...")
            result = download_song(url)

            if result.returncode == SUCCESS_DOWNLOAD:
                print(f"Descarga exitosa: {url}")
                downloaded_songs.add(url)
                remove_url_of_file(url)
            else:
                print(f"Error al descargar {url}: {result.stderr.decode()}")

        time.sleep(5)

main()