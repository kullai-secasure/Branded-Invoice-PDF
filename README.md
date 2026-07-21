# Branded-Invoice-PDF

QuillBill lets freelancers design branded invoices and export them as PDFs. The backend renders user-authored invoice HTML to PDF with WeasyPrint on EC2 instances that carry an IAM role. After a previous pentest, the team added SSRF protection that validates every remote asset URL (logo images, CSS url()/@import) before rendering. Review how the validation and the actual asset fetch line up, and decide whether the guard really protects the metadata endpoint.
