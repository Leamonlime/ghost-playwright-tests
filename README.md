\# ghost-playwright-tests



Automated browser tests for the dashboard of \[Ghost](https://github.com/Leamonlime/ghost), my self-hosted AI assistant. Written in Python with Playwright and pytest.



\## What the tests check



\- The dashboard loads and the page has a title

\- No console errors on load

\- No failed network requests (4xx or 5xx) on load

\- Every internal link returns a good response

\- No sideways scrolling on a phone-sized screen (390 x 844)

\- The root address responds OK

\- The Bills section opens and shows the "Add bill" button and the monthly card



\## Setup



```

python -m venv .venv

.venv\\Scripts\\Activate.ps1

pip install pytest-playwright

playwright install chromium

```



\## Run



The dashboard is on a private network, so its address is read from an environment variable and is not stored in this repo.



```

$env:GHOST\_URL = "https://your-dashboard-address"

pytest -v

```



Add `--headed` to watch the browser.



\## Notes



These tests only run for someone with access to the dashboard.



Next: tests for adding and deleting a bill, and running the suite automatically on each push.

