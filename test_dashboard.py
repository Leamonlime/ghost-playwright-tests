import os
import re
from playwright.sync_api import Page, expect

URL = os.environ["GHOST_URL"].rstrip("/")


def test_dashboard_loads(page: Page):
    page.goto(URL)
    expect(page).to_have_title(re.compile(".+"))


def test_no_console_errors_on_load(page: Page):
    errors = []
    page.on("console", lambda m: errors.append(m.text) if m.type == "error" else None)
    page.goto(URL)
    page.wait_for_load_state("networkidle")
    assert errors == [], f"Console errors: {errors}"


def test_no_failed_requests_on_load(page: Page):
    failed = []
    page.on("response", lambda r: failed.append(f"{r.status} {r.url}") if r.status >= 400 else None)
    page.goto(URL)
    page.wait_for_load_state("networkidle")
    assert failed == [], f"Failed requests: {failed}"


def test_internal_links_work(page: Page):
    page.goto(URL)
    hrefs = page.eval_on_selector_all("a[href]", "els => els.map(e => e.href)")
    internal = sorted({h.split("#")[0] for h in hrefs if h.startswith(URL)})
    assert internal, "No internal links found"
    for link in internal:
        response = page.goto(link)
        assert response is not None and response.status < 400, f"Bad response for {link}"


def test_no_sideways_scroll_on_phone(page: Page):
    page.set_viewport_size({"width": 390, "height": 844})
    page.goto(URL)
    page.wait_for_load_state("networkidle")
    overflow = page.evaluate("document.documentElement.scrollWidth > window.innerWidth")
    assert not overflow, "Page scrolls sideways on a phone-sized screen"


def test_root_responds_ok(page: Page):
    assert page.request.get(URL).ok

def test_bills_section_visible(page: Page):
    page.goto(URL)
    page.get_by_role("link", name="▤ Bills").click()
    expect(page.get_by_role("button", name="+ Add bill").first).to_be_visible()
    expect(page.locator("#cMonthly")).to_be_visible()