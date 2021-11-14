
import numpy as np
def my_rgbToYuv(v_rgb):
    Y = 0.257*v_rgb[0]+0.504*v_rgb[1]+0.098*v_rgb[2]+16
    U = -0.148*v_rgb[0] -0.291*v_rgb[1]+0.439*v_rgb[2]+128
    V= 0.439*v_rgb[0]-0.368*v_rgb[1]-0.071*v_rgb[2]+128
    return [Y,U,V]
def my_YuvTorgb(v_yuv):
    R = 1.164*(v_yuv[0]-16)+1.596*(v_yuv[2]-128)
    G = 1.164*(v_yuv[0]-16)-0.813*(v_yuv[2]-128)-0.391*(v_yuv[1]-128)
    B = 1.164*(v_yuv[0]-16)+2.018*(v_yuv[1]-128)
    return [R,G,B]

if __name__ == "__main__":
    v_rgb = np.array([0,0,0])
    v_rgb[0] = int(input("R: "))
    v_rgb[1] = int(input("G: "))
    v_rgb[2] = int(input("B: "))
    v_yuv = my_rgbToYuv(v_rgb)
    print("The array of yuv is:", v_yuv)
    v_rgb = my_YuvTorgb(v_yuv)
    print("The array of yuv is:", v_rgb)

