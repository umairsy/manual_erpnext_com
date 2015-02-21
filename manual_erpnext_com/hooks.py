from __future__ import unicode_literals
# -*- coding: utf-8 -*-

app_name = "manual_erpnext_com"
app_title = "manual_erpnext_com"
app_publisher = "Frappe"
app_description = "manual.erpnext.com"
app_icon = "icon-globe"
app_color = "blue"
app_email = "info@frappe.io"
app_version = "0.0.1"

website_context = {
	"nav_brand": "The ERPNext Manual",
	"nav_links": [
		("Knowledge Base", "https://kb.erpnext.com")
	]
}


# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/manual_erpnext_com/css/manual_erpnext_com.css"
# app_include_js = "/assets/manual_erpnext_com/js/manual_erpnext_com.js"

# include js, css files in header of web template
# web_include_css = "/assets/manual_erpnext_com/css/manual_erpnext_com.css"
# web_include_js = "/assets/manual_erpnext_com/js/manual_erpnext_com.js"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "manual_erpnext_com.install.before_install"
# after_install = "manual_erpnext_com.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "manual_erpnext_com.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"manual_erpnext_com.tasks.all"
# 	],
# 	"daily": [
# 		"manual_erpnext_com.tasks.daily"
# 	],
# 	"hourly": [
# 		"manual_erpnext_com.tasks.hourly"
# 	],
# 	"weekly": [
# 		"manual_erpnext_com.tasks.weekly"
# 	]
# 	"monthly": [
# 		"manual_erpnext_com.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "manual_erpnext_com.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "manual_erpnext_com.event.get_events"
# }

