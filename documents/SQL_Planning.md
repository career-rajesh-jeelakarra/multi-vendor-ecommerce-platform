# SQL Planning Document

## Purpose

This document contains the SQL planning for the Multi-Vendor E-Commerce Platform. It lists the execution order for database creation, tables, constraints, indexes, sample data, and queries.

---

# Database Creation Order

1. Create Database
2. Use Database
3. Create Users Table
4. Create Categories Table
5. Create Vendors Table
6. Create Products Table
7. Create Inventory Table
8. Create Cart Table
9. Create Wishlist Table
10. Create Orders Table
11. Create Order_Items Table
12. Create Payments Table
13. Create Shipping Table
14. Create Reviews Table
15. Create Coupons Table
16. Create Notifications Table
17. Create Addresses Table

---

# Foreign Key Creation Order

- Products → Categories
- Products → Vendors
- Inventory → Products
- Cart → Users
- Cart → Products
- Wishlist → Users
- Wishlist → Products
- Orders → Users
- Order_Items → Orders
- Order_Items → Products
- Payments → Orders
- Shipping → Orders
- Reviews → Users
- Reviews → Products
- Coupons → Users
- Notifications → Users
- Addresses → Users

---

# Recommended Indexes

- user_id
- product_id
- category_id
- vendor_id
- order_id
- payment_status
- order_status
- created_at

Indexes improve query performance and make searching much faster.

---

# SQL Files Planning

01_create_database.sql

02_users.sql

03_categories.sql

04_vendors.sql

05_products.sql

06_inventory.sql

07_cart.sql

08_wishlist.sql

09_orders.sql

10_order_items.sql

11_payments.sql

12_shipping.sql

13_reviews.sql

14_coupons.sql

15_notifications.sql

16_addresses.sql

17_indexes.sql

18_sample_data.sql

19_views.sql

20_stored_procedures.sql

21_triggers.sql

22_final_queries.sql

---

# Sample Data Planning

Insert sample data for:

- 10 Users
- 5 Categories
- 5 Vendors
- 20 Products
- Inventory Records
- Cart Items
- Wishlist Items
- Orders
- Payments
- Shipping
- Reviews
- Coupons
- Notifications
- Addresses

---

# SQL Features to Implement

- Primary Keys
- Foreign Keys
- Constraints
- Default Values
- Auto Increment
- CHECK Constraints
- Indexes
- Views
- Stored Procedures
- Triggers
- Joins
- Aggregate Functions
- GROUP BY
- HAVING
- Subqueries
- Transactions

---

# Development Order

Phase 1
- Create Database
- Create Tables

Phase 2
- Insert Sample Data

Phase 3
- Test CRUD Operations

Phase 4
- Create Views

Phase 5
- Create Stored Procedures

Phase 6
- Create Triggers

Phase 7
- Performance Optimization

---

# Best Practices

- Use meaningful table names.
- Use Primary Keys in every table.
- Use Foreign Keys for relationships.
- Store only normalized data.
- Avoid duplicate records.
- Use indexes for frequently searched columns.
- Write readable SQL queries.
- Keep backup before altering tables.

---

# Key Takeaway

A proper SQL planning document ensures that database development is organized, scalable, maintainable, and easy to implement without missing dependencies.