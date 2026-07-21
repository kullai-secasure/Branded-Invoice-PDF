import logging

from weasyprint import HTML, default_url_fetcher
from validators.url_guard import validate_asset_url

log = logging.getLogger("quillbill.render")


def _guarded_fetcher(url):
    # every remote asset goes through the SSRF allowlist first
    validate_asset_url(url)
    return default_url_fetcher(url)


def render_invoice_pdf(invoice_html, base_url):
    try:
        return HTML(string=invoice_html, base_url=base_url,
                    url_fetcher=_guarded_fetcher).write_pdf()
    except Exception as exc:
        log.warning("asset fetch failed: %s", exc)
        raise
