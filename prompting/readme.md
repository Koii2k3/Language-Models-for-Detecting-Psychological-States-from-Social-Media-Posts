# Prompt Templates for Mental Health Assessment

This directory contains Python scripts defining prompt templates used to guide Large Language Models (LLMs) in performing mental health assessments on text data (e.g., social media posts).  These templates are designed to provide the LLM with context, instructions, and a structured approach for classifying text according to specific psychological criteria. The scripts use prompt engineering techniques such as Zero-shot, Few-shot, Chain-of-Thought (CoT), and CoT Reasoning.

## Script Descriptions

Each script contains one or more prompt templates, typically focused on a specific mental health assessment task (e.g., stress assessment, suicide risk assessment, thwarted belongingness assessment).  The templates are designed to be easily customizable and reusable with different LLMs.

## Common Template Structure

All prompt templates share a similar structure:

1.  **Context:** Sets the stage by defining the LLM's role.
2.  **Instructions:** Provides clear instructions on how to classify the text data, emphasizing basing the decision on the explicit content of the post and avoiding assumptions.
4.  **Enhancement:**  Provides a placeholder for adding additional examples to the prompt..
5.  **Post for Classification:** Specifies the text data that the LLM should classify.
6.  **Output Format:** Defines the desired output format.