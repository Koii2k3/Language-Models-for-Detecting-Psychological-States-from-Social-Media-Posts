#!/bin/bash

# gemini-1.5-flash-8b (gemini-1.5-flash-8b-001)
# gemini-1.5-flash (gemini-1.5-flash-002)
# gemini-2.0-flash-exp (gemini-2.0-flash-exp)
# grok-2-1212


# python .\evaluating\gemini_zscot.py --key_number 1 --dataset_name SDCNL --eval_type val --task_name suicide --task_desc "suicidal intention" --model_codename gemini-2.0-flash-exp
# python .\evaluating\gemini_fscot.py --key_number 2 --dataset_name SDCNL --eval_type val --task_name suicide --task_desc "suicidal intention" --model_codename gemini-1.5-flash-8b
# python .\evaluating\gemini_zscot_reason.py --key_number 3 --dataset_name SDCNL --eval_type val --task_name suicide --task_desc "suicidal intention" --model_codename gemini-2.0-flash-exp
# python .\evaluating\gemini_fscot_reason.py --key_number 4 --dataset_name SDCNL --eval_type val --task_name suicide --task_desc "suicidal intention" --model_codename gemini-2.0-flash-exp

# python .\evaluating\gemini_zscot.py --key_number 5 --dataset_name Irf_belong --eval_type test --task_name belong --task_desc "thwarted belongingness" --model_codename gemini-2.0-flash-exp
# python .\evaluating\gemini_fscot.py --key_number 6 --dataset_name Irf_belong --eval_type test --task_name belong --task_desc "thwarted belongingness" --model_codename gemini-2.0-flash-exp
# python .\evaluating\gemini_zscot_reason.py --key_number 8 --dataset_name Irf_belong --eval_type test --task_name belong --task_desc "thwarted belongingness" --model_codename gemini-2.0-flash-exp
# python .\evaluating\gemini_fscot_reason.py --key_number 7 --dataset_name Irf_belong --eval_type test --task_name belong --task_desc "thwarted belongingness" --model_codename gemini-2.0-flash-exp




# python .\evaluating\grok_zscot.py --key_number 1 --dataset_name Irf_belong --eval_type test --task_name belong --task_desc "thwarted belongingness" --model_codename grok-2-1212
# python .\evaluating\grok_fscot.py --key_number 2 --dataset_name Irf_belong --eval_type test --task_name belong --task_desc "thwarted belongingness" --model_codename grok-2-1212
# python .\evaluating\grok_zscot_reason.py --key_number 1 --dataset_name Irf_belong --eval_type test --task_name belong --task_desc "thwarted belongingness" --model_codename grok-2-1212
python .\evaluating\grok_fscot_reason.py --key_number 2 --dataset_name Irf_belong --eval_type test --task_name belong --task_desc "thwarted belongingness" --model_codename grok-2-1212  # -137

# python .\evaluating\grok_zscot.py --key_number 1 --dataset_name SDCNL --eval_type val --task_name suicide --task_desc "suicidal intention" --model_codename grok-2-1212
# python .\evaluating\grok_fscot.py --key_number 2 --dataset_name SDCNL --eval_type val --task_name suicide --task_desc "suicidal intention" --model_codename grok-2-1212
# python .\evaluating\grok_zscot_reason.py --key_number 1 --dataset_name SDCNL --eval_type val --task_name suicide --task_desc "suicidal intention" --model_codename grok-2-1212
# python .\evaluating\grok_fscot_reason.py --key_number 2 --dataset_name SDCNL --eval_type val --task_name suicide --task_desc "suicidal intention" --model_codename grok-2-1212

