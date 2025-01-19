import pandas as pd
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, classification_report

df = pd.read_csv(r'evaluating\grok\fewshotcot\SDCNL.csv') 

model_cols = [col for col in df.columns if col.startswith('grok')]

for col in model_cols:
    y_true = df['is_suicide']
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
# Metrics for grok21212:
#   Accuracy: 0.6359
#   Precision: 0.6410
#   Recall: 0.6359
#   F1-Score: 0.6338
# ------------------------------

## Irf_belong
# Metrics for grok21212:
#   Accuracy: 0.6112
#   Precision: 0.6185
#   Recall: 0.6112
#   F1-Score: 0.6122
# ------------------------------




################################# DREADDIT
# Metrics for grok-2-1212:
#   Accuracy: 0.7748
#   Precision: 0.7800
#   Recall: 0.7748
#   F1-Score: 0.7730
# Classification Report:
#               precision    recall  f1-score   support

#           No       0.82      0.69      0.75       346
#          Yes       0.75      0.85      0.80       369

#     accuracy                           0.77       715
#    macro avg       0.78      0.77      0.77       715
# weighted avg       0.78      0.77      0.77       715

# ------------------------------

################################# SDCNL
# Metrics for grok-2-1212:
#   Accuracy: 0.6201
#   Precision: 0.6460
#   Recall: 0.6201
#   F1-Score: 0.6057
# Classification Report:
#               precision    recall  f1-score   support

#           No       0.58      0.82      0.68       186
#          Yes       0.71      0.43      0.54       193

#     accuracy                           0.62       379
#    macro avg       0.64      0.62      0.61       379
# weighted avg       0.65      0.62      0.61       379

# ------------------------------

################################# Irf_belong
# Metrics for grok21212:
#   Accuracy: 0.6689 
#   Precision: 0.6688
#   Recall: 0.6689
#   F1-Score: 0.6613
# Classification Report:
#               precision    recall  f1-score   support

#           No       0.67      0.51      0.58       472
#          Yes       0.67      0.79      0.73       585

#     accuracy                           0.67      1057
#    macro avg       0.67      0.65      0.65      1057
# weighted avg       0.67      0.67      0.66      1057

# ------------------------------