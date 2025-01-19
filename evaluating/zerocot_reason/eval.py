import pandas as pd
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, classification_report

df = pd.read_csv(r'evaluating\zerocot_reason\SDCNL.csv') 

model_cols = [col for col in df.columns if col.startswith('gemini')]

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
# Metrics for gemini15flash8b:
#   Accuracy: 0.6121
#   Precision: 0.6140
#   Recall: 0.6121
#   F1-Score: 0.6115
# ------------------------------
# Metrics for gemini15flash:
#   Accuracy: 0.6174
#   Precision: 0.6216
#   Recall: 0.6174
#   F1-Score: 0.6121
# ------------------------------
# Metrics for gemini20flashexp:
#   Accuracy: 0.6306
#   Precision: 0.6308
#   Recall: 0.6306
#   F1-Score: 0.6298
# ------------------------------
# Metrics for grok21212:
#   Accuracy: 0.6412
#   Precision: 0.6491
#   Recall: 0.6412
#   F1-Score: 0.6344
# ------------------------------


## Irl_belong
# Metrics for gemini15flash8b:
#   Accuracy: 0.5251
#   Precision: 0.5639
#   Recall: 0.5251
#   F1-Score: 0.5066
# ------------------------------
# Metrics for gemini15flash:
#   Accuracy: 0.5591
#   Precision: 0.5755
#   Recall: 0.5591
#   F1-Score: 0.5579
# ------------------------------
# Metrics for gemini20flashexp:
#   Accuracy: 0.5516
#   Precision: 0.5787
#   Recall: 0.5516
#   F1-Score: 0.5448
# ------------------------------
# Metrics for grok21212:
#   Accuracy: 0.5913
#   Precision: 0.6042
#   Recall: 0.5913
#   F1-Score: 0.5915
# ------------------------------













################################# DREADDIT
# Metrics for gemini_20:
#   Accuracy: 0.6280
#   Precision: 0.6699
#   Recall: 0.6280
#   F1-Score: 0.6095
# Classification Report:
#               precision    recall  f1-score   support

#           No       0.58      0.86      0.69       346
#          Yes       0.76      0.41      0.53       369

#     accuracy                           0.63       715
#    macro avg       0.67      0.64      0.61       715
# weighted avg       0.67      0.63      0.61       715

# ------------------------------
# Metrics for gemini_15_8b:
#   Accuracy: 0.6993
#   Precision: 0.7052
#   Recall: 0.6993
#   F1-Score: 0.6984
# Classification Report:
#               precision    recall  f1-score   support

#           No       0.66      0.77      0.71       346
#          Yes       0.74      0.64      0.69       369

#     accuracy                           0.70       715
#    macro avg       0.70      0.70      0.70       715
# weighted avg       0.71      0.70      0.70       715

# ------------------------------
# Metrics for gemini_15:
#   Accuracy: 0.6853
#   Precision: 0.6886
#   Recall: 0.6853
#   F1-Score: 0.6849
# Classification Report:
#               precision    recall  f1-score   support

#           No       0.66      0.73      0.69       346
#          Yes       0.72      0.64      0.68       369

#     accuracy                           0.69       715
#    macro avg       0.69      0.69      0.69       715
# weighted avg       0.69      0.69      0.68       715

# ------------------------------

################################# SDCNL
# Metrics for gemini_15_8b:
#   Accuracy: 0.5963
#   Precision: 0.6035
#   Recall: 0.5963
#   F1-Score: 0.5858
# Classification Report:
#               precision    recall  f1-score   support

#           No       0.63      0.44      0.51       186
#          Yes       0.58      0.75      0.65       193

#     accuracy                           0.60       379
#    macro avg       0.60      0.59      0.58       379
# weighted avg       0.60      0.60      0.59       379

# ------------------------------
# Metrics for gemini_15:
#   Accuracy: 0.5673
#   Precision: 0.5867
#   Recall: 0.5673
#   F1-Score: 0.5337
# Classification Report:
#               precision    recall  f1-score   support

#           No       0.62      0.30      0.40       186
#          Yes       0.55      0.83      0.66       193

#     accuracy                           0.57       379
#    macro avg       0.59      0.56      0.53       379
# weighted avg       0.59      0.57      0.53       379

# ------------------------------
# Metrics for gemini_20:
#   Accuracy: 0.6359
#   Precision: 0.6510
#   Recall: 0.6359
#   F1-Score: 0.6239
# Classification Report:
#               precision    recall  f1-score   support

#           No       0.70      0.46      0.55       186
#          Yes       0.61      0.81      0.69       193

#     accuracy                           0.64       379
#    macro avg       0.65      0.63      0.62       379
# weighted avg       0.65      0.64      0.62       379

# ------------------------------

################################# Irf_belong
# Metrics for gemini15flash8b:
#   Accuracy: 0.6500
#   Precision: 0.6475
#   Recall: 0.6500
#   F1-Score: 0.6458
# Classification Report:
#               precision    recall  f1-score   support

#           No       0.63      0.53      0.58       472
#          Yes       0.66      0.74      0.70       585

#     accuracy                           0.65      1057
#    macro avg       0.65      0.64      0.64      1057
# weighted avg       0.65      0.65      0.65      1057

# ------------------------------
# Metrics for gemini15flash:
#   Accuracy: 0.6679        
#   Precision: 0.6687       
#   Recall: 0.6679
#   F1-Score: 0.6591        
# Classification Report:    
#               precision    recall  f1-score   support

#           No       0.67      0.50      0.57       472
#          Yes       0.67      0.80      0.73       585

#     accuracy                           0.67      1057
#    macro avg       0.67      0.65      0.65      1057
# weighted avg       0.67      0.67      0.66      1057

# ------------------------------
# Metrics for gemini20flashexp:
#   Accuracy: 0.6263
#   Precision: 0.6271
#   Recall: 0.6263
#   F1-Score: 0.6081
# Classification Report:
#               precision    recall  f1-score   support

#           No       0.63      0.40      0.49       472
#          Yes       0.62      0.81      0.71       585

#     accuracy                           0.63      1057
#    macro avg       0.63      0.60      0.60      1057
# weighted avg       0.63      0.63      0.61      1057

# ------------------------------