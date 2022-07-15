import frappe
from frappe.custom.doctype.property_setter.property_setter import make_property_setter
from frappe.custom.doctype.custom_field.custom_field import create_custom_fields

def sales_invoice():
    sales_invoice_property_setter()
    sales_invoice_custom_field()

def sales_invoice_property_setter():

    prop = make_property_setter(
        "Sales Invoice", "einvoice_section", "hidden", 0, "Check")
    frappe.db.commit()

def sales_invoice_custom_field():
    custom_fields={
        "Sales Invoice":[
            dict(fieldname='e_way_bill', label='E-Way Bill',
                fieldtype='Section Break', insert_after='ts_tax_breakup_gst_table'),
            dict(fieldname='e_way_bill_number', label='E-Way Bill Number',
                fieldtype='Int', insert_after='e_way_bill'),
            dict(fieldname='ts_mode_of_transport', label='Mode of Transport',
                fieldtype='Select', insert_after='e_way_bill_number', options="Road\nShip\nRail\nAir"),
            dict(fieldname='transporter_name_', label='Transporter Name',
                fieldtype='Data', insert_after='ts_mode_of_transport'),
            dict(fieldname='transporter_id', label='Transporter ID',
                fieldtype='Int', insert_after='transporter_name_'),
            dict(fieldname='column_break_00', label='',
                fieldtype='Column Break', insert_after='transporter_id'),
            dict(fieldname='vehicle_number', label='Vehicle Number',
                fieldtype='Link', insert_after='column_break_00', options="Vehicle"),
            dict(fieldname='ts_distance', label='Distance',
                fieldtype='Float', insert_after='vehicle_number'),
            dict(fieldname='vehicle_type', label='Vehicle Type',
                fieldtype='Data', insert_after='ts_distance'),
        ],
    }
    create_custom_fields(custom_fields)
