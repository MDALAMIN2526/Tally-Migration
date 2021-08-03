from __future__ import unicode_literals

import frappe
import json


@frappe.whitelist()
def customer_group():
    payload = json.loads(frappe.request.data)
    groups = payload['data']

    tally_response = []

    for group in groups:
        group_exists = frappe.db.exists(
            group['doctype'], group['customer_group_name'])
        if not group_exists:
            try:
                doc = frappe.get_doc(group)
                doc.insert()
                tally_response.append(
                    {'name': group['customer_group_name'], 'tally_object': 'Group', 'message': 'Success'})
            except Exception as e:
                tally_response.append(
                    {'name': group['customer_group_name'], 'tally_object': 'Group', 'message': str(e)})
        else:
            try:
                frappe.db.set_value(group['doctype'], group['customer_group_name'], {
                    "customer_group_name": group['customer_group_name'],
                    "is_group": group['is_group'],
                    "parent_customer_group": group['parent_customer_group'],
                })

                tally_response.append(
                    {'name': group['customer_group_name'], 'tally_object': 'Group', 'message': 'Success'})
            except Exception as e:
                tally_response.append(
                    {'name': group['customer_group_name'], 'tally_object': 'Group', 'message': str(e)})

    return {"status": True, 'data': tally_response}


@frappe.whitelist()
def supplier_group():
    payload = json.loads(frappe.request.data)
    groups = payload['data']

    tally_response = []

    for group in groups:
        group_exists = frappe.db.exists(
            group['doctype'], group['supplier_group_name'])
        if not group_exists:
            try:
                doc = frappe.get_doc(group)
                doc.insert()
                tally_response.append(
                    {'name': group['supplier_group_name'], 'tally_object': 'Group', 'message': 'Success'})
            except Exception as e:
                tally_response.append(
                    {'name': group['supplier_group_name'], 'tally_object': 'Group', 'message': str(e)})
        else:
            try:
                frappe.db.set_value(group['doctype'], group['supplier_group_name'], {
                    "supplier_group_name": group['suppiler_group_name'],
                    "is_group": group['is_group'],
                    "parent_supplier_group": group['parent_supplier_group'],
                })

                tally_response.append(
                    {'name': group['supplier_group_name'], 'tally_object': 'Group', 'message': 'Success'})
            except Exception as e:
                tally_response.append(
                    {'name': group['supplier_group_name'], 'tally_object': 'Group', 'message': str(e)})

    return {"status": True, 'data': tally_response}


@frappe.whitelist()
def item_group():
    payload = json.loads(frappe.request.data)
    stockgroups = payload['data']

    tally_response = []

    for stockgroup in stockgroups:
        group_exists = frappe.db.exists(
            stockgroup['doctype'], stockgroup['item_group_name'])
        if not group_exists:
            try:
                doc = frappe.get_doc(stockgroup)
                doc.insert()
                tally_response.append(
                    {'name': stockgroup['item_group_name'], 'tally_object': 'Stock Group', 'message': 'Success'})
            except Exception as e:
                tally_response.append(
                    {'name': stockgroup['item_group_name'], 'tally_object': 'Stock Group', 'message': str(e)})
        else:
            try:
                frappe.db.set_value(stockgroup['doctype'], stockgroup['item_group_name'], {
                    "item_group_name": stockgroup['item_group_name'],
                    "is_group": stockgroup['is_group'],
                    "parent_item_group": stockgroup['parent_item_group'],
                })

                tally_response.append(
                    {'name': stockgroup['item_group_name'], 'tally_object': 'Stock Group', 'message': 'Success'})
            except Exception as e:
                tally_response.append(
                    {'name': stockgroup['item_group_name'], 'tally_object': 'Stock Group', 'message': str(e)})

    return {"status": True, 'data': tally_response}


@frappe.whitelist()
def warehouse():
    payload = json.loads(frappe.request.data)
    warehouses = payload['data']

    tally_response = []

    for warehouse in warehouses:
        is_exists = frappe.db.exists(
            warehouse['doctype'], warehouse['warehouse_name'])
        if not is_exists:
            try:
                doc = frappe.get_doc(warehouse)
                doc.insert()
                tally_response.append(
                    {'name': warehouse['warehouse_name'], 'tally_object': 'Godown', 'message': 'Success'})
            except Exception as e:
                tally_response.append(
                    {'name': warehouse['item_group_name'], 'tally_object': 'Godown', 'message': str(e)})
        else:
            try:
                frappe.db.set_value(warehouse['doctype'], warehouse['warehouse_name'], {
                    "warehouse_name": warehouse['warehouse_name'],
                    "is_group": warehouse['is_group'],
                    "parent_warehouse": warehouse['parent_warehouse'],
                    "company": warehouse['company']
                })

                tally_response.append(
                    {'name': warehouse['warehouse_name'], 'tally_object': 'Godown', 'message': 'Success'})
            except Exception as e:
                tally_response.append(
                    {'name': warehouse['warehouse_name'], 'tally_object': 'Godown', 'message': str(e)})

    return {"status": True, 'data': tally_response}


