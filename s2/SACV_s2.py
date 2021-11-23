import subprocess

class Exercice():
    def run(self):
        task = 0
        while (task != '1' and task != '2' and task != '3' and task != '4'):
            task = input("Quin exercici vols (1,2,3 i 4): ")
            if task == '1':
                subprocess.call(
                    ["ffmpeg", "-flags2", "+export_mvs", "-i", "messi.mp4", "-vf",
                     "codecview=mv=pf+bf+bb", "Vector.mp4", ]);
            if task == '2':
                #Cut video
                subprocess.call(
                    ["ffmpeg", "-ss", "00:00:00.0", "-i", "messi.mp4", "-c",
                     "copy", "-t", "00:01:00.0", "messi1min.mp4", ]);
                #Video without audio
                subprocess.call(
                    ["ffmpeg", "-i", "messi1min.mp4", "-c",
                     "copy", "-an" , "messiNoAudio.mp4",]);
                #MP3
                subprocess.call(
                    ["ffmpeg", "-i", "messi1min.mp4", "mp3", "messi1min.mp3", ]);
                #AAC
                subprocess.call(
                    ["ffmpeg", "-i", "messi1min.mp4", "-c", "copy", "-map",
                     "0:a:0", "messiACC.aac", ]);
                #Merging
                subprocess.call(
                    ["ffmpeg", "-i", "messi1min.mp4", "-i", "messi1min.mp3", "-c:v",
                     "copy", "-c:a", "aac", "MarginMP3.mp4"]);
                subprocess.call(
                    ["ffmpeg", "-i", "messi1min.mp4", "-i", "messiACC.aac", "-c:v",
                     "copy", "-c:a", "aac", "messiACC.mp4"]);
            if task == '3':
                print('HOLA')
            if task == '4':
                print('HOLA')
            if (task != '1' and task != '2' and task != '3' and task != '4'):
                print('error nº exercicis: 1,2,3 i 4')

if __name__ == "__main__":
        Exercice().run()
