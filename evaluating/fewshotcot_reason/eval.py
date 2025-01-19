import pandas as pd
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, classification_report

df = pd.read_csv(r'evaluating\fewshotcot_reason\Irf_belong.csv')

model_cols = [col for col in df.columns if col.startswith('gemini')]

for col in model_cols:
    y_true = df['is_belong']
    y_pred = df[col]
    
    accuracy = accuracy_score(y_true, y_pred)
    precision = precision_score(y_true, y_pred, average='weighted', zero_division=0)
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
#   Accuracy: 0.6306
#   Precision: 0.6324
#   Recall: 0.6306
#   F1-Score: 0.6301
# ------------------------------
# Metrics for gemini15flash:
#   Accuracy: 0.6359
#   Precision: 0.6361
#   Recall: 0.6359
#   F1-Score: 0.6351
# ------------------------------
# Metrics for gemini20flashexp:
#   Accuracy: 0.6227
#   Precision: 0.6227
#   Recall: 0.6227
#   F1-Score: 0.6222
# ------------------------------
# Metrics for grok21212:
#   Accuracy: 0.6148
#   Precision: 0.6151
#   Recall: 0.6148
#   F1-Score: 0.6148
# ------------------------------


## Irf_belong
# Metrics for gemini15flash8b:
#   Accuracy: 0.5478
#   Precision: 0.5796
#   Recall: 0.5478
#   F1-Score: 0.5379
# ------------------------------
# Metrics for gemini15flash:    
#   Accuracy: 0.5771
#   Precision: 0.5901
#   Recall: 0.5771
#   F1-Score: 0.5772
# ------------------------------
# Metrics for gemini20flashexp:
#   Accuracy: 0.5932
#   Precision: 0.5993
#   Recall: 0.5932
#   F1-Score: 0.5943
# ------------------------------
# Metrics for grok21212:
#   Accuracy: 0.5960
#   Precision: 0.6033
#   Recall: 0.5960
#   F1-Score: 0.5971
# ------------------------------








################################# DREADDIT
# ------------------------------
# Metrics for gemini_15:
#   Accuracy: 0.6951
#   Precision: 0.7018
#   Recall: 0.6951
#   F1-Score: 0.6907
# Classification Report:
#               precision    recall  f1-score   support

#           No       0.74      0.58      0.65       346
#          Yes       0.67      0.80      0.73       369

#     accuracy                           0.70       715
#    macro avg       0.70      0.69      0.69       715
# weighted avg       0.70      0.70      0.69       715

# ------------------------------
# Metrics for gemini_15_8b:
#   Accuracy: 0.7049
#   Precision: 0.7075
#   Recall: 0.7049
#   F1-Score: 0.7028
# Classification Report:
#               precision    recall  f1-score   support

#           No       0.73      0.62      0.67       346
#          Yes       0.69      0.78      0.73       369

#     accuracy                           0.70       715
#    macro avg       0.71      0.70      0.70       715
# weighted avg       0.71      0.70      0.70       715

# ------------------------------
# Metrics for gemini_20:
#   Accuracy: 0.7329 
#   Precision: 0.7328
#   Recall: 0.7329
#   F1-Score: 0.7327
# Classification Report:
#               precision    recall  f1-score   support

#           No       0.73      0.71      0.72       346
#          Yes       0.73      0.76      0.74       369

#     accuracy                           0.73       715
#    macro avg       0.73      0.73      0.73       715
# weighted avg       0.73      0.73      0.73       715


################################# SDCNL
# Metrics for gemini_15_8b:
#   Accuracy: 0.6227
#   Precision: 0.6234
#   Recall: 0.6227
#   F1-Score: 0.6211
# Classification Report:
#               precision    recall  f1-score   support

#           No       0.63      0.56      0.59       186
#          Yes       0.62      0.68      0.65       193

#     accuracy                           0.62       379
#    macro avg       0.62      0.62      0.62       379
# weighted avg       0.62      0.62      0.62       379

# ------------------------------
# Metrics for gemini_15:
#   Accuracy: 0.5884
#   Precision: 0.5934
#   Recall: 0.5884
#   F1-Score: 0.5794
# Classification Report:
#               precision    recall  f1-score   support

#           No       0.61      0.44      0.51       186
#          Yes       0.58      0.73      0.64       193

#     accuracy                           0.59       379
#    macro avg       0.59      0.59      0.58       379
# weighted avg       0.59      0.59      0.58       379

# ------------------------------
# Metrics for gemini_20:
#   Accuracy: 0.6412
#   Precision: 0.6452
#   Recall: 0.6412
#   F1-Score: 0.6372
# Classification Report:
#               precision    recall  f1-score   support

#           No       0.67      0.54      0.60       186
#          Yes       0.62      0.74      0.68       193

#     accuracy                           0.64       379
#    macro avg       0.65      0.64      0.64       379
# weighted avg       0.65      0.64      0.64       379

# ------------------------------


################################# Irf_belong
# Metrics for gemini_15_8b:
#   Accuracy: 0.6227
#   Precision: 0.6234
#   Recall: 0.6227
#   F1-Score: 0.6211
# Classification Report:
#               precision    recall  f1-score   support

#           No       0.63      0.56      0.59       186
#          Yes       0.62      0.68      0.65       193

#     accuracy                           0.62       379
#    macro avg       0.62      0.62      0.62       379
# weighted avg       0.62      0.62      0.62       379

# ------------------------------
# Metrics for gemini_15:
#   Accuracy: 0.5884
#   Precision: 0.5934
#   Recall: 0.5884
#   F1-Score: 0.5794
# Classification Report:
#               precision    recall  f1-score   support

#           No       0.61      0.44      0.51       186
#          Yes       0.58      0.73      0.64       193

#     accuracy                           0.59       379
#    macro avg       0.59      0.59      0.58       379
# weighted avg       0.59      0.59      0.58       379

# ------------------------------
# Metrics for gemini_20:
#   Accuracy: 0.6412
#   Precision: 0.6452
#   Recall: 0.6412
#   F1-Score: 0.6372
# Classification Report:
#               precision    recall  f1-score   support

#           No       0.67      0.54      0.60       186
#          Yes       0.62      0.74      0.68       193

#     accuracy                           0.64       379
#    macro avg       0.65      0.64      0.64       379
# weighted avg       0.65      0.64      0.64       379

# ------------------------------