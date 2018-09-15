"""
Hello Machine Learning v1
Apple vs. Orange
Simple program with simple training data
"""

from sklearn import tree

# Training data
# feature = [
#     [140, "smooth"],
#     [130, "smooth"],
#     [150, "bumpy"],
#     [170, "bumpy"]
# ]

# label = [
#     "apple",
#     "apple",
#     "orange",
#     "orange"
# ]

# Training data substitute
feature = [
    [140, 1],
    [130, 1],
    [150, 0],
    [170, 0]
]

label = [
    0,
    0,
    1,
    1
]

# Create classifier
clf = tree.DecisionTreeClassifier()
# Training algorithm
clf = clf.fit(feature, label)

# Run classification prediction
print(clf.predict([[160, 0]]))