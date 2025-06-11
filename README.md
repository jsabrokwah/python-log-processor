# Python Log Processor

A collection of Python scripts for analyzing and extracting insights from Node.js application logs.

## Overview

This project provides various utilities to process and analyze log files from a Node.js application. It can extract information about request patterns, user agents, endpoints, and IP addresses.

## Features

- Count requests per user agent and operating system
- Track requests per IP address within 10-second windows
- Monitor requests per endpoint
- Analyze requests in consecutive 10-second windows
- Helper utilities for IP validation and log sorting

## Scripts

### 1. `request_per_user_agent.py`

Categorizes and counts HTTP requests by user agent and operating system.

```
python request_per_user_agent.py
```

### 2. `request_per_10_sec.py`

Counts how many requests each IP address makes within a 10-second window.

```
python request_per_10_sec.py
```

### 3. `request_per_endpoint.py`

Analyzes which endpoints are being accessed and how frequently.

```
python request_per_endpoint.py
```

### 4. `helper.py`

Provides utility functions for:
- IP address validation
- Sorting log lines by timestamp

## Requirements

- Python 3.6+
- Required packages are listed in `requirements.txt`

## Setup

1. Clone the repository
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Ensure your log file is named `NodeJsApp.log` and placed in the project root directory
4. Run the desired script
