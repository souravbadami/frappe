# Copyright (c) 2017, Frappe and Contributors
# License: GNU General Public License v3. See license.txt

from __future__ import unicode_literals
import frappe

def execute():
	sms_sender_name = frappe.db.get_single_value("SMS Settings", "sms_sender_name")
	if sms_sender_name:
		frappe.reload_doctype("SMS Settings")
		sms_settings = frappe.get_doc("SMS Settings")
		sms_settings.append("parameters", {
			"parameter": "sender_name",
			"value": sms_sender_name
		})
		sms_settings.save()