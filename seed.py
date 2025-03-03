#!/usr/bin/env python3
# Script goes here!
from models import Company, Dev, Freebie
import sys
import os

sys.path.append(os.path.abspath(os.path.dirname(__file__)))
from config import session

google = Company(name="Google", founding_year=1998)
microsoft = Company(name="Microsoft", founding_year=1975)

alice = Dev(name="Alice")
bob = Dev(name="Bob")

tshirt = Freebie(item_name="T-Shirt", value=10, dev=alice, company=google)
usb = Freebie(item_name="USB Stick", value=5, dev=bob, company=google)
notebook = Freebie(item_name="Notebook", value=15, dev=alice, company=microsoft)

if not session.query(Dev).first():
    session.add_all([google, microsoft, alice, bob, tshirt, usb, notebook])
    session.commit()
    print("Database seeded successfully!")
else:
    print("Database already has data. Skipping seed process.")