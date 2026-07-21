import os
import json
from dataclasses import dataclass

INVOICE_DIR = os.environ.get("INVOICE_DIR", "/var/lib/quillbill/invoices")


@dataclass
class Invoice:
    id: str
    owner: str
    html: str
    base_url: str


def load_invoice(invoice_id, owner):
    path = os.path.join(INVOICE_DIR, f"{invoice_id}.json")
    if not os.path.isfile(path):
        return None
    with open(path) as fh:
        data = json.load(fh)
    if data.get("owner") != owner:
        return None
    return Invoice(id=invoice_id, owner=data["owner"],
                   html=data["html"], base_url=data.get("base_url", ""))
