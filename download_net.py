import urllib.request
import os
import zipfile

def download_net(data_dir):
    """
    Downloads inceptionh5 to data_dir.
    InceptionH5 is a modficiation of Inception-v1 specifically
    for use with Image processing techniques since it allows
    you to input an image of arbitrary width/height
    """
    url = 'https://storage.googleapis.com/download.tensorflow.org/models/inception5h.zip'

    if not os.path.exists(data_dir):
        os.makedirs(data_dir)

    model_name = os.path.split(url)[-1]
    local_zip_file = os.path.join(data_dir, model_name)

    if not os.path.exists(local_zip_file):
        # Download
        model_url = urllib.request.urlopen(url)
        with open(local_zip_file, 'wb') as output:
            output.write(model_url.read())

        # Extract
        with zipfile.ZipFile(local_zip_file, 'r') as zip_ref:
            zip_ref.extractall(data_dir)
def download_vgg(data_dir):
    print("Downloading pretrained VGG19")
    url = "http://www.vlfeat.org/matconvnet/models/beta16/imagenet-vgg-verydeep-19.mat"
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)

    model_name = os.path.split(url)[-1]
    local_file = os.path.join(data_dir, model_name)

    if not os.path.exists(local_file):
        # Download
        model_url = urllib.request.urlopen(url)
        with open(local_file, 'wb') as output:
            output.write(model_url.read())
        print("VGG19 Downloaded Successfully")
    else:
        print("Model already downloaded")
