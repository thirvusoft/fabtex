import frappe
from frappe.custom.doctype.property_setter.property_setter import make_property_setter


def sales_invoice_property_setter():
    make_property_setter("Sales Invoice", "einvoice_section", "hidden", 0, "Check")