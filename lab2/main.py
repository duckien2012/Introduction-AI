import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, export_graphviz
from sklearn import tree
import graphviz
from graphviz import Source
import matplotlib.pyplot as plt
from six import StringIO  
from IPython.display import Image,SVG,display  
import pydotplus
from sklearn.metrics import classification_report, confusion_matrix
import numpy as np

# Step 1: Merge the two files into a single CSV file
file_train = 'poker-hand-training-true.data'
file_test = 'poker-hand-testing.data'
file_merged = 'poker-hand-data.csv'

with open(file_train, 'r') as f_train, open(file_test, 'r') as f_test, open(file_merged, 'w') as f_merged:
    f_merged.write(f_train.read())
    f_merged.write(f_test.read())

# Step 2: Load the merged dataset
attribute_info = ['S1', 'C1', 'S2', 'C2', 'S3', 
                    'C3', 'S4', 'C4', 'S5', 'C5','Class']
data = pd.read_csv(file_merged, header=None , names=attribute_info)

# Step 4: Split the dataset into features and labels
features = data.iloc[:, :-1]  # Exclude the last column
labels = data.iloc[:, -1]  # Select the last column as labels
# Step 5: Perform stratified splitting
train_sizes = [0.4, 0.6, 0.8, 0.9]
test_sizes = [0.6, 0.4, 0.2, 0.1]
random_state = 1

subsets = []
for train_size, test_size in zip(train_sizes, test_sizes):
    X_train, X_test, y_train, y_test = train_test_split(features, labels, 
                                                        train_size=train_size, 
                                                        test_size=test_size, 
                                                        random_state=random_state, 
                                                        stratify=labels)
    subsets.append((X_train, y_train, X_test, y_test))

# Step 6: Generate 16 subsets for different proportions

# (train/test) 40/60
feature_train_40, label_train_40, feature_test_40, label_test_40 = subsets[0]
# (train/test) 60/40
feature_train_60, label_train_60, feature_test_60, label_test_60 = subsets[1]
# (train/test) 80/20
feature_train_80, label_train_80, feature_test_80, label_test_80 = subsets[2]
# (train/test) 90/10
feature_train_90, label_train_90, feature_test_90, label_test_90 = subsets[3]

lable_train = (label_train_40,label_train_60,label_train_80,label_train_90)
lable_test = (label_test_40,label_test_60,label_test_80,label_test_90)


fig, axs = plt.subplots(2, 2, figsize=(10, 10))

bar_width = 0.2  # Width of each bar
offset = 0.1  # Offset between each bar group

for i in range(4):
    ax = axs[i // 2][i % 2]
    unique_train, counts_train = np.unique(lable_train[i], return_counts=True)
    unique_test, counts_test = np.unique(lable_test[i], return_counts=True)
    unique_labels, counts_labels = np.unique(labels, return_counts=True)
    
    # Calculate the x-axis positions for each bar group
    x_train = np.arange(len(unique_train))
    x_test = x_train + bar_width + offset
    x_all = x_train + 2 * (bar_width + offset)

    ax.bar(x_all, counts_labels, width=bar_width, color='green', alpha=1, label='All')
    ax.bar(x_test, counts_test, width=bar_width, color='red', alpha=1, label='Test')
    ax.bar(x_train, counts_train, width=bar_width, color='blue', alpha=1, label='Train')
    
    ax.set_xticks(x_train + bar_width)  # Set the x-axis tick positions to the center of each bar group
    ax.set_xticklabels(unique_train)  # Set the x-axis tick labels as the unique classes
    
    ax.set_title(f'Train/Test Ratio: {train_sizes[i]}/{test_sizes[i]}')
    ax.legend()

plt.tight_layout()
plt.savefig('class_distribution.png')
plt.show()


# Create a function to build and visualize the decision tree
def build_and_visualize_decision_tree(X_train, y_train):
    clf = DecisionTreeClassifier(criterion='entropy',max_depth=3)
    # Fit the classifier to the training data
    clf.fit(X_train, y_train)

    # Visualize the decision tree
    class_labels = ['Nothing', 'One pair', 'Two pairs', 'Three of a kind', 'Straight', 
                        'Flush', 'Full house', 'Four of a kind', 'Straight flush', 'Royal flush']
    # dot_data = StringIO() 
    # export_graphviz(clf, out_file=dot_data, filled=True, rounded=True, special_characters=True,
    #                             feature_names=attribute_info[:-1], class_names=class_labels)
    # graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
    # graph.write_png('diabetes.png')

    graph = Source(tree.export_graphviz(clf, out_file=None
        , feature_names=attribute_info[:-1], class_names=class_labels 
        , filled = True))
    return graph

# # Iterate over the subsets
# for subset in subsets:
#     X_train, y_train, X_test, y_test = subset

#     # Build and visualize the decision tree for the current subset
#     decision_tree = build_and_visualize_decision_tree(X_train, y_train)
#     decision_tree.write_png('diabetes.png')
#     # Display the decision tree image
#     Image(decision_tree.create_png())

#Create an instance of the DecisionTreeClassifier with information gain
# clf = DecisionTreeClassifier(criterion='entropy',max_depth=3)

# # Fit the classifier to the training data
# clf.fit(X_train, y_train)

# # Visualize the decision tree
# class_labels = ['Nothing', 'One pair', 'Two pairs', 'Three of a kind', 'Straight', 
#                     'Flush', 'Full house', 'Four of a kind', 'Straight flush', 'Royal flush']
# dot_data = StringIO() 
# export_graphviz(clf, out_file=dot_data, filled=True, rounded=True, special_characters=True,
#                                feature_names=attribute_info[:-1], class_names=class_labels)
# graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
# graph.write_png('diabetes.png')
# # Display the decision tree image

graph = build_and_visualize_decision_tree(feature_train_40, label_train_40)
# graph_png = graph.create_png()

# # Display the decision tree image in the notebook
# display(Image(graph_png))

display(SVG(graph.pipe(format='svg')))
# for subset in subsets:
#     X_train, y_train, X_test, y_test = subset

#     # Build and fit the decision tree classifier
#     clf = DecisionTreeClassifier(criterion='entropy', max_depth=3)
#     clf.fit(X_train, y_train)

#     # Make predictions on the test set
#     y_pred = clf.predict(X_test)

#     # Generate classification report and confusion matrix
#     report = classification_report(y_test, y_pred)
#     matrix = confusion_matrix(y_test, y_pred)

#     print(f"Train/Test Ratio: {len(X_train)}/{len(X_test)}")
#     print("Classification Report:")
#     print(report)
#     print("Confusion Matrix:")
#     print(matrix)
#     print("-----------------------------")