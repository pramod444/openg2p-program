# Part of OpenG2P. See LICENSE file for full copyright and licensing details.
{
    "name": "OpenG2P Program Payments: In Files",
    "category": "G2P",
    "version": "15.0.1.1.0",
    "sequence": 1,
    "author": "OpenG2P",
    "website": "https://openg2p.org",
    "license": "Other OSI approved licence",
    "development_status": "Alpha",
    "depends": [
        "g2p_programs",
        "g2p_program_documents",
        "mail",
    ],
    "external_dependencies": {
        "python": ["cryptography", "python-jose", "python-barcode", "pdfkit", "qrcode"]
    },
    "data": [
        "security/ir.model.access.csv",
        "views/payment_file_config_view.xml",
    ],
    "assets": {},
    "demo": [],
    "images": [],
    "application": True,
    "installable": True,
    "auto_install": False,
}
