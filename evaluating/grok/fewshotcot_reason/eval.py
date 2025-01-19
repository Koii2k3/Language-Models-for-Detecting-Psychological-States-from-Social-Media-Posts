import pandas as pd
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, classification_report

df = pd.read_csv(r'evaluating\grok\fewshotcot_reason\SDCNL.csv') 

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
#   Accuracy: 0.6148
#   Precision: 0.6151
#   Recall: 0.6148
#   F1-Score: 0.6148
# ------------------------------

## Irl_belong
# Metrics for grok21212:
#   Accuracy: 0.5960
#   Precision: 0.6033
#   Recall: 0.5960
#   F1-Score: 0.5971
# ------------------------------











################################# DREADDIT
# Metrics for grok-2-1212:
#   Accuracy: 0.7175
#   Precision: 0.7253
#   Recall: 0.7175
#   F1-Score: 0.7163
# Classification Report:
#               precision    recall  f1-score   support

#           No       0.68      0.79      0.73       346
#          Yes       0.77      0.64      0.70       369

#     accuracy                           0.72       715
#    macro avg       0.72      0.72      0.72       715
# weighted avg       0.73      0.72      0.72       715

# ------------------------------

################################# SDCNL
# Metrics for grok-2-1212:
#   Accuracy: 0.6412
#   Precision: 0.6412
#   Recall: 0.6412
#   F1-Score: 0.6407
# Classification Report:
#               precision    recall  f1-score   support

#           No       0.64      0.61      0.62       186
#          Yes       0.64      0.67      0.66       193

#     accuracy                           0.64       379
#    macro avg       0.64      0.64      0.64       379
# weighted avg       0.64      0.64      0.64       379

# ------------------------------

################################# Irf_belong
# Metrics for grok21212:
#   Accuracy: 0.6026
#   Precision: 0.5983
#   Recall: 0.6026
#   F1-Score: 0.5970
# Classification Report:
#               precision    recall  f1-score   support

#           No       0.57      0.47      0.51       472
#          Yes       0.62      0.71      0.66       585

#     accuracy                           0.60      1057
#    macro avg       0.60      0.59      0.59      1057
# weighted avg       0.60      0.60      0.60      1057

# ------------------------------