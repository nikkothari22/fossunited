import frappe


def get_context(context):
    context.foss_user = frappe.get_doc(
        "FOSS User Profile", {"user": frappe.session.user}
    )
