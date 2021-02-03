import os, imageio

png_dir = './saves1/'
images = []
for x in range(2,822):
    images.append(imageio.imread("./saves/box" + str(x) + ".png"))

imageio.mimsave('./saves1/gif/movie.gif', images, fps=55)