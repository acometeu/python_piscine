import numpy as np
import PIL.Image
import matplotlib.pyplot as plt
from rotate import rotate_animal


def zoom_animal(img: np.asarray) -> np.asarray:
    '''zoom on the face of animal.jpeg passed in subject'''
    return img[200:400, 450:850, 1:2]


def ft_load():
    '''Load an image print it's shape, RGB content
    and display a zoom of it using opencv-python library'''
    try:
        img = np.asarray(PIL.Image.open("../animal.jpeg"))
    except Exception:
        print("Error: ft_load arg is not a file or a valid one")
        return

    print(f"The shape of this image is : {img.shape}")
    print(img)

    img = zoom_animal(img)
    img = rotate_animal(img)
    print(f"The new shape after slicing : {img.shape}")
    print(img)

    plt.imshow(img)
    plt.show()


def main():
    ft_load()


if (__name__ == "__main__"):
    main()
