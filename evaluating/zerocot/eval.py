import pandas as pd
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, classification_report

df = pd.read_csv(r'evaluating\zerocot\SDCNL.csv')

model_cols = [col for col in df.columns if col.startswith('gemini')]

for col in model_cols:
    y_true = df['is_suicide']
    y_pred = df[col]

    accuracy = accuracy_score(y_true, y_pred)
    precision = precision_score(
        y_true, y_pred, average='weighted', zero_division=0)
    recall = recall_score(y_true, y_pred, average='weighted', zero_division=0)
    f1 = f1_score(y_true, y_pred, average='weighted', zero_division=0)
    print(f"Metrics for {col}:")
    print(f"  Accuracy: {accuracy:.4f}")
    print(f"  Precision: {precision:.4f}")
    print(f"  Recall: {recall:.4f}")
    print(f"  F1-Score: {f1:.4f}")
    # print("Classification Report:")
    # print(classification_report(y_true, y_pred, zero_division=0))
    print("-" * 30)

## SDCNL
# Metrics for gemini15flash8b:
#   Accuracy: 0.5726
#   Precision: 0.5725
#   Recall: 0.5726
#   F1-Score: 0.5712
# ------------------------------
# Metrics for gemini15flash:    
#   Accuracy: 0.5778
#   Precision: 0.5884
#   Recall: 0.5778
#   F1-Score: 0.5594
# ------------------------------
# Metrics for gemini20flashexp:
#   Accuracy: 0.5989
#   Precision: 0.6107
#   Recall: 0.5989
#   F1-Score: 0.5841
# ------------------------------
# Metrics for grok21212:
#   Accuracy: 0.5937
#   Precision: 0.5935
#   Recall: 0.5937
#   F1-Score: 0.5934
# ------------------------------


## Irl_belong
# Metrics for gemini15flash8b:
#   Accuracy: 0.5629
#   Precision: 0.5875
#   Recall: 0.5629
#   F1-Score: 0.5582
# ------------------------------
# Metrics for gemini15flash:    
#   Accuracy: 0.5667
#   Precision: 0.5758
#   Recall: 0.5667
#   F1-Score: 0.5676
# ------------------------------
# Metrics for gemini20flashexp: 
#   Accuracy: 0.6017
#   Precision: 0.6054
#   Recall: 0.6017
#   F1-Score: 0.6027
# ------------------------------
# Metrics for grok21212:
#   Accuracy: 0.6216
#   Precision: 0.6262
#   Recall: 0.6216
#   F1-Score: 0.6226
# ------------------------------







######################################### DREADDIT
# Metrics for gemini_15_8b:
#   Accuracy: 0.7874
#   Precision: 0.7931
#   Recall: 0.7874
#   F1-Score: 0.7857
# Classification Report:
#               precision    recall  f1-score   support

#           No       0.83      0.70      0.76       346
#          Yes       0.76      0.87      0.81       369

#     accuracy                           0.79       715
#    macro avg       0.79      0.78      0.78       715
# weighted avg       0.79      0.79      0.79       715

# ------------------------------
# Metrics for gemini_15:
#   Accuracy: 0.7189
#   Precision: 0.7914
#   Recall: 0.7189
#   F1-Score: 0.6968
# Classification Report:
#               precision    recall  f1-score   support

#           No       0.94      0.45      0.61       346
#          Yes       0.65      0.97      0.78       369

#     accuracy                           0.72       715
#    macro avg       0.80      0.71      0.69       715
# weighted avg       0.79      0.72      0.70       715

# ------------------------------
# Metrics for gemini_20:
#   Accuracy: 0.7958
#   Precision: 0.8194
#   Recall: 0.7958
#   F1-Score: 0.7907
# Classification Report:
#               precision    recall  f1-score   support

#           No       0.91      0.64      0.75       346
#          Yes       0.74      0.94      0.83       369

#     accuracy                           0.80       715
#    macro avg       0.82      0.79      0.79       715
# weighted avg       0.82      0.80      0.79       715

######################################### SDCNL
# Metrics for gemini_15_8b:
#   Accuracy: 0.5884
#   Precision: 0.5939
#   Recall: 0.5884
#   F1-Score: 0.5787
# Classification Report:
#               precision    recall  f1-score   support

#           No       0.61      0.44      0.51       186
#          Yes       0.57      0.74      0.65       193

#     accuracy                           0.59       379
#    macro avg       0.59      0.59      0.58       379
# weighted avg       0.59      0.59      0.58       379

# ------------------------------
# Metrics for gemini_15:
#   Accuracy: 0.5040
#   Precision: 0.4948
#   Recall: 0.5040
#   F1-Score: 0.4307
# Classification Report:
#               precision    recall  f1-score   support

#           No       0.48      0.14      0.22       186
#          Yes       0.51      0.85      0.64       193

#     accuracy                           0.50       379
#    macro avg       0.49      0.50      0.43       379
# weighted avg       0.49      0.50      0.43       379

# ------------------------------
# Metrics for gemini_20:
#   Accuracy: 0.5778
#   Precision: 0.5877
#   Recall: 0.5778
#   F1-Score: 0.5604
# Classification Report:
#               precision    recall  f1-score   support

#           No       0.61      0.38      0.47       186
#          Yes       0.56      0.77      0.65       193

#     accuracy                           0.58       379
#    macro avg       0.59      0.57      0.56       379
# weighted avg       0.59      0.58      0.56       379

# ------------------------------

######################################### Irf_belong
# Metrics for gemini15flash8b:
#   Accuracy: 0.6424
#   Precision: 0.6676
#   Recall: 0.6424
#   F1-Score: 0.6064
# Classification Report:
#               precision    recall  f1-score   support

#           No       0.72      0.32      0.45       472
#          Yes       0.62      0.90      0.74       585

#     accuracy                           0.64      1057
#    macro avg       0.67      0.61      0.59      1057
# weighted avg       0.67      0.64      0.61      1057

# ------------------------------
# Metrics for gemini15flash:
#   Accuracy: 0.6367
#   Precision: 0.7049
#   Recall: 0.6367
#   F1-Score: 0.5769
# Classification Report:
#               precision    recall  f1-score   support

#           No       0.82      0.24      0.37       472
#          Yes       0.61      0.96      0.75       585

#     accuracy                           0.64      1057
#    macro avg       0.72      0.60      0.56      1057
# weighted avg       0.70      0.64      0.58      1057

# ------------------------------
# Metrics for gemini20flashexp:
#   Accuracy: 0.6358
#   Precision: 0.6734
#   Recall: 0.6358
#   F1-Score: 0.5905
# Classification Report:
#                 precision    recall  f1-score   support
#             No       0.75      0.28      0.41       472
#            Yes       0.61      0.92      0.74       585
#       accuracy                           0.64      1057
#      macro avg       0.45      0.40      0.38      1057
#   weighted avg       0.67      0.64      0.59      1057