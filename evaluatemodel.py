import numpy as np
import sys
import tensorflow as tf
import time, cv2, os

IMG_WIDTH = 150
IMG_HEIGHT = 150
def main():
    if len(sys.argv) != 3:
        exit("Usage: python evaluatemodel.py [test] [model]")
    model = tf.keras.models.load_model(sys.argv[2])
    yimg, ylab = load_data(sys.argv[1])
    ylab = tf.keras.utils.to_categorical(ylab)
    ytest, ylabel = np.array(yimg), np.array(ylab)
    model.evaluate(ytest,  ylabel, verbose=2)

def load_data(data_dir):
    images = []
    labels = []
    size = (IMG_WIDTH, IMG_HEIGHT)
    for folder in os.listdir(os.path.join(data_dir)):
        for filename in os.listdir(os.path.join(data_dir,str(folder))):
            img = cv2.imread(os.path.join(data_dir,str(folder),filename))
            # print(img.shape)
            img = cv2.resize(img, size)
            if img is not None:
                images.append(img)
                labels.append(folder)
    return (images, labels)

main()