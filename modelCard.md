# Model Card
For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf
## Model Details
Nurudeen Adesina Created the model. It is a Random forest classifier for prediction using default configuration for training with scikit-learn.

## Intended Use
This model should be used to predict the category of the salary of a person based on it's financials attributes.

## Metrics
The overall model performance was evaluated using Accuracy score. The value is around 0.82. 
The preformance of the model is also evaluated for key slices using F1 beta score, Precision and Recall. 

## Training Data
Data source: The data was obtained from the UCI Machine Learning Repository (https://archive.ics.uci.edu/ml/datasets/census+income)
The original data set has 32561rows and 15 columns
80% of the data is used to train model using stratified KFold.

## Evaluation Data
20% of the data is used to validate the model.

## Ethical Considerations
For Ethical Considerations the metics were also calculated on data slices. This will drive to a model that may potentially discriminate people; 
further investigation before using it should be done.

## Caveats and Recommendations
The data is biased based on gender. Have data imbalance that need to be investigated.
