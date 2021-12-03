import subprocess
import os
import socket
class Ex1:
    def __init__(self, video, ChoseeVideo):
        while (
                ChoseeVideo != '1' and ChoseeVideo != '2' and ChoseeVideo != '3' and ChoseeVideo != '4'):
            ChoseeVideo = input(
                "A quina resolució vols? \n 1- 1280:720 \n 2- 640:480 \n 3- 360:240 \n 4- 160:120 \n")
            if ChoseeVideo == '1':
                subprocess.call(
                    ["ffmpeg", "-i", video, "-vf", "scale=1280:720", "-c:a",
                     "copy", videoLessResol, ]);
            if ChoseeVideo == '2':
                subprocess.call(
                    ["ffmpeg", "-i", video, "-vf", "scale=640:480", "-c:a",
                     "copy", videoLessResol, ]);
            if ChoseeVideo == '3':
                subprocess.call(
                    ["ffmpeg", "-i", video, "-s", "360x240", "-c:a", "copy",
                     videoLessResol, ]);
            if ChoseeVideo == '4':
                subprocess.call(
                    ["ffmpeg", "-i", video, "-s", "160x120", "-c:a", "copy",
                     videoLessResol, ]);
            if (
                    ChoseeVideo != '1' and ChoseeVideo != '2' and ChoseeVideo != '3' and ChoseeVideo != '4'):
                print('error nº escollit: 1,2,3 i 4')
        subprocess.call(
            ["ffmpeg", "-i", videoLessResol, "-vcodec", "libvpx", "-qmin", "0",
             "-qmax",
             "50", "-crf", "10", "-b:v", "1M", "-acodec", "libvorbis",
             "vp8.webm"]);
        subprocess.call(
            ["ffmpeg", "-i", videoLessResol, "-vcodec", "libvpx-vp9", "-b:v",
             "1M", "-acodec", "libvorbis", "vp9.webm"]);
        subprocess.call(
            ["ffmpeg", "-i", videoLessResol, "-c:v", "libx265",
             "-c:a", "copy", "h2651pass.mp4"]);
        subprocess.call(
            ["ffmpeg", "-i", videoLessResol, "-c:v", "libaom-av1",
             "-crf", "30", "-b:v", "0", "av1.mkv"]);

if __name__ == '__main__':
    task = '0'
    ChoseeVideo = '0'
    video = '1s.mp4'
    videoLessResol = '1sLess.mp4'
    while(task != '1' and task != '2'  and task != '3' and task != '4'):
        task = input("Quin exercici vols: \n1- Convert them into VP8, VP9, h265 & AV1\n2- Comparision videos\n3- Broadcast it into an IP\n4- Choose the IP to broadcast\n")
        if task == '1':
            Ex1(video, ChoseeVideo)
        if task == '2':
            os.system("ffmpeg -i vp8.webm -i vp9.webm -filter_complex \"blend=all_mode=difference[blend];[0:v]pad=2*iw:2*ih[left];[left][1:v]overlay=w[tmp];[tmp][blend]overlay=0:h\" -c:v libx264 -crf 18 -c:a copy diffVideo.mp4")
            #Las diferencias que he visto son relativamente pocas, solo que hay como unos pixeles blancos que se aprecian por el centro de la pantalla
        if task == '3':
            os.system(
                "ffmpeg -re -i 1s.mp4 -vcodec copy -acodec copy -f mpegts udp://@172.26.16.1:2222" )
        if task == '4':
            IP = input("Quina es la teva IP?\n")
            hostname = socket.gethostname()
            local_ip = socket.gethostbyname(hostname)
            if (IP == '' or len(IP)!=13):
                os.system(
                    "ffmpeg -re -i 1s.mp4 -vcodec copy -acodec copy -f mpegts udp://@"+local_ip+":2222")
                print(local_ip)
            else:
                os.system(
                    "ffmpeg -re -i 1s.mp4 -vcodec copy -acodec copy -f mpegts udp://@" + IP+ ":2222")
                print(IP)

        if (task != '1' and task != '2'  and task != '3' and task != '4'):
            print('error nº exercicis: 1,2,3 i 4')