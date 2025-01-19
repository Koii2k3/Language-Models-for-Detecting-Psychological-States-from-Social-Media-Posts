import pandas as pd
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, classification_report

df = pd.read_csv(r'evaluating\grok\zeroshotcot\SDCNL.csv') 

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
#   Accuracy: 0.5937
#   Precision: 0.5935
#   Recall: 0.5937
#   F1-Score: 0.5934
# ------------------------------

## Irl_belong
# Metrics for grok21212:
#   Accuracy: 0.6216
#   Precision: 0.6262
#   Recall: 0.6216
#   F1-Score: 0.6226
# ------------------------------












################################# DREADDIT
# Metrics for grok-2-1212:
#   Accuracy: 0.7692
#   Precision: 0.7769
#   Recall: 0.7692
#   F1-Score: 0.7684
# Classification Report:
#               precision    recall  f1-score   support

#           No       0.73      0.84      0.78       346
#          Yes       0.82      0.70      0.76       369

#     accuracy                           0.77       715
#    macro avg       0.78      0.77      0.77       715
# weighted avg       0.78      0.77      0.77       715

# ------------------------------

################################# SDCNL
# Metrics for grok-2-1212:
#   Accuracy: 0.5066
#   Precision: 0.5842
#   Recall: 0.5066
#   F1-Score: 0.3809
# Classification Report:
#               precision    recall  f1-score   support

#           No       0.50      0.97      0.66       186
#          Yes       0.67      0.06      0.11       193

#     accuracy                           0.51       379
#    macro avg       0.58      0.51      0.39       379
# weighted avg       0.58      0.51      0.38       379

# ------------------------------

################################# Irf_belong
# Metrics for grok21212:
#   Accuracy: 0.5686
#   Precision: 0.6382
#   Recall: 0.5686
#   F1-Score: 0.5424
# Classification Report:
#               precision    recall  f1-score   support

#           No       0.51      0.85      0.64       472
#          Yes       0.74      0.34      0.46       585

#     accuracy                           0.57      1057
#    macro avg       0.63      0.60      0.55      1057
# weighted avg       0.64      0.57      0.54      1057

# ------------------------------