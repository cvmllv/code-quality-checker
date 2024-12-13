# Code Quality Checker

This project demonstrates a CI pipeline with code quality checks, including linting and static code analysis.

## Features
- **Linting**: Ensures code adheres to Python style guidelines (PEP8) using `flake8`.
- **Static Analysis**: Scans for security vulnerabilities using `bandit`.

## Project Structure
code-quality-checker/
├── .github/
│   └── workflows/
│       └── code-quality.yml
├── main.py
├── requirements.txt
├── README.md

## How to Run Locally
1. Install Python (>= 3.9).
2. Clone the repository:
   ```bash
   git clone https://github.com/cvmllv/code-quality-checker.git
   cd code-quality-checker

pip install -r requirements.txt

python main.py

flake8 .

bandit -r .
