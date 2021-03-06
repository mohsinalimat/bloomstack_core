from bloomstack_core.bloomtrace import get_bloomtrace_client
from frappe.utils import get_host_name


def sync_bloomtrace(compliance_settings, method):
	if not compliance_settings.is_compliance_enabled:
		return

	frappe_client = get_bloomtrace_client()
	if not frappe_client:
		return

	site_url = get_host_name()
	frappe_client.update({
		"doctype": "Bloomstack Site",
		"name": site_url
	})

	for company in compliance_settings.company:
		frappe_client.update({
			"doctype": "Bloomstack Company",
			"name": company.company,
			"metrc_push_data": company.push_data,
			"metrc_pull_data": company.pull_data,
			"pull_incoming_transfer": company.pull_incoming_transfer
		})
