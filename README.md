# DevOps API Health Checker

A Python automation tool that checks the health of an API endpoint, handles HTTP and network failures, parses JSON responses, and reports whether the API is healthy or unhealthy.

## Overview

This project was built as part of my Cloud/DevOps learning roadmap.

The goal is to practice using Python for real-world DevOps automation, particularly API monitoring and error handling.

## Features

- Sends HTTP GET requests to an API endpoint
- Checks HTTP response status codes
- Uses `raise_for_status()` to detect unsuccessful HTTP responses
- Parses JSON API responses
- Handles request and network errors
- Reports API health status
- Demonstrates successful and failed API scenarios

## Technologies

- Python 3
- `requests` library
- HTTP APIs
- JSON
- Python exception handling

## Project Structure

```text
devops-api-health-checker/
├── api_health_checker.py
├── api_test.py
├── README.md
└── .gitignore
```

## How It Works

The health checker follows this flow:

```text
API URL
   ↓
requests.get()
   ↓
HTTP response
   ↓
raise_for_status()
   ↓
JSON parsing
   ↓
Health decision
   ↓
HEALTHY / UNHEALTHY
```

## Example — Healthy API

Using:

```text
https://httpbin.org/get
```

Example output:

```text
=================
API HEALTH CHECK
=================
URL: https://httpbin.org/get
Status Code: 200
Health: HEALTHY
```

## Example — Failed API

Using:

```text
https://httpbin.org/status/500
```

Example output:

```text
=================
API HEALTH CHECK
=================
URL: https://httpbin.org/status/500
API request failed
Reason: 500 Server Error
Health: UNHEALTHY
```

## Key Concepts Learned

- HTTP GET requests
- HTTP status codes
- JSON API responses
- `response.status_code`
- `response.text`
- `response.json()`
- `response.raise_for_status()`
- `requests.RequestException`
- `try / except / else`
- Basic service health monitoring

## Installation

Install the required Python package:

```bash
python -m pip install requests
```

## Usage

Run the API health checker:

```bash
python api_health_checker.py
```

Run the basic API test:

```bash
python api_test.py
```

## DevOps Relevance

API health checks are commonly used in automation, monitoring, deployment pipelines, and service validation.

This project demonstrates how Python can communicate with services over HTTP, detect failures, process structured API responses, and make an automated health decision.

## Learning Outcome

This project strengthened my understanding of Python API interaction and error handling and provided practical experience building a simple service health-checking automation tool.