# ER Diagram

## Definition

An ER (Entity Relationship) Diagram is a visual representation of the database structure.

It shows how tables (entities) are connected using relationships.

---

## Why ER Diagram?

A good ER Diagram helps to:

- Understand database structure
- Identify relationships
- Reduce data duplication
- Improve database design
- Make development easier
- Help backend developers

---

## Objectives

- Design database before development
- Identify entities
- Define relationships
- Improve scalability
- Maintain data consistency

---

## Main Entities

- Users
- Vendors
- Categories
- Products
- Product Images
- Orders
- Order Items
- Cart
- Wishlist
- Reviews
- Payments
- Addresses
- Coupons
- Notifications

---

## Relationship Types

### One to One (1:1)

Example:

User → Profile

---

### One to Many (1:N)

Example:

Vendor → Products

Category → Products

User → Orders

Order → Order Items

---

### Many to Many (M:N)

Example:

Products ↔ Orders

(Implemented using Order Items table)

---

## High Level ER Flow

Customer

↓

Registers

↓

Adds Address

↓

Adds Products

↓

Places Order

↓

Payment

↓

Delivery

↓

Review

---

## Real Time Example

Amazon

Users → Orders

Orders → Order Items

Products → Categories

Products → Vendors

Payments → Orders

Reviews → Products

Wishlist → Products

---

## Interview Question

Q. What is an ER Diagram?

Answer:

An ER Diagram is a blueprint of a database that shows entities, attributes and relationships before database implementation.

---

## Key Takeaway

A well-designed ER Diagram is the foundation of a scalable, maintainable and efficient database.