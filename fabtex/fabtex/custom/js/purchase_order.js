var tax_category
var tax_and_charges
var main_data
frappe.ui.form.on("Purchase Order",{
	onload:function(frm,cdt,cdn){
		main_data=locals[cdt][cdn]
	}
})
frappe.ui.form.on("Purchase Order Item",{
	item_code:function(frm,cdt,cdn){
		var data = locals[cdt][cdn]
		var item_code=data.item_code
		var transaction_type="Purchase"
		tax_category=main_data.tax_category
		tax_and_charges=main_data.taxes_and_charges
		frappe.call({
			method:"fabtex.fabtex.custom.py.tax.tax_template_filltering",
			args:{item_code,tax_category,tax_and_charges,transaction_type},
			callback(r){
				for(var i=0;i<main_data.items.length;i++){
					if(item_code==main_data.items[i].item_code){
						frappe.model.set_value(main_data.items[i].doctype,main_data.items[i].name,"item_tax_template",r.message)
					}
				}
			}
		})
	}
})