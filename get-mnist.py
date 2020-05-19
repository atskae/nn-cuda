'''
This script downloads the MNIST handwritten dataset from http://yann.lecun.com/exdb/mnist/
The four .gz files are downloaded, extracted, and placed into a new directory called mnist/
'''

import os, sys
#import urllib2
import urllib.request
import gzip, shutil

mnistPath = 'mnist'

if os.path.exists(mnistPath):
    print('%s already exists' % mnistPath)
    sys.exit()

# Create empty mnist directory
os.mkdir(mnistPath)

# URLS of the four .gz files from MNIST dataset
urls = [
    'http://yann.lecun.com/exdb/mnist/train-images-idx3-ubyte.gz',
    'http://yann.lecun.com/exdb/mnist/train-labels-idx1-ubyte.gz',
    'http://yann.lecun.com/exdb/mnist/t10k-images-idx3-ubyte.gz',
    'http://yann.lecun.com/exdb/mnist/t10k-labels-idx1-ubyte.gz'
]

# Download and extract each .gz file into the MNIST directory
print('Downloading the MNIST dataset to the path %s' % mnistPath)
for i, url in enumerate(urls):
    # Read response
    #response = urllib2.urlopen(url)
    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)
    
    # Save file
    tarfile = mnistPath + '/' + os.path.basename(url)
    with open(tarfile, 'wb') as f:
        # Write file contents to local file
        f.write(response.read())

    # Extract .gz file
    with gzip.open(tarfile, 'r') as fin, open(tarfile.replace('.gz', ''), 'wb') as fout:
        shutil.copyfileobj(fin, fout)

    # Remove .gz
    os.remove(tarfile)

    print('%i/%i: Downloaded and extracted %s' % (i+1, len(urls), tarfile))

print('Download complete.')
