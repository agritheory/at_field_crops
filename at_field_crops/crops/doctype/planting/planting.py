# -*- coding: utf-8 -*-
# Copyright (c) 2017, AgriTheory and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class Planting(Document):
    def before_insert(self):
        # adds meaningful_name naming series
        name_key = self.variety + " - " + frappe.utils.data.formatdate(self.plant_date) + " - " + self.location + " - .###"
        self.meaningful_name = frappe.model.naming.make_autoname(name_key, self, self)

    def validate(self):
        # brings in variety's days to maturity to hidden field
        self.planting_days_to_maturity = frappe.db.get_value("Crop Variety", self.variety, "days_to_maturity")

        # order seed?
