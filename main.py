import os
import zipfile
import shutil
import requests
import subprocess
from pathlib import Path

def download_ffmpeg():
    url = "https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-essentials.zip"
    ffmpeg_zip_path = Path("ffmpeg.zip")
    
    # Scarica l'archivio zip di FFmpeg
    print("Scaricando FFmpeg...")
    response = requests.get(url)
    with open(ffmpeg_zip_path, "wb") as file:
        file.write(response.content)
    print("Download completato.")

    # Estrai l'archivio
    with zipfile.ZipFile(ffmpeg_zip_path, "r") as zip_ref:
        zip_ref.extractall("ffmpeg_extracted")
    print("Estrazione completata.")
    
    # Ottieni il percorso della cartella estratta
    ffmpeg_folder = next(Path("ffmpeg_extracted").glob("ffmpeg-*"))
    final_path = Path("C:/Program Files/ffmpeg")
    
    # Copia la cartella estratta nella directory finale con privilegi elevati
    if not final_path.exists():
        shutil.copytree(ffmpeg_folder, final_path)
    else:
        print("La cartella di destinazione esiste già.")

    # Rimuove l'archivio zip e cartelle temporanee
    ffmpeg_zip_path.unlink()
    shutil.rmtree("ffmpeg_extracted")

    # Aggiungi a PATH
    add_to_path(final_path / "bin")

def add_to_path(ffmpeg_bin_path):
    current_path = os.environ["PATH"]
    if str(ffmpeg_bin_path) not in current_path:
        command = f'setx PATH "%PATH%;{ffmpeg_bin_path}"'
        subprocess.run(command, shell=True)
        print("FFmpeg è stato aggiunto a PATH.")
    else:
        print("FFmpeg è già nel PATH.")

if __name__ == "__main__":
    download_ffmpeg()
    print("Installazione completata.")
