from fabtex.utils.accounts.sales_invoice import sales_invoice
from fabtex.utils.accounts.purchase_taxes_charges import purchase_taxes_charges
from fabtex.utils.accounts.sales_taxes_charges import sales_taxes_charges
from fabtex.utils.accounts.delivery_note import delivery_note

def after_install():
    sales_invoice()
    purchase_taxes_charges()
    sales_taxes_charges()
    delivery_note()
    
