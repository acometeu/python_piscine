import numpy as np


def zoom_animal(img: np.asarray) -> np.asarray:
    '''zoom on the face of animal.jpeg passed in subject'''
    return img[200:400, 450:850, 1:2]


def main():
    pass


if (__name__ == "__main__"):
    main()
