import cv2
import numpy as np


def ft_load(path: str) -> np.array:
    '''Load an image print it's shape, RGB content
       and display it using opencv-python library'''
    try:
        img = cv2.imread(path)
        assert isinstance(img, np.ndarray)
    except Exception:
        print("Error: ft_load arg is not a file or a valid one")
        return

    print(f"The shape of this image is : {img.shape}")
    print(np.concatenate((img[:, :, 2:3], img[:, :, 1:2],
                          img[:, :, 0:1]), axis=2))

    cv2.imshow('image', img)
    cv2.waitKey(0)
    return (np.concatenate((img[:, :, 2:3], img[:, :, 1:2],
                            img[:, :, 0:1]), axis=2))


def main():
    ft_load("../animal.jpeg")
    ft_load("../landscape.jpg")
    ft_load("../red.jpg")
    # ft_load("../red.png")

    # error management
    print("1: ", end=''), ft_load(7)
    print("2: ", end=''), ft_load('abc')
    print("2: ", end=''), ft_load("load_image.py")


if (__name__ == "__main__"):
    main()
