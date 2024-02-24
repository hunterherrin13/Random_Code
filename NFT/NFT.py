import cv2,os
import numpy as np
from skimage import draw
from math import radians

CWD=os.getcwd().replace('\\','/')+'/'

Fib_arr = [0, 1]
def fibonacci_gen(n):
    if n < len(Fib_arr):return Fib_arr[n]
    else:       
        Fib_arr.append(fibonacci_gen(n - 1) + fibonacci_gen(n - 2))
        return Fib_arr[n]
def fibonacci_maker(Fib_arr):
    fib_im=np.zeros((232,232,3), np.uint8)
    n,m,z=np.shape(fib_im)
    Useful_arr=[]
    for Fib in Fib_arr:
       for _ in range(Fib):
            Useful_arr.append(Fib)
    for i in range(n):
        for j in range(m):
            fib_im[i][j]=Useful_arr[j]
    fib_image=cv2.imwrite(CWD+'fib_im.png', fib_im)
    return fib_image
# fibonacci_gen(11)
# fibonacci_maker(Fib_arr)

def eulers_form():
    eul_arr = np.zeros((1000, 1000,3))
    eul_arr=cv2.arrowedLine(eul_arr,(500,500),(500,1000),(150,150,150),thickness=3,line_type=4,tipLength=0.05)
    eul_arr=cv2.arrowedLine(eul_arr,(500,500),(500,0),(150,150,150),thickness=3,line_type=4,tipLength=0.05)
    eul_arr=cv2.arrowedLine(eul_arr,(500,500),(1000,500),(150,150,150),thickness=3,line_type=4,tipLength=0.05)
    eul_arr=cv2.arrowedLine(eul_arr,(500,500),(0,500),(150,150,150),thickness=3,line_type=4,tipLength=0.05)
    eul_arr=cv2.circle(eul_arr,(500,500),250,color=(0,255,0),thickness=20)
    eul_arr=cv2.ellipse(eul_arr,center=(500,500),axes=(75,75),angle=0,startAngle=302,endAngle=358,color=(255,255,255),thickness=3,lineType=8)
    eul_arr=cv2.line(eul_arr,(620,294),(620,497),(0,0,255),thickness=1)
    eul_arr=cv2.arrowedLine(eul_arr,(502,497),(620,294),(255,255,255),thickness=1,line_type=8,tipLength=0.02)
    

    eul_arr=cv2.circle(eul_arr,(530,480),5,color=(255,255,255),thickness=1)
    eul_arr=cv2.line(eul_arr,(525,485),(535,475),(255,255,255),thickness=1)

    eul_image=cv2.imwrite(CWD+'eul_im.png', eul_arr)
    return eul_image
# eulers_form()

def diffraction():
    dif_arr=np.zeros((1800,1800,3), np.uint8)
    theta=range(-900,900,1)
    Const=100
    N=[1,2,3,4,5,6,7,8,9]
    for n in N:
        for j in range(0,200):
            for i in theta:
                if i == 0:I=1
                else:
                    sigma=Const*np.sin(radians(i))/10
                    I=((np.sin(sigma/2)**2)*(np.sin(n*sigma/2))**2)/(((sigma/2)**2)*np.sin(sigma/2)**2)
                dif_arr[j+(n-1)*200][(i+900)]=(0,0,int(255*I))


    dif_image=cv2.imwrite(CWD+'dif_image.png', dif_arr)
# diffraction()

def diffraction2():
    dif_arr=np.zeros((900,900,3), np.uint8)
    theta=range(-450,450,1)
    Const=20
    N=[1,2,3,4,5,6,7,8,9]
    for n in N:
        for j in range(0,100):
            for i in theta:
                if i == 0:I=1
                else:
                    sigma=Const*np.sin(radians(i))/10
                    I=((np.sin(sigma/2)**2)*(np.sin(n*sigma/2))**2)/(((sigma/2)**2)*np.sin(sigma/2)**2)
                dif_arr[j+(n-1)*100][(i+450)]=(0,0,int(255*I))


    dif_image=cv2.imwrite(CWD+'dif_image2.png', dif_arr)
diffraction2()

# def circle_diffraction():


# np.set_printoptions(threshold=np.inf)
# print(imsize)