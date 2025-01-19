import pandas as pd
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, classification_report

df = pd.read_csv(r'evaluating\grok\fewshot\Irf_belong.csv') 

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
# Metrics for grok-2-1212:
#   Accuracy: 0.7497
#   Precision: 0.8051
#   Recall: 0.7497
#   F1-Score: 0.7352
# Classification Report:
#               precision    recall  f1-score   support

#           No       0.94      0.52      0.67       346
#          Yes       0.68      0.97      0.80       369

#     accuracy                           0.75       715
#    macro avg       0.81      0.74      0.73       715
# weighted avg       0.81      0.75      0.74       715

# ------------------------------

################################# SDCNL
# Metrics for grok-2-1212:
#   Accuracy: 0.6491
#   Precision: 0.6542
#   Recall: 0.6491
#   F1-Score: 0.6473
# Classification Report:
#               precision    recall  f1-score   support

#           No       0.62      0.73      0.67       186
#          Yes       0.69      0.58      0.63       193

#     accuracy                           0.65       379
#    macro avg       0.65      0.65      0.65       379
# weighted avg       0.65      0.65      0.65       379

# ------------------------------

################################# Irf_belong
# Metrics for grok21212:
#   Accuracy: 0.7162    
#   Precision: 0.7170   
#   Recall: 0.7162      
#   F1-Score: 0.7117    
# Classification Report:
#               precision    recall  f1-score   support

#           No       0.72      0.59      0.65       472
#          Yes       0.71      0.82      0.76       585

#     accuracy                           0.72      1057
#    macro avg       0.72      0.70      0.71      1057
# weighted avg       0.72      0.72      0.71      1057

# ------------------------------