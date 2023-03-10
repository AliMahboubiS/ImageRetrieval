# Import the libraries

# Base Libs
import glob
import numpy as np
import matplotlib.pyplot as plt

from pathlib import Path
from PIL import Image

from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.vgg16 import VGG16, preprocess_input
from tensorflow.keras.models import Model


class FeatureExtractor:
    def __init__(self):
        # Use VGG-16 as the architecture and ImageNet for the weight
        base_model = VGG16(weights='imagenet')
        # Customize the model to return features from fully-connected layer
        self.model = Model(inputs=base_model.input, outputs=base_model.get_layer('fc1').output)
    def extract(self, img):
        # Resize the image
        img = img.resize((224, 224))
        # Convert the image color space
        img = img.convert('RGB')
        # Reformat the image
        x = image.img_to_array(img)
        x = np.expand_dims(x, axis=0)
        x = preprocess_input(x)
        # Extract Features
        feature = self.model.predict(x)[0]
        return feature / np.linalg.norm(feature)

if __name__ == "__main__":
    # Iterate through images (Change the path based on your image location)
    all_features = []
    fe =FeatureExtractor()
    for img_path in glob.glob('train/*.jpg'):
        print(img_path)
        # Extract Features
        feature = fe.extract(img=Image.open(img_path))
        all_features.append(feature)
        # Save the Numpy array (.npy) on designated path

    feature_path = "features.npy"
    np.save(feature_path, all_features)

    # now we can check the Similarity distance base on the 10 lowest distance
    img_paths = glob.glob('train/*.jpg')
    test = glob.glob('test/*.jpg')

    features = np.load('features.npy')
    # Insert the image query
    img = Image.open(test[1])
    # Extract its features
    query = fe.extract(img)
    # Calculate the similarity (distance) between images
    dists = np.linalg.norm(features - query, axis=1)
    # Extract 30 images that have lowest distance
    ids = np.argsort(dists)[:30]
    scores = [(dists[id], img_paths[id]) for id in ids]


    # Visualize the result
    axes=[]
    fig=plt.figure(figsize=(8,8))
    for a in range(5*6):
        score = scores[a]
        axes.append(fig.add_subplot(5, 6, a+1))
        subplot_title=str(score[0])
        axes[-1].set_title(subplot_title)  
        plt.axis('off')
        plt.imshow(Image.open(score[1]))
    fig.tight_layout()
    plt.show()
