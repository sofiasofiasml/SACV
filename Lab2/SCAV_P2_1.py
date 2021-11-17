import subprocess

if __name__ == '__main__':
    task = '0'
    while(task != '1' and task != '2'  and task != '3' and task != '4'):
        task = input("Quin exercici vols (1,2,3 i 4): ")
        if task == '1':
            subprocess.call(["ffmpeg", "-ss" ,"00:00:00.0", "-i", "messi.mp4" ,"-c", "copy" ,"-t", "00:00:10.0", "output.mp4",]);
        if task == '2':
            subprocess.call(["ffmpeg", "-i","output.mp4" ,"-vf", "split=2[a][b],[b]histogram,scale = 180:70,format=yuva444p[hh],[a][hh]overlay", "historgam.mp4",]);
        if task == '3':
            subprocess.call(["ffmpeg", "-i", "output.mp4", "-vf", "scale=1280:720","-c:a", "copy", "output720.mp4",]);
            subprocess.call(["ffmpeg", "-i", "output.mp4", "-vf", "scale=640:480", "-c:a","copy", "output480.mp4",]);
            subprocess.call(["ffmpeg", "-i", "output.mp4", "-s", "360x240", "-c:a","copy", "output360x240.mp4",]);
            subprocess.call(["ffmpeg", "-i", "output.mp4", "-s", "160x120", "-c:a", "copy", "output160x120.mp4",]);
        if task == '4':
            subprocess.call(["ffmpeg", "-i", "output.mp4", "-ac", "1", "Mono.flac",]);
        if (task != '1' and task != '2'  and task != '3' and task != '4'):
            print('error nº exercicis: 1,2,3 i 4')

    