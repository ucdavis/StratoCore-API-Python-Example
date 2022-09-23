#!/usr/bin/env python

"""Example code on how to use the 'pyppms' package."""

# pylint: disable-msg=multiple-imports
# pylint: disable-msg=wrong-import-order

import datetime
import pyppms, pyppmsconf


conn = pyppms.ppms.PpmsConnection(
    url=pyppmsconf.PUMAPI_URL,
    api_key=pyppmsconf.PUMAPI_KEY,
    timeout=pyppmsconf.TIMEOUT,
)

# get all users -- this takes way longer than you'd think:
#users = conn.get_users()
#print(users)
#print("got users")

#get admins:
#admins = conn.get_admins()
#print("got admins")

#invoices = conn.get_invoice_list()
#print("got invoices")
#for invoice in invoices:
    #print(invoice.invoiceid)
    #print(invoice.details)

#serviceid, login, quantity, project=None, accepted, completed
#create new order:
# conn.new_order(
   # "2497",
   # "username",
   # "5",
   # None,
   # "true",
   # "true"
# )
# print("new order")

#get all orders
#orders = conn.get_order_list()
#for order in orders:
   #print(order.details)

# get all groups:
# groups = conn.get_groups()
# print("got groups")

# get details on the first group:
# conn.get_group(groups[0])
# print("got group 0")

# get all users of that group:
# conn.get_group_users(groups[0])
# print("got group users")


# get all systems:
# systems = conn.get_systems()

# show system IDs:
# print(systems.keys())

# show details on the first system:
# details = systems[list(systems.keys())[0]]
# print(details)


# get the currently running booking for system 39 (can be empty):
# cur = conn.get_booking(39)
# print(cur)

# get the next booking for system 39 (can be empty):
# next_booking = conn.get_next_booking(39)
# print(next_booking)

# get the running sheet for today (includes bookings for ALL systems!):
# conn.get_running_sheet(2, datetime.datetime.now())


# get the user experience (permissions):
# conn.get_user_experience(login=list(users.keys())[0])

# get permissions for system 39:
# conn.get_user_experience(system_id=39)

# create new users:
# conn.new_user(
    # "pyppms",
    # "Python",
    # "PumAPI",
    # "pyppms@python-facility.example",
    # "pyppms_group",
    # phone="+98 (76) 54 3210",
# )

# conn.new_user(
    # "pyppms-adm",
    # "Python",
    # "PumAPI (Administrator)",
    # "pyppms-adm@python-facility.example",
    # "pyppms_group",
    # phone="+98 (76) 54 3112",
# )
