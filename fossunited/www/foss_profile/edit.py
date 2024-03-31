import frappe


def get_context(context):
    context.foss_user = frappe.get_doc(
        "FOSS User Profile",
        {"username": frappe.form_dict["foss_user"]},
    )
