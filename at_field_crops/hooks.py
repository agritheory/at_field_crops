# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "at_field_crops"
app_title = "Crops"
app_publisher = "AgriTheory"
app_description = "App for managing standing crops"
app_icon = "assets/at_field_crops/images/aticonwhite.svg"
app_color = "'black'"
app_email = "tyler@agritheory.com"
app_license = "GNU AGPLv3"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/at_field_crops/css/at_field_crops.css"
# app_include_js = "/assets/at_field_crops/js/at_field_crops.js"

# include js, css files in header of web template
# web_include_css = "/assets/at_field_crops/css/at_field_crops.css"
# web_include_js = "/assets/at_field_crops/js/at_field_crops.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}

fixtures = [{"dt":"UOM", "filters": {"uom_name": "Acre"}},
    {"dt":"UOM", "filters": {"uom_name": "Hectare"}},
    {"dt":"UOM", "filters": {"uom_name": "Ounce"}}]

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "at_field_crops.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "at_field_crops.install.before_install"
# after_install = "at_field_crops.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "at_field_crops.notifications.get_notification_config"

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
# 		"at_field_crops.tasks.all"
# 	],
# 	"daily": [
# 		"at_field_crops.tasks.daily"
# 	],
# 	"hourly": [
# 		"at_field_crops.tasks.hourly"
# 	],
# 	"weekly": [
# 		"at_field_crops.tasks.weekly"
# 	]
# 	"monthly": [
# 		"at_field_crops.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "at_field_crops.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "at_field_crops.event.get_events"
# }
