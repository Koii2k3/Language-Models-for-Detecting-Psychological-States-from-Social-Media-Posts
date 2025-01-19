import pandas as pd
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, classification_report

df = pd.read_csv(r'evaluating\zeroshot\Irf_belong.csv') 

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
#   Accuracy: 0.7077
#   Precision: 0.7804
#   Recall: 0.7077
#   F1-Score: 0.6837
# Classification Report:
#               precision    recall  f1-score   support

#           No       0.93      0.43      0.59       346
#          Yes       0.64      0.97      0.77       369

#     accuracy                           0.71       715
#    macro avg       0.78      0.70      0.68       715
# weighted avg       0.78      0.71      0.68       715

# ------------------------------
# Metrics for gemini_15:
#   Accuracy: 0.7203
#   Precision: 0.7836
#   Recall: 0.7203
#   F1-Score: 0.7005
# Classification Report:
#               precision    recall  f1-score   support

#           No       0.92      0.46      0.62       346
#          Yes       0.66      0.96      0.78       369

#     accuracy                           0.72       715
#    macro avg       0.79      0.71      0.70       715
# weighted avg       0.78      0.72      0.70       715

# ------------------------------
# Metrics for gemini_20:
#   Accuracy: 0.7119
#   Precision: 0.8031
#   Recall: 0.7119
#   F1-Score: 0.6846
# Classification Report:
#               precision    recall  f1-score   support

#           No       0.97      0.42      0.58       346
#          Yes       0.64      0.99      0.78       369

#     accuracy                           0.71       715
#    macro avg       0.81      0.70      0.68       715
# weighted avg       0.80      0.71      0.68       715


################################# SDCNL
# ------------------------------
# Metrics for gemini_15_8b:
#   Accuracy: 0.5673    
#   Precision: 0.5922   
#   Recall: 0.5673      
#   F1-Score: 0.5277    
# Classification Report:
#               precision    recall  f1-score   support

#           No       0.64      0.27      0.38       186
#          Yes       0.55      0.85      0.67       193

#     accuracy                           0.57       379
#    macro avg       0.59      0.56      0.53       379
# weighted avg       0.59      0.57      0.53       379

# ------------------------------
# Metrics for gemini_15:
#   Accuracy: 0.6042
#   Precision: 0.6248
#   Recall: 0.6042
#   F1-Score: 0.5829
# Classification Report:
#               precision    recall  f1-score   support

#           No       0.67      0.38      0.48       186
#          Yes       0.58      0.82      0.68       193

#     accuracy                           0.60       379
#    macro avg       0.63      0.60      0.58       379
# weighted avg       0.62      0.60      0.58       379

# ------------------------------
# Metrics for gemini_20:
#   Accuracy: 0.6174
#   Precision: 0.6295
#   Recall: 0.6174
#   F1-Score: 0.6053
# Classification Report:
#               precision    recall  f1-score   support

#           No       0.67      0.44      0.53       186
#          Yes       0.59      0.79      0.68       193

#     accuracy                           0.62       379
#    macro avg       0.63      0.61      0.60       379
# weighted avg       0.63      0.62      0.61       379

# ------------------------------

################################# Irf_belong
# Metrics for gemini15flash8b:
#   Accuracy: 0.6547    
#   Precision: 0.7274   
#   Recall: 0.6547      
#   F1-Score: 0.6022    
# Classification Report:
#               precision    recall  f1-score   support

#           No       0.86      0.27      0.41       472
#          Yes       0.62      0.96      0.76       585

#     accuracy                           0.65      1057
#    macro avg       0.74      0.62      0.58      1057
# weighted avg       0.73      0.65      0.60      1057

# ------------------------------
# Metrics for gemini15flash:
#   Accuracy: 0.7370        
#   Precision: 0.7506       
#   Recall: 0.7370
#   F1-Score: 0.7269        
# Classification Report:    
#               precision    recall  f1-score   support

#           No       0.80      0.54      0.65       472
#          Yes       0.71      0.89      0.79       585

#     accuracy                           0.74      1057
#    macro avg       0.76      0.72      0.72      1057
# weighted avg       0.75      0.74      0.73      1057

# ------------------------------
# Metrics for gemini20flashexp:
#   Accuracy: 0.6887
#   Precision: 0.7151
#   Recall: 0.6887
#   F1-Score: 0.6659
# Classification Report:
#               precision    recall  f1-score   support

#           No       0.78      0.42      0.54       472
#          Yes       0.66      0.91      0.76       585

#     accuracy                           0.69      1057
#    macro avg       0.72      0.66      0.65      1057
# weighted avg       0.72      0.69      0.67      1057

# ------------------------------