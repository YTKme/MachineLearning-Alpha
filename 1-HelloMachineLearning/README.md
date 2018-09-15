# Hello Machine Learning

First Hello World program for machine learning.

## Note
* [scikit learn](http://scikit-learn.org/)
* [TensorFlow](https://www.tensorflow.org/)
* Machine learning is a subfield of artificial intelligence.
    * Write one program that can solve many problems without needing to be rewritten.
    * The study of algorithms that learns from examples and experience, instead of relying on hard-coded rules.
* Classifier
    * A function.
    * It takes some data as input and assigns a label to it as output.
    * OK to think of it as a box of rules.
    * There are many different types of classifier, but the input and output type is always the same.
        * If the classifier is a box of rules, then the learning algorithm as the procedure that creates them.
        * It does this by finding patterns in the training data.
    * Start with is called Decision Tree.
* Supervised Learning
    * Technique to write the classifier automatically.
    * Create a classifier by finding patterns in examples.
    * Recipe: Collect Training Data &rarr; Train Classifier &rarr; Make Predictions

## Dependency


## Data
### Training Data
* Measurement
    * Called feature (Weight and Texture)
* Label

| Weight | Texture | Label  |
|:------:|:-------:|:------:|
| 150g   | Bumpy   | Orange |
| 170g   | Bumpy   | Orange |
| 140g   | Smooth  | Apple  |
| 130g   | Smooth  | Apple  |

### Training Data Substitute
| Weight | Texture | Label  |
|:------:|:-------:|:------:|
| 150g   | 0       | 1      |
| 170g   | 0       | 1      |
| 140g   | 1       | 0      |
| 130g   | 1       | 0      |

### New Training Data
| Horsepower | Seats | Label      |
|:----------:|:-----:|:----------:|
| 300        | 2     | sports-car |
| 450        | 2     | sports-car |
| 200        | 8     | minivan    |
| 150        | 9     | minivan    |

## Run

```bash
# Run with training data
# Return 1, which is orange
$ python HelloMLv1.py
[1]
```

## Reference
* [Hello World - Machine Learning Recipes #1](https://www.youtube.com/watch?v=cKxRvEZd3Mw)