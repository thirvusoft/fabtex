frappe.ui.form.on("Sales Invoice",{
	get_gst:function(frm,cdt,cdn){
		console.log("rgre")
		frm.set_value("gst","GST")
	}
})