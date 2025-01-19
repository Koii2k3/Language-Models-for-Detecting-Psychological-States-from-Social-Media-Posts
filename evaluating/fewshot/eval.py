import pandas as pd
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, classification_report

df = pd.read_csv(r'evaluating\fewshot\Irf_belong.csv') 

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
    print("Classification Report:")
    print(classification_report(y_true, y_pred, zero_division=0))
    print("-" * 30)

################################# DREADDIT
# Metrics for gemini_15_8b:
#   Accuracy: 0.7552
#   Precision: 0.7886
#   Recall: 0.7552
#   F1-Score: 0.7460
# Classification Report:
#               precision    recall  f1-score   support

#           No       0.89      0.57      0.69       346
#          Yes       0.70      0.93      0.80       369

#     accuracy                           0.76       715
#    macro avg       0.79      0.75      0.74       715
# weighted avg       0.79      0.76      0.75       715

# ------------------------------
# Metrics for gemini_15:
#   Accuracy: 0.7483
#   Precision: 0.7923
#   Recall: 0.7483
#   F1-Score: 0.7361
# Classification Report:
#               precision    recall  f1-score   support

#           No       0.91      0.53      0.67       346
#          Yes       0.68      0.95      0.80       369

#     accuracy                           0.75       715
#    macro avg       0.80      0.74      0.73       715
# weighted avg       0.79      0.75      0.74       715

# ------------------------------
# Metrics for gemini_20:
#   Accuracy: 0.7455
#   Precision: 0.8026
#   Recall: 0.7455
#   F1-Score: 0.7302
# Classification Report:
#               precision    recall  f1-score   support

#           No       0.94      0.51      0.66       346
#          Yes       0.68      0.97      0.80       369

#     accuracy                           0.75       715
#    macro avg       0.81      0.74      0.73       715
# weighted avg       0.80      0.75      0.73       715

# ------------------------------

################################# SDCNL
# ------------------------------
# Metrics for gemini_15_8b:
#   Accuracy: 0.6359
#   Precision: 0.6361
#   Recall: 0.6359
#   F1-Score: 0.6351
# Classification Report:
#               precision    recall  f1-score   support

#           No       0.64      0.59      0.61       186
#          Yes       0.63      0.68      0.66       193

#     accuracy                           0.64       379
#    macro avg       0.64      0.64      0.63       379
# weighted avg       0.64      0.64      0.64       379

# ------------------------------
# Metrics for gemini_15:
#   Accuracy: 0.6675
#   Precision: 0.6675
#   Recall: 0.6675
#   F1-Score: 0.6674
# Classification Report:
#               precision    recall  f1-score   support

#           No       0.66      0.65      0.66       186
#          Yes       0.67      0.68      0.68       193

#     accuracy                           0.67       379
#    macro avg       0.67      0.67      0.67       379
# weighted avg       0.67      0.67      0.67       379

# ------------------------------
# Metrics for gemini_20:
#   Accuracy: 0.6596
#   Precision: 0.6601
#   Recall: 0.6596
#   F1-Score: 0.6588
# Classification Report:
#               precision    recall  f1-score   support

#           No       0.67      0.61      0.64       186
#          Yes       0.65      0.70      0.68       193

#     accuracy                           0.66       379
#    macro avg       0.66      0.66      0.66       379
# weighted avg       0.66      0.66      0.66       379

################################# Irf_belong
# Metrics for gemini15flash8b:
#   Accuracy: 0.6783 
#   Precision: 0.6829
#   Recall: 0.6783   
#   F1-Score: 0.6670 
# Classification Report:
#               precision    recall  f1-score   support

#           No       0.70      0.49      0.57       472
#          Yes       0.67      0.83      0.74       585

#     accuracy                           0.68      1057
#    macro avg       0.68      0.66      0.66      1057
# weighted avg       0.68      0.68      0.67      1057

# ------------------------------
# Metrics for gemini15flash:
#   Accuracy: 0.7313
#   Precision: 0.7352
#   Recall: 0.7313
#   F1-Score: 0.7255
# Classification Report:
#               precision    recall  f1-score   support

#           No       0.76      0.59      0.66       472
#          Yes       0.72      0.85      0.78       585

#     accuracy                           0.73      1057
#    macro avg       0.74      0.72      0.72      1057
# weighted avg       0.74      0.73      0.73      1057

# ------------------------------
# Metrics for gemini20flashexp:
#   Accuracy: 0.7124
#   Precision: 0.7236
#   Recall: 0.7124
#   F1-Score: 0.7008
# Classification Report:
#               precision    recall  f1-score   support

#           No       0.77      0.51      0.61       472
#          Yes       0.69      0.87      0.77       585

#     accuracy                           0.71      1057
#    macro avg       0.73      0.69      0.69      1057
# weighted avg       0.72      0.71      0.70      1057

# ------------------------------