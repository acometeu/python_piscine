import numpy as np


def rotate_animal(img: np.asarray) -> np.asarray:
    '''Rotate the image passed in parameter in np.asarray format'''
    temp = np.zeros((img.shape[1], img.shape[0], img.shape[2]), dtype=int)
    x = 0
    for i in img:
        y = 0
        for j in i:
            temp[y][x] = j
            y = y + 1
        x = x + 1
    return (temp)


def main():
    pass


if (__name__ == "__main__"):
    main()
