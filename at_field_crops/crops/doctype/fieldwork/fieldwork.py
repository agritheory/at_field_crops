# -*- coding: utf-8 -*-
# Copyright (c) 2017, AgriTheory and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class Fieldwork(Document):
    def before_insert(self):
        # adds meaningful_name naming series
        name_key = self.location + " - " + frappe.utils.data.formatdate(self.fieldwork_date) + " - .###"
        self.meaningful_name = frappe.model.naming.make_autoname(name_key, self, self)

    def validate(self):
        if self.create_todo is True:
            new_todo = frappe.new_doc('ToDo')
            new_todo.status = 'Open'
            new_todo.priority = self.fieldwork_priority
            new_todo.status = self.fieldwork_status
            new_todo.date = self.fieldwork_date
            new_todo.owner = self.user_assigned
            new_todo.description = self.fieldwork_description
            new_todo.reference_type = 'Fieldwork'
            new_todo.role = 'Cultivator'
            new_todo.assigned_by = self.assigned_by
            new_todo.assigned_by_full_name = frappe.utils.get_fullname(self.assigned_by)
            new_todo.save()
        else:
            pass
