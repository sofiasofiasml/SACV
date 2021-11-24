import subprocess
import shlex

def printCodec(p):
    if (p.stdout.decode('utf-8') == ''):
        print('ERROR')
    else:
        print(p.stdout.decode('utf-8'))

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
                    ["ffmpeg", "-i", "messi1min.mp4", "-f", "mp3", "messi1min.mp3"]);
                #AAC
                subprocess.call(
                    ["ffmpeg", "-i", "messi1min.mp4", "-c", "copy", "-map",
                     "0:a:0", "messiACC.aac", ]);
                #Merging
                subprocess.call(
                    ["ffmpeg", "-i", "messi1min.mp4", "-i", "messi1min.mp3",
                     "-i", "messiACC.aac",
                     "-map", "0:v", "-map", "1:a", "-c", "copy", "-map",
                     "2:a", "-c", "copy", "messiContainer.mp4"]);
            if task == '3':
                numAudio = subprocess.run(shlex.split(
                    "ffprobe -v error -select_streams a -show_entries stream=index -of csv=p=0 messiContainer.mp4"),
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.STDOUT);
                numVideo = subprocess.run(shlex.split(
                    "ffprobe -v error -select_streams v -show_entries stream=index -of csv=p=0 messiContainer.mp4"),
                    stdout=subprocess.PIPE,
                    stderr=subprocess.STDOUT);
                print('Audio codec')
                for i in range(len(numAudio.stdout.decode('utf-8').splitlines())):
                    p = subprocess.run(shlex.split(
                        "ffprobe -v error -select_streams a:"+ str(i)+ " -show_entries stream=codec_name -of default=noprint_wrappers=1:nokey=1 messiContainer.mp4"),
                        stdout=subprocess.PIPE, stderr=subprocess.STDOUT);
                    printCodec(p)
                print('Video codec and error')
                for j in range(len(numVideo.stdout.decode('utf-8').splitlines())+1):
                    p = subprocess.run(shlex.split(
                        "ffprobe -v error -select_streams v:"+ str(j) +" -show_entries stream=codec_name -of default=noprint_wrappers=1:nokey=1 messiContainer.mp4"),
                        stdout=subprocess.PIPE, stderr=subprocess.STDOUT);
                    printCodec(p)
            if task == '4':
                subprocess.call(
                    ["ffmpeg", "-i", "messi1min.mp4", "-i", "subtitles.srt",
                     "-map", "0", "-map", "1:s", "-c", "copy","-c:s","mov_text", "messiSub.mp4"]);
                subprocess.call(
                    ["ffmpeg", "-i", "messiSub.mp4", "-map", "0:2", "out.srt"]);
                subprocess.call(
                    ["ffmpeg", "-i", "messi1min.mp4", "-vf", "subtitles=subtitles.srt", "messiSubclose.mp4"]);
            if (task != '1' and task != '2' and task != '3' and task != '4'):
                print('error nº exercicis: 1,2,3 i 4')

if __name__ == "__main__":
        Exercice().run()