@frappe.whitelist()
def customer():
    payload = json.loads(frappe.request.data)
    customers = payload['data']

    tally_response = []

    for customer in customers:
        is_exists = frappe.db.exists(
            customer['doctype'], customer['customer_name'])
        if not is_exists:
            try:
                doc = frappe.get_doc(customer)
                doc.insert()

                create_contact(customer)
                create_address(customer)

                tally_response.append(
                    {'name': customer['customer_name'], 'tally_object': 'Ledger', 'message': 'Success'})
            except Exception as e:
                tally_response.append(
                    {'name': customer['customer_name'], 'tally_object': 'Ledger', 'message': str(e)})
        else:
            try:
                frappe.db.set_value(customer['doctype'], customer['customer_name'], {
                    "customer_name": customer['customer_name'],
                    "customer_type": customer['customer_type'],
                    "customer_group": customer['customer_group'],
                    "territory": customer['territory'],
                    "tax_category": customer['tax_category'],
                    "so_required": customer['so_required'],
                    "dn_required": customer['dn_required'],
                    "default_currency": customer['default_currency'],
                    "default_price_list": customer['default_price_list'],
                    "item_group_limit": customer['item_group_limit'] if 'item_group_limit' in customer else ""
                })

                tally_response.append(
                    {'name': customer['customer_name'], 'tally_object': 'Ledger', 'message': 'Success'})
            except Exception as e:
                tally_response.append(
                    {'name': customer['customer_name'], 'tally_object': 'Ledger', 'message': str(e)})

    return {"status": True, 'data': tally_response}


def create_contact(customer):
    try:
        req = {
            "name": customer['ledgercontact'],
            "first_name": customer['ledgercontact'],
            "email_id": customer['email']  if 'email' in customer else "",
            "status": "Passive",
            "phone": customer['ledgermobile'] if 'ledgermobile' in customer else "",
            "mobile_no": customer['ledgermobile'] if 'ledgermobile' in customer else "",
            "is_primary_contact": 1,
            "is_billing_contact": 1,
            "doctype": "Contact",
            "email_ids": [
                {
                    "parent": customer['ledgercontact'],
                    "parentfield": "email_ids",
                    "parenttype": "Contact",
                    "email_id": customer['email'] if 'email' in customer else "a@b.com",
                    "is_primary": 1,
                    "doctype": "Contact Email"
                }
            ],
            "phone_nos": [
                {
                    "parent": customer['ledgercontact'],
                    "parentfield": "phone_nos",
                    "parenttype": "Contact",
                    "phone": customer['ledgermobile'] if 'ledgermobile' in customer else "9999999999",
                    "is_primary_phone": 1,
                    "is_primary_mobile_no": 1,
                    "doctype": "Contact Phone"
                }
            ],
            "links": [
                {
                    "parent": customer['ledgercontact'],
                    "parentfield": "links",
                    "parenttype": "Contact",
                    "link_doctype": "Customer",
                    "link_name": customer['customer_name'],
                    "link_title": customer['customer_name'],
                    "doctype": "Dynamic Link"
                }
            ],
        }

        # print(req)
        doc = frappe.get_doc(req)
        doc.insert()

        # return {'name': customer['customer_name'], 'tally_object': 'Ledger_Contact', 'message': 'Success'}
        print('Success- Contact')
    except Exception as e:
        print(str(e))
        # return {'name': customer['customer_name'], 'tally_object': 'Ledger_Contact', 'message': str(e)}


def create_address(customer):
    try:
        address1 = customer['address1'] if 'address1' in customer else ""
        address2 = customer['address2'] if 'address2' in customer else ""
        address3 = customer['address3'] if 'address3' in customer else ""
        address4 = customer['address4'] if 'address4' in customer else ""

        req = {
            "name": customer['customer_name']+"-Billing",
            "address_title": customer['customer_name'],
            "address_type": "Billing",
            "address_line1": address1 + " " + address2,
            "address_line2": address3 + " " + address4,
            "city": customer['city'] if 'city' in customer else "",
            "state": customer['state'] if 'state' in customer else "",
            "country": customer['country'] if 'country' in customer else "",
            "pincode": customer['pincode'] if 'pincode' in customer else "",
            # "phone": customer['customer_name'],
            "gstin": customer['partygstin'] if 'partygstin' in customer else "",
            "gst_state": customer['state'] if 'state' in customer else "",
            "gst_state_number": customer['state_code'] if 'state_code' in customer else "",
            "tax_category": customer['tax_category'] if 'tax_category' in customer else "",
            "is_primary_address": 1,
            "is_shipping_address": 1,
            "doctype": "Address",
            "links": [
                {
                    "parent": customer['customer_name']+"-Billing",
                    "parentfield": "links",
                    "parenttype": "Address",
                    "link_doctype": "Customer",
                    "link_name": customer['customer_name'],
                    "link_title": customer['customer_name'],
                    "doctype": "Dynamic Link"
                }
            ]
        }
        # print(req)
        doc = frappe.get_doc(req)
        doc.insert()

        print('Success- Address') # return {'name': customer['customer_name'], 'tally_object': 'Ledger_Address', 'message': 'Success'}
    except Exception as e:
        print(str(e))
        # return {'name': customer['customer_name'], 'tally_object': 'Ledger_Address', 'message': str(e)}