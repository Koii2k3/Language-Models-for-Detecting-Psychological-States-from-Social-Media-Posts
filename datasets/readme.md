# Dataset Overview

This repository contains the datasets used in our research, referencing the main raw datasets from [SteveKGYang/MentalLLaMA](https://github.com/SteveKGYang/MentalLLaMA?tab=readme-ov-file).

The repository is organized into two subfolders:

## 1. `clean`

This folder houses the cleaned and preprocessed datasets prepared for our research.  The data within this folder is ready for immediate use.

*   **`CoTExample`:**  Contains examples of Chain-of-Thought (CoT) prompts employed in our research. This folder includes 2 files:

    *   `generate_cot_example.py` - includes the prompts used to generate the CoT examples.
    *   `gpt_generate_cot_reason.py` - main script to generate the CoT examples.

    The figure below illustrates the pipeline for generating CoT examples.
    <div align="center">
      <img src="images/PipelineCoTExample.png" alt="pipeline CoT example" width="800"/>
    </div>

## 2. `raw`

This folder contains the original, unprocessed datasets downloaded directly from their respective sources.  See below for links to the original datasets and associated papers.

---

## Datasets

The following datasets are included in this repository.  An asterisk (`*`) indicates datasets that were the primary focus of our research.

*   **\* Irf:** [https://github.com/drmuskangarg/Irf](https://github.com/drmuskangarg/Irf) - [Paper](https://aclanthology.org/2023.findings-acl.757.pdf)
*   **\* SDCNL:** [https://github.com/ayaanzhaque/SDCNL](https://github.com/ayaanzhaque/SDCNL)
*   **\* Loneliness:** [https://github.com/sociocom/Japanese-Loneliness-Dataset](https://github.com/sociocom/Japanese-Loneliness-Dataset)
*   **MultiWD:** [https://github.com/drmuskangarg/MultiWD](https://github.com/drmuskangarg/MultiWD) - [Paper](https://www.techrxiv.org/doi/full/10.36227/techrxiv.22816586.v1)
*   **SAD:** [https://github.com/PervasiveWellbeingTech/Stress-Annotated-Dataset-SAD](https://github.com/PervasiveWellbeingTech/Stress-Annotated-Dataset-SAD) - [Paper](https://sensifylab.cis.udel.edu/docs/2021-Mauriello-CHI-StressAnnotatedDataset-Abstract.pdf)
*   **DR:** [https://github.com/Inusette/Identifying-depression](https://github.com/Inusette/Identifying-depression)
*   **CAMS:** [https://github.com/drmuskangarg/CAMS](https://github.com/drmuskangarg/CAMS) - [Paper](https://aclanthology.org/2022.lrec-1.686/)
*   **CSSRS:** [https://github.com/AmanuelF/Suicide-Risk-Assessment-using-Reddit](https://github.com/AmanuelF/Suicide-Risk-Assessment-using-Reddit) - [Paper](https://scholarcommons.sc.edu/cgi/viewcontent.cgi?article=1527&context=aii_fac_pub)

**Note:** This documentation is subject to updates.  Additional datasets and information will be added as needed.