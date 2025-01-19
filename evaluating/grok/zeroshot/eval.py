import pandas as pd
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, classification_report

df = pd.read_csv(r'evaluating\grok\zeroshot\Irf_belong.csv') 

model_cols = [col for col in df.columns if col.startswith('grok')]

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
    print("Classification Report:")
    print(classification_report(y_true, y_pred, zero_division=0))
    print("-" * 30)

################################# DREADDIT
# Metrics for grok_2_1212:
#   Accuracy: 0.7077
#   Precision: 0.7907
#   Recall: 0.7077
#   F1-Score: 0.6819
# Classification Report:
#               precision    recall  f1-score   support

#           No       0.95      0.42      0.58       346
#          No.       0.00      0.00      0.00         0
#          Yes       0.64      0.98      0.78       369

#     accuracy                           0.71       715
#    macro avg       0.53      0.47      0.45       715
# weighted avg       0.79      0.71      0.68       715

# ------------------------------

################################# SDCNL
# Metrics for grok_2_1212:
#   Accuracy: 0.6253
#   Precision: 0.6253
#   Recall: 0.6253
#   F1-Score: 0.6249
# Classification Report:
#               precision    recall  f1-score   support

#           No       0.62      0.59      0.61       186
#          Yes       0.63      0.66      0.64       193

#     accuracy                           0.63       379
#    macro avg       0.63      0.62      0.62       379
# weighted avg       0.63      0.63      0.62       379

# ------------------------------

################################# Irf_belong
# Metrics for grok21212:
#   Accuracy: 0.6698
#   Precision: 0.7070
#   Recall: 0.6698
#   F1-Score: 0.6397
# Classification Report:
#               precision    recall  f1-score   support

#           No       0.79      0.36      0.50       472
#          No.       0.00      0.00      0.00         0
#          Yes       0.64      0.92      0.76       585

#     accuracy                           0.67      1057
#    macro avg       0.48      0.43      0.42      1057
# weighted avg       0.71      0.67      0.64      1057

# ------------------------------

