import frappe
from frappe.custom.doctype.property_setter.property_setter import make_property_setter
from frappe.custom.doctype.custom_field.custom_field import create_custom_fields

def delivery_note():
    make_property_setter(
        "Delivery Note", "naming_series","options","\nDN-.####\nMAT-DN-.YYYY.-\nMAT-DN-RET-.YYYY.-","Text Editor" )
    make_property_setter(
        "Delivery Note", "naming_series","default","DN-.####","Text Editor" )