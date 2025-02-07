# Description

This directory contains scripts for evaluating large language models (LLMs) like Grok and Gemini using few-shot learning. The scripts are designed to:

1.  **Load Data:** Load the specified dataset (validation split) from the `datasets/clean/{dataset_name}/{eval_type}.csv` path.
2.  **Load Examples:** Load few-shot examples from the training split `datasets/clean/{dataset_name}/train.csv`.
3.  **Create Prompts:** Generate prompts for each example in the validation set, including the few-shot examples.  The prompt templates are defined in `prompting/` folder.
4.  **Call LLM:** Call the specified LLM (Grok or Gemini) with the prompt.
5.  **Save Results:** Save the LLM's predictions in a CSV file named `evaluating/{model_type}/{prompt_type}_{eval_model}/{dataset_name}.csv`.

**Arguments:**

*   `--key_number`: The key number to use (API\_KEY{key\_number}).
*   `--dataset_name`: The dataset name (e.g., "SDCNL").
*   `--eval_type`: The subset evaluating on (e.g., "val").
*   `--task_name`: The dataset column task name (e.g., "suicide").
*   `--task_desc`: The full name of the task (e.g., "suicide").
*   `--model_codename`: The model codename to use (e.g., "grok-1", "gemini-2.0-flash-exp").

**Example Usage:**

```bash
python grok_fs.py --key_number 1 --dataset_name SDCNL --eval_type val --task_name suicide --task_desc suicide --model_codename gemini-2.0-flash-exp
```