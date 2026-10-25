# ghost-playwright-tests

[![Playwright tests](https://github.com/Leamonlime/ghost-playwright-tests/actions/workflows/tests.yml/badge.svg)](https://github.com/Leamonlime/ghost-playwright-tests/actions/workflows/tests.yml)

Automated browser tests for the dashboard of [Ghost](https://github.com/Leamonlime/ghost), my self-hosted AI assistant. Written in Python with Playwright and pytest.

## What the tests check

- The dashboard loads and the page has a title
- No console errors on load
- No failed network requests (4xx or 5xx) on load
- Every internal link returns a good response
- No sideways scrolling on a phone-sized screen (390 x 844)
- The root address responds OK
- The Bills section opens and shows the "Add bill" button and the monthly card

## Setup

```
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install pytest-playwright
playwright install chromium
```

## Run

The dashboard is on a private network, so its address is read from an environment variable and is not stored in this repo.

```
$env:GHOST_URL = "https://your-dashboard-address"
pytest -v
```

Add `--headed` to watch the browser.

## Continuous integration

The suite runs on GitHub Actions on every push to `main`, and can be started by hand from the Actions tab. The run joins the private network for the length of the job, runs the tests in headless Chromium, and uploads Playwright traces if any test fails.

## Next

Tests for adding and deleting a bill.
