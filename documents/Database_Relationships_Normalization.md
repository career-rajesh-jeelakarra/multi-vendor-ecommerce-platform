# Database Relationships & Normalization

## Definition

Database Relationships define how different tables are connected with each other.

Normalization is the process of organizing data to reduce duplication and improve data integrity.

---

# Why Database Relationships?

Database Relationships help to:

- Connect related tables
- Reduce duplicate data
- Improve data consistency
- Maintain data integrity
- Simplify data retrieval
- Improve database scalability

---

# Relationship Types

## 1. One-to-One (1:1)

Definition:

One record in Table A is related to only one record in Table B.

Example:

Order
↓

Payment

One Order has one Payment.

One Payment belongs to one Order.

---

## 2. One-to-Many (1:N)

Definition:

One record in Table A can have many related records in Table B.

Example:

Vendor
↓

Products

One Vendor can upload many Products.

Every Product belongs to one Vendor.

Another Example:

User
↓

Orders

One User can place many Orders.

---

## 3. Many-to-Many (M:N)

Definition:

Many records in one table can relate to many records in another table.

Example:

Orders

↓

Order Items

↓

Products

One Order contains many Products.

One Product can appear in many Orders.

This relationship is implemented using the Order_Items table.

---

# Normalization

## What is Normalization?

Normalization is the process of organizing database tables to eliminate duplicate data and improve efficiency.

---

## First Normal Form (1NF)

Rules

- Each column contains only one value.
- No repeating groups.
- Every row is unique.

Example

Wrong

Product

Laptop, Mouse

Correct

Laptop

Mouse

---

## Second Normal Form (2NF)

Rules

- Must satisfy 1NF.
- Remove partial dependency.
- Every non-key column depends on the entire primary key.

Example

Move customer information to the Users table instead of repeating it in every Order Item.

---

## Third Normal Form (3NF)

Rules

- Must satisfy 2NF.
- Remove transitive dependency.
- Non-key columns should depend only on the primary key.

Example

Store Category details in the Categories table instead of repeating category names in every Product.

---

# Advantages of Normalization

- Reduces duplicate data.
- Saves storage space.
- Improves data consistency.
- Simplifies maintenance.
- Improves query performance.
- Makes database scalable.

---

# Real-Time Example

Customer

↓

Places Order

↓

Order Items

↓

Products

↓

Payments

↓

Shipping

Every table stores only its own information and connects using Primary Keys and Foreign Keys.

---

# Interview Questions

Q1. What is a Database Relationship?

Answer:

A Database Relationship defines how two or more tables are connected using Primary Keys and Foreign Keys.

---

Q2. What is Normalization?

Answer:

Normalization is the process of organizing data into multiple related tables to eliminate redundancy and improve data integrity.

---

Q3. What are the types of Relationships?

Answer:

- One-to-One
- One-to-Many
- Many-to-Many

---

Q4. What are the Normal Forms?

Answer:

- First Normal Form (1NF)
- Second Normal Form (2NF)
- Third Normal Form (3NF)

---

# Best Practices

- Use Primary Keys for unique identification.
- Use Foreign Keys to maintain relationships.
- Avoid duplicate data.
- Follow at least Third Normal Form (3NF).
- Use meaningful table names.
- Keep relationships simple and maintainable.

---

# Key Takeaway

Database Relationships and Normalization are the foundation of every well-designed database. They help build scalable, maintainable, and efficient software systems by organizing data correctly and reducing redundancy.