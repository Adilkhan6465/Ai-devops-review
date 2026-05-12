# AI DevOps Review Platform

A multi-model AI-powered DevOps automation platform that performs intelligent code reviews, security scanning, risk prediction, infrastructure generation, log analysis, test generation, and incident alerting using OpenAI, Claude, and Gemini models with automatic fallback support.

---

## Features

### AI Pull Request Review

- Reviews GitHub pull requests automatically
- Detects bugs, security risks, and improvements
- Generates structured review comments
- Blocks pipeline for critical/high severity issues

### Multi-Model AI Fallback

Supports:

- OpenAI GPT-4o
- Claude Sonnet
- Gemini Flash

If one provider fails, the system automatically switches to the next available provider.

### Security Scanner

- Detects:
  - Hardcoded secrets
  - API keys
  - SQL injection risks
  - XSS vulnerabilities
  - OWASP Top 10 issues

### Deployment Risk Predictor

Predicts:

- Risk score
- Risk level
- Rollback strategy
- Safe deployment timing

### Terraform Generator

Generates production-ready Terraform infrastructure code automatically.

### AI Test Generator

Creates:

- Pytest unit tests
- Edge case tests
- Error handling tests

### Log Analyzer

Analyzes application logs and detects:

- Root causes
- Failures
- Recommended fixes

### Slack Incident Alerts

Generates AI-powered DevOps incident alerts for monitoring systems.

---

## Project Structure

```text
ai-devops-review/
│
├── .github/
│   └── workflows/
│       └── ai-devops.yml
│
├── scripts/
│   ├── common/
│   │   └── ai_client.py
│   │
│   ├── review/
│   │   ├── ai_review.py
│   │   └── providers/
│   │       ├── openai_provider.py
│   │       ├── claude_provider.py
│   │       ├── gemini_provider.py
│   │       ├── fallback_provider.py
│   │       └── prompts.py
│   │
│   ├── monitoring/
│   │   ├── log_analyzer.py
│   │   └── slack_alert.py
│   │
│   ├── testing/
│   │   └── test_generator.py
│   │
│   ├── infrastructure/
│   │   ├── terraform_generator.py
│   │   └── risk_predictor.py
│   │
│   └── security/
│       └── security_scanner.py
│
├── generated/
│
├── logs/
│
├── requirements.txt
├── diff.txt
├── .env
└── README.md
```

---

## Installation

### Clone Repository

```bash
git clone <your-repo-url>
cd ai-devops-review
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### requirements.txt

```bash
openai>=1.0.0
anthropic
google-genai
requests
python-dotenv
```

### Environment Variables

Creat a .env file:

```bash
OPENAI_API_KEY=your_openai_key
ANTHROPIC_API_KEY=your_claude_key
GEMINI_API_KEY=your_gemini_key
SLACK_WEBHOOK=your_slack_webhook
```

You can use one provider or multiple providers.

## Running Modules

### AI Review

```bash
python -m scripts.review.ai_review
```

### Security Scanner

```bash
python -m scripts.security.security_scanner
```

### Terraform Generator

```bash
python -m scripts.infrastructure.terraform_generator
```

### Deployment Risk Predictor

```bash
python -m scripts.infrastructure.risk_predictor
```

### Test Generator

```bash
python -m scripts.testing.test_generator
```

### Log Analyzer

```bash
python -m scripts.monitoring.log_analyzer
```

### Slack Alert Generator

```bash
python -m scripts.monitoring.slack_alert
```

## GitHub Actions Integration

The platform includes GitHub Actions CI/CD integration.

**Workflow:**

1. Detects pull request changes
2. Generates code diff
3. Sends diff to AI review engine
4. Posts AI review comment automatically
5. Blocks pipeline on critical issues

## Example AI Review Output

```bash
## AI Code Review ✅

Verdict: PASS
Score: 8/10
Severity: medium

### Summary
Code structure is clean but contains potential security risks.

### Bugs Found
- Missing error handling
- Potential null reference

### Security Risks
- Hardcoded API key

### Improvements
- Add validation
- Improve logging
```

## Architecture

```bash
GitHub PR
    ↓
GitHub Actions
    ↓
AI Review Engine
    ↓
Fallback Provider Layer
    ↓
OpenAI / Claude / Gemini
    ↓
Generated Reports
```

## Generated Outputs

The system automatically generates:

- generated/review.txt
- generated/security_report.txt
- generated/risk_report.json
- generated/main.tf
- generated/generated_tests.py
- generated/log_report.txt

## Tech Stack

- Python
- GitHub Actions
- OpenAI API
- Claude API
- Gemini API
- Terraform
- DevOps Automation

## Future Improvements

- Kubernetes deployment analysis
- Dockerfile optimization
- Jira integration
- AI observability dashboard
- Vector database memory
- RAG-based incident analysis

## License

This project is licensed under the MIT Licence.
