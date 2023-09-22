# Produce Classifier
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

The purpose of this repository 
is to create model to classifier plants and fruits using Tensorflow

My idea is to use computer vision models to identify fruits and provide nutritional information.

![produce](https://c1.wallpaperflare.com/preview/561/447/715/produce-fruits-vegetables-farmer-s-market.jpg)

# Setup

To get started, make sure to install all the necessary dependencies and packages listed in the provided YAML file.


```
conda env create -f env.yaml
```



# Dataset

The dataset is publicly available in [Kaggle](https://www.kaggle.com/datasets/yudhaislamisulistya/plants-type-datasets)
and it has been extended using a [fruit dataset](https://www.kaggle.com/datasets/moltean/fruits)


# Model 
Due to computational limitations, the train model will be trained with 3 classes: bananas,coconuts, and aloevera.
Here's a table of the models I've experimented with, along with their respective accuracy:

| Model  | Accuracy |  Classes |
| ------------- | ------------- |  ------------- |
| MobileNet V2  | 80%  | bananas,coconuts, and aloevera |


# Usage 

The demo can be used 
```
python -m streamlit run app.py
```

# Author 
Bryan Piguave
Email: bryan.piguave@eastern.edu
LinkedIn: [Bryan Piguave](https://www.linkedin.com/in/bryan-piguave-llano/)
