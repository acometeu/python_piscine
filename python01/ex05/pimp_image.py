import numpy as np
import matplotlib.pyplot as plt


def ft_invert(array) -> np.asarray:
    '''apply invert filter on the rgb content of an np array'''
    img = array.copy()
    img[:, :, :1] -= (img[:, :, :1] - 128) * 2 + 1
    img[:, :, 1:2] -= (img[:, :, 1:2] - 128) * 2 + 1
    img[:, :, 2:] -= (img[:, :, 2:] - 128) * 2 + 1
    plt.imshow(img)
    plt.show()
    return (img)


def ft_red(array) -> np.asarray:
    '''apply red filter on the rgb content of an np array'''
    img = array.copy()
    img[:, :, 1:2] = 0
    img[:, :, 2:] = 0
    plt.imshow(img)
    plt.show()
    return (img)


def ft_green(array) -> np.asarray:
    '''apply green filter on the rgb content of an np array'''
    img = array.copy()
    img[:, :, 0:1] = 0
    img[:, :, 2:] = 0
    plt.imshow(img)
    plt.show()
    return (img)


def ft_blue(array) -> np.asarray:
    '''apply blue filter on the rgb content of an np array'''
    img = array.copy()
    img[:, :, 0:1] = 0
    img[:, :, 1:2] = 0
    plt.imshow(img)
    plt.show()
    return (img)


def ft_grey(array):
    '''apply better grey filter on the rgb content of an np array'''
    img = array.copy()
    temp = np.add((img[:, :, :1] / (1 / 0.21)),
                  (img[:, :, 1:2] / (1 / 0.72)),
                  (img[:, :, 2:] / (1 / 0.072)))
    img[:, :, :1] = temp
    img[:, :, 1:2] = temp
    img[:, :, 2:] = temp
    plt.imshow(img)
    plt.show()
    return (img)


def main():
    pass


if (__name__ == "__main__"):
    main()
