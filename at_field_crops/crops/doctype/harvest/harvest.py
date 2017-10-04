# -*- coding: utf-8 -*-
# Copyright (c) 2017, AgriTheory, LLC and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.model.document import Document


class Harvest(Document):
    def before_insert(self):
        # adds meaningful_name naming series
        name_key = frappe.db.get_value("Planting", self.planting_harvested, "variety") + " Harvest - " + frappe.utils.data.formatdate(self.harvest_date) + " - .###"
        self.meaningful_name = frappe.model.naming.make_autoname(name_key, self, self)

    def validate(self):
        # lookup values
        planting_days_to_maturity = frappe.db.get_value("Planting", self.planting_harvested, "planting_days_to_maturity")
        planting_date = frappe.db.get_value("Planting", self.planting_harvested, "plant_date")
        target_date = frappe.utils.data.add_days(frappe.db.get_value("Planting", self.planting_harvested, "plant_date"), planting_days_to_maturity)

        # calculate the differences between dates
        target_diff = frappe.utils.data.date_diff(target_date, planting_date)
        actual_diff = frappe.utils.data.date_diff(self.harvest_date, planting_date)

        # check to see if harvest is before planting date
        if actual_diff < 0:
            frappe.msgprint("Harvest date cannot be before planting date! %d" % actual_diff)

        # warn if harvest is unreasonably early
        elif actual_diff < (target_diff*0.9):
            frappe.msgprint("Are you sure you want to harvest %d days earlier than expected? (Saved)" % (target_diff - actual_diff))

        # warn if harvest is unreasonably late
        elif actual_diff > (target_diff*1.5):
            frappe.msgprint("Are you sure you want to harvest %d days later than expected? (Saved)" % (actual_diff - target_diff))
        else:
            pass

    def on_update(self):
            # pass harvest crop to stock
            pass_to_stock = frappe.new_doc('Stock Entry')
            pass_to_stock.purpose = "Material Receipt"
            pass_to_stock.append("items", {
                "item_code": self.harvest_as_item,  # lookup?
                "qty": self.crop_yield,
                "uom": self.harvest_uom,
                "stock_uom": self.harvest_uom,
                "conversion_factor": "1",
                "transfer_qty": (self.crop_yield)
            })
            pass_to_stock.company = frappe.db.get_value("Global Defaults", None, "default_company")
            pass_to_stock.to_warehouse = self.harvest_warehouse
            pass_to_stock.date = self.harvest_date
            pass_to_stock.time = frappe.utils.data.nowtime()
            pass_to_stock.save()
