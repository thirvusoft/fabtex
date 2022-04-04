import frappe
@frappe.whitelist()
def tax_template_filltering(item_code,tax_category,tax_and_charges,transaction_type):
	separate_item_tax=[]
	total_item_tax=[]
	total_tax_category=[]
	item_data=frappe.get_doc("Item",item_code)
	total_item_tax_details=item_data.__dict__["taxes"]
	for i in range(0,len(total_item_tax_details),1):
		total_item_tax.append(total_item_tax_details[i].__dict__["item_tax_template"])
		total_tax_category.append(total_item_tax_details[i].__dict__["tax_category"])
	for i in range(0,len(total_item_tax),1):
		if(total_tax_category[i]==tax_category):
			separate_item_tax.append(total_item_tax[i])
	for item_tax_name in separate_item_tax:
		tax_details=frappe.get_doc("Item Tax Template",item_tax_name)
		if(tax_details.__dict__["transaction_type"]==transaction_type):
			break
	return item_tax_name