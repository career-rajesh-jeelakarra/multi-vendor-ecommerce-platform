# Database Design

## Definition

Database Design is the process of planning and organizing the database structure before development.

It defines how data is stored, connected, updated, and retrieved efficiently.

---

## Why Database Design?

A good database design helps to:

- Store data efficiently
- Reduce duplicate data
- Maintain data integrity
- Improve performance
- Increase scalability
- Improve security
- Make maintenance easier

---

## Objectives

- Organize project data
- Create relationships between tables
- Reduce redundancy
- Improve query performance
- Support future features

---

## Database Used

MySQL

Reason:

- Open Source
- Fast
- Reliable
- Easy to integrate with Django
- Supports large applications

---

## Database Terminologies

### Table

Stores related information.

Example:

Users

Products

Orders

---

### Row (Record)

One complete entry inside a table.

Example:

User ID = 1

Name = Rajesh

Email = abc@gmail.com

---

### Column (Field)

Represents one attribute.

Example:

id

name

email

password

---

### Primary Key (PK)

Uniquely identifies each record.

Example:

user_id

product_id

order_id

---

### Foreign Key (FK)

Connects one table with another.

Example:

orders.user_id → users.user_id

---

### Relationship Types

One to One

One to Many

Many to Many

---

## Real Time Example

Customer

↓

Places Order

↓

Order contains Products

↓

Payment Completed

↓

Order Delivered

---

## Interview Question

Q. What is Database Design?

Answer:

Database Design is the process of creating tables, relationships, keys and constraints before development so that data can be stored efficiently and securely.

---

## Key Takeaway

A good database design is the foundation of every scalable software application.