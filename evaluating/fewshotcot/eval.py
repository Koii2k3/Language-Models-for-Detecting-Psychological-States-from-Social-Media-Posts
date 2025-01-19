import pandas as pd
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, classification_report

df = pd.read_csv(r'evaluating\fewshotcot\Irf_belong.csv')

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
#   Accuracy: 0.6148
#   Precision: 0.6270
#   Recall: 0.6148
#   F1-Score: 0.6079
# ------------------------------
# Metrics for gemini15flash:    
#   Accuracy: 0.6069
#   Precision: 0.6110
#   Recall: 0.6069
#   F1-Score: 0.6009
# ------------------------------
# Metrics for gemini20flashexp: 
#   Accuracy: 0.6253
#   Precision: 0.6256
#   Recall: 0.6253
#   F1-Score: 0.6244
# ------------------------------
# Metrics for grok21212:
#   Accuracy: 0.6359
#   Precision: 0.6410
#   Recall: 0.6359
#   F1-Score: 0.6338
# ------------------------------

## Irf_belong
# Metrics for gemini15flash8b:
#   Accuracy: 0.5695
#   Precision: 0.5961
#   Recall: 0.5695
#   F1-Score: 0.5642
# ------------------------------
# Metrics for gemini15flash:
#   Accuracy: 0.5743        
#   Precision: 0.5816       
#   Recall: 0.5743
#   F1-Score: 0.5754        
# ------------------------------
# Metrics for gemini20flashexp:
#   Accuracy: 0.6140
#   Precision: 0.6159
#   Recall: 0.6140
#   F1-Score: 0.6147
# ------------------------------
# Metrics for grok21212:
#   Accuracy: 0.6112
#   Precision: 0.6185
#   Recall: 0.6112
#   F1-Score: 0.6122
# ------------------------------











################################# DREADDIT
# Metrics for gemini_15_8b:
#   Accuracy: 0.7455
#   Precision: 0.7485
#   Recall: 0.7455
#   F1-Score: 0.7453
# Classification Report:
#               precision    recall  f1-score   support

#           No       0.72      0.79      0.75       346
#          Yes       0.78      0.71      0.74       369

#     accuracy                           0.75       715
#    macro avg       0.75      0.75      0.75       715
# weighted avg       0.75      0.75      0.75       715

# ------------------------------
# Metrics for gemini_15:
#   Accuracy: 0.6937
#   Precision: 0.7798
#   Recall: 0.6937
#   F1-Score: 0.6638
# Classification Report:
#               precision    recall  f1-score   support

#           No       0.94      0.39      0.55       346
#          Yes       0.63      0.98      0.77       369

#     accuracy                           0.69       715
#    macro avg       0.78      0.68      0.66       715
# weighted avg       0.78      0.69      0.66       715

# ------------------------------

# Metrics for gemini_20:
#   Accuracy: 0.7650
#   Precision: 0.7954
#   Recall: 0.7650
#   F1-Score: 0.7571
# Classification Report:
#               precision    recall  f1-score   support

#           No       0.89      0.59      0.71       346
#          Yes       0.71      0.93      0.80       369

#     accuracy                           0.77       715
#    macro avg       0.80      0.76      0.76       715
# weighted avg       0.80      0.77      0.76       715

# ------------------------------

################################# SDCNL
# Metrics for gemini_15_8b:
#   Accuracy: 0.6095
#   Precision: 0.6118
#   Recall: 0.6095
#   F1-Score: 0.6086
# Classification Report:
#               precision    recall  f1-score   support

#           No       0.59      0.66      0.62       186
#          Yes       0.63      0.56      0.59       193

#     accuracy                           0.61       379
#    macro avg       0.61      0.61      0.61       379
# weighted avg       0.61      0.61      0.61       379

# ------------------------------
# Metrics for gemini_15:
#   Accuracy: 0.6174
#   Precision: 0.6246
#   Recall: 0.6174
#   F1-Score: 0.6093
# Classification Report:
#               precision    recall  f1-score   support

#           No       0.65      0.47      0.55       186
#          Yes       0.60      0.76      0.67       193

#     accuracy                           0.62       379
#    macro avg       0.63      0.61      0.61       379
# weighted avg       0.62      0.62      0.61       379

# ------------------------------
# Metrics for gemini_20:
#   Accuracy: 0.6148
#   Precision: 0.6153
#   Recall: 0.6148
#   F1-Score: 0.6133
# Classification Report:
#               precision    recall  f1-score   support

#           No       0.62      0.55      0.59       186
#          Yes       0.61      0.67      0.64       193

#     accuracy                           0.61       379
#    macro avg       0.62      0.61      0.61       379
# weighted avg       0.62      0.61      0.61       379

# ------------------------------


################################# Irf_belong
# Metrics for gemini15flash8b:
#   Accuracy: 0.6443
#   Precision: 0.6447
#   Recall: 0.6443
#   F1-Score: 0.6318
# Classification Report:
#               precision    recall  f1-score   support

#           No       0.65      0.45      0.53       472
#          Yes       0.64      0.80      0.71       585

#     accuracy                           0.64      1057
#    macro avg       0.64      0.63      0.62      1057
# weighted avg       0.64      0.64      0.63      1057

# ------------------------------
# Metrics for gemini15flash:
#   Accuracy: 0.6698        
#   Precision: 0.7141       
#   Recall: 0.6698
#   F1-Score: 0.6339        
# Classification Report:
#               precision    recall  f1-score   support

#           No       0.81      0.34      0.48       472
#          Yes       0.64      0.94      0.76       585

#     accuracy                           0.67      1057
#    macro avg       0.72      0.64      0.62      1057
# weighted avg       0.71      0.67      0.63      1057

# ------------------------------
# Metrics for gemini20flashexp:
#   Accuracy: 0.6556
#   Precision: 0.6767
#   Recall: 0.6556
#   F1-Score: 0.6283
# Classification Report:
#               precision    recall  f1-score   support
#           No       0.73      0.37      0.49       472
#          Yes       0.64      0.89      0.74       585
#     accuracy                           0.66      1057
#    macro avg       0.45      0.42      0.41      1057
# weighted avg       0.68      0.66      0.63      1057
# ------------------------------