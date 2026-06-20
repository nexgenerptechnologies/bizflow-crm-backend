import frappe
from frappe.modules.import_file import import_files

def after_migrate():
    # Forcefully create the Module Def if it didn't get created during install
    if not frappe.db.exists("Module Def", "BizFlow CRM Backend"):
        frappe.get_doc({
            "doctype": "Module Def",
            "module_name": "BizFlow CRM Backend",
            "app_name": "bizflow_crm_backend",
            "custom": 0
        }).insert(ignore_permissions=True)
        frappe.db.commit()
    
    # Forcefully sync the doctypes
    try:
        import_files(app="bizflow_crm_backend")
    except Exception as e:
        frappe.log_error(title="BizFlow Sync Error", message=str(e))