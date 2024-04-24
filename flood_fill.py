import matplotlib.pyplot as plt


def flood_fill(picture, x, y):
    rozmery = picture.shape
    x_img, y_img = rozmery
    if x > (x_img - 1) or y > (y_img - 1) or x < 0 or y < 0:
        return picture
    elif (picture[x, y] == 0) or (picture[x, y] == 2):
        return picture
    elif picture[x, y] == 1:
        picture[x, y] = 2
        plt.imshow(picture, cmap="gray")
        plt.show(block=False)
        plt.pause(0.01)
        plt.clf()
        flood_fill(picture, x + 1, y)
        flood_fill(picture, x - 1, y)
        flood_fill(picture, x, y + 1)
        flood_fill(picture, x, y - 1)
        return picture



def main():
    img = plt.imread("files/img0.png")[:, :, 0]
    # img = plt.imread("files/img1.png")[:, :, 0]
    # img = plt.imread("files/img2.png")[:, :, 0]

    img = flood_fill(img, 0, 0)

    plt.imshow(img, cmap="gray")
    plt.show(block=False)
    plt.pause(5)
    plt.clf()

    # flood_fill(img, 0, 0)


if __name__ == "__main__":
    main()
