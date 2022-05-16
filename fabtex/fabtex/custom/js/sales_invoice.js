frappe.ui.form.on("Sales Invoice",{
	get_gst:function(frm,cdt,cdn){
		frm.set_value("gst","GST")
	}
})