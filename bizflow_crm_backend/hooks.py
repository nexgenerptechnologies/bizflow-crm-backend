app_name = "bizflow_crm_backend"
app_title = "BizFlow CRM Backend"
app_publisher = "Nexgen ERP Technologies"
app_description = "Lightweight CRM and ERP features for the Indian market."
app_email = "admin@example.com"
app_license = "mit"

after_migrate = "bizflow_crm_backend.setup.after_migrate"


custom_fields = {
    'User': [
        {
            'fieldname': 'bizflow_tenant',
            'label': 'BizFlow Tenant',
            'fieldtype': 'Link',
            'options': 'BizFlow Tenant',
            'insert_after': 'email'
        }
    ]
}
