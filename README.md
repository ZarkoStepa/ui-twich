# Twitch UI Automation Framework (Selenium + Pytest)

## Overview

This project demonstrates a scalable and stable UI automation framework for testing Twitch.tv using Selenium and Pytest.

The primary focus is on handling dynamic content (video streaming), minimizing flakiness, and implementing reliable synchronization strategies.

---

## Objectives

- Automate core user flow on Twitch
- Validate that a live stream loads correctly
- Ensure screenshots capture actual rendered video (not blank frames)
- Design a maintainable and extensible test architecture

---

## Test Execution

### Local Run

```bash
pip install -r requirements.txt
pytest -v
```
