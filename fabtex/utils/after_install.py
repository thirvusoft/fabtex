from fabtex.utils.accounts.sales_invoice import sales_invoice_property_setter


def after_install():
    sales_invoice_property_setter()
