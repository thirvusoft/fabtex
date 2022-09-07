import frappe
from frappe.custom.doctype.property_setter.property_setter import make_property_setter
from frappe.custom.doctype.custom_field.custom_field import create_custom_fields

def sales_taxes_charges():
    make_property_setter(
        "Sales Taxes and Charges", "charge_type","options","\nActual\nOn Net Total\nOn Previous Row Amount\nOn Previous Row Total\nOn Item Quantity\nOn Before Previous Row Amount","Text Editor" )