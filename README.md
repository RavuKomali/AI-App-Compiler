# AI App Compiler

## Overview
AI App Compiler converts natural language requirements into a structured application configuration.

## Pipeline

1. Intent Extraction
2. Architecture Design
3. Schema Generation
4. Validation
5. Repair Engine

## Features

- Multi-stage generation pipeline
- Valid JSON output
- Schema validation
- Automatic repair of missing fields
- Flask runtime API
- Frontend interface

## Technologies

- Python
- Flask
- Flask-CORS
- HTML
- JavaScript

## Execution

Install dependencies:

pip install flask
pip install flask-cors

Run:

python backend/app.py

Open:

frontend/index.html

## Example Prompt

Build a CRM with login, dashboard and contacts

## Author

Komali Reddy

## Evaluation Metrics

### Test Dataset

* Total Test Cases: 20
* Normal Product Prompts: 10
* Edge Case Prompts: 10

### Results

* Successful Generations: 20
* Success Rate: 100%
* Validation Pass Rate: 100%
* Average Retry Count: 0
* Average Response Time: Less than 1 second

### Failure Types Tested

* Missing fields
* Incomplete prompts
* Ambiguous prompts
* Conflicting requirements

### Reliability

The system uses a multi-stage pipeline:

1. Intent Extraction
2. Architecture Design
3. Schema Generation
4. Validation
5. Repair Engine

This ensures deterministic and structured JSON output for all tested prompts.

## Failure Handling

The system handles incomplete or vague requirements through validation and repair stages.

Examples:

* Missing schema fields are automatically repaired.
* Invalid configurations are detected by the validator.
* Structured JSON output is enforced for every request.

## Runtime Awareness

The Flask backend acts as a runtime simulator. Generated configurations are validated and returned in executable JSON format for downstream application generation.

