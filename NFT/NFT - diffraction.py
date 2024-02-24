import cv2,os
import numpy as np
from skimage import draw
from math import radians,ceil,floor

CWD=os.getcwd().replace('\\','/')+'/'
def accu_round(num):
    left=num%1
    if left >=0.5: return ceil(num)
    elif left < 0.5: return floor(num)

## Double-slit comparison
def diffraction1():
    dif_arr=np.zeros((1800,1800,3), np.uint8)
    theta=range(-900,900,1)
    Const=[1,2,3,5,10,20,30,40,50]
    N=2
    for c in range(len(Const)):
        for j in range(0,200):
            for i in theta:
                if i == 0:I=1
                else:
                    sigma=np.pi*Const[c]*np.sin(abs(radians(i/10)))
                    I=((np.sin(sigma/2)**2)*(np.sin(N*sigma/2))**2)/(((sigma/2)**2)*np.sin(sigma/2)**2)
                dif_arr[j+(c)*200][(i+900)]=(0,0,accu_round(255*I))

    dif_image=cv2.imwrite(CWD+'dif_image1.png', dif_arr)
diffraction1()

## N 1-9 comparison
def diffraction2():
    dif_arr=np.zeros((1800,1800,3), np.uint8)
    theta=range(-900,900,1)
    Const=2
    N=[1,2,3,4,5,6,7,8,9]
    for n in N:
        for j in range(0,200):
            for i in theta:
                if i == 0:I=1
                else:
                    sigma=np.pi*Const*np.sin(abs(radians(i/10)))
                    I=((np.sin(sigma/2)**2)*(np.sin(n*sigma/2))**2)/(((sigma/2)**2)*np.sin(sigma/2)**2)
                dif_arr[j+(n-1)*200][(i+900)]=(0,0,accu_round(255*I))

    dif_image=cv2.imwrite(CWD+'dif_image2.png', dif_arr)
# diffraction2()

## 45 degree 1-9 comparison
def diffraction3():
    dif_arr=np.zeros((1800,1800,3), np.uint8)
    theta=range(-1800,1800,2)
    Const=10
    N=[1,2,3,4,5,6,7,8,9]
    for n in N:
        for j in range(0,200):
            for i in theta:
                if i == 0:I=1
                else:
                    sigma=np.pi*Const*np.sin(abs(radians(i/10)))
                    I=((np.sin(sigma/2)**2)*(np.sin(n*sigma/2))**2)/(((sigma/2)**2)*np.sin(sigma/2)**2)
                dif_arr[j+(n-1)*200][int((i+1800)/2)]=(0,0,accu_round(255*I))

    dif_image=cv2.imwrite(CWD+'dif_image3.png', dif_arr)
# diffraction3()

def diffraction4():
    dif_arr=np.zeros((1800,1800,3), np.uint8)
    theta=range(-900,900,1)
    Const=3
    N=[1,2,3,4,5,6,7,8,9]
    for n in N:
        for j in range(0,200):
            for i in theta:
                if i == 0:I=1
                else:
                    sigma=np.pi*Const*np.sin(abs(radians(i/10)))
                    I=((np.sin(sigma/2)**2)*(np.sin(n*sigma/2))**2)/(((sigma/2)**2)*np.sin(sigma/2)**2)
                dif_arr[j+(n-1)*200][(i+900)]=(0,0,accu_round(255*I))

    dif_image=cv2.imwrite(CWD+'dif_image4.png', dif_arr)
# diffraction4()


def diffraction5():
    dif_arr=np.zeros((100,100,3), np.uint8)
    theta=range(-50,50,1)
    Const=25
    N=[1,2,3,4,5]
    for n in N:
        for j in range(0,20):
            for i in theta:
                if i == 0:I=1
                else:
                    sigma=np.pi*Const*np.sin(abs(radians(i/10)))
                    I=((np.sin(sigma/2)**2)*(np.sin(n*sigma/2))**2)/(((sigma/2)**2)*np.sin(sigma/2)**2)
                dif_arr[j+(n-1)*20][(i+50)]=(0,0,accu_round(255*I))
                print(sigma)
                
    dif_image=cv2.imwrite(CWD+'dif_image5.png', dif_arr)
# diffraction5()



# def circle_diffraction():


