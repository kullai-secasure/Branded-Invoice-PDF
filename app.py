from flask import Flask, request, jsonify, send_file
import io

from models.invoice import Invoice, load_invoice
from renderer.pdf import render_invoice_pdf

app = Flask(__name__)


@app.route("/invoices/<invoice_id>/export", methods=["POST"])
def export_invoice(invoice_id):
    invoice = load_invoice(invoice_id, owner=request.user_id)
    if invoice is None:
        return jsonify(error="not found"), 404

    # invoice.html is authored in the browser editor and may include
    # a logo <img> plus custom CSS with url()/@import references
    pdf_bytes = render_invoice_pdf(invoice.html, base_url=invoice.base_url)
    return send_file(io.BytesIO(pdf_bytes), mimetype="application/pdf",
                     download_name=f"{invoice_id}.pdf")


if __name__ == "__main__":
    app.run(port=8080)
