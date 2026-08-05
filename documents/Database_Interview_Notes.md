# Database Interview Notes

## Introduction

This document contains important database interview questions, answers, SQL concepts, normalization, keys, constraints, indexing, joins, and best practices. It is useful for interviews and real-world project development.

---

# Database Basics

### What is a Database?

A database is an organized collection of related data that allows efficient storage, retrieval, updating, and management.

---

### What is DBMS?

A Database Management System (DBMS) is software used to create, manage, and manipulate databases.

Examples:

- MySQL
- PostgreSQL
- Oracle
- SQL Server
- SQLite

---

### What is SQL?

SQL (Structured Query Language) is the standard language used to communicate with relational databases.

---

# Primary Key

- Uniquely identifies each row.
- Cannot contain NULL values.
- Must be unique.
- One Primary Key per table.

Example:

Users.user_id

---

# Foreign Key

- Connects two tables.
- Maintains referential integrity.
- Prevents invalid references.

Example:

Orders.user_id → Users.user_id

---

# Candidate Key

A column that can uniquely identify a record.

Example:

Email

Phone Number

---

# Alternate Key

Candidate keys that are not selected as the Primary Key.

---

# Composite Key

A key made using two or more columns.

Example:

order_id + product_id

---

# Unique Key

- Prevents duplicate values.
- Allows NULL (depending on DBMS).

---

# Constraints

- PRIMARY KEY
- FOREIGN KEY
- UNIQUE
- NOT NULL
- CHECK
- DEFAULT

---

# Normalization

Normalization reduces data redundancy and improves consistency.

---

## First Normal Form (1NF)

- Atomic values
- No repeating groups

---

## Second Normal Form (2NF)

- Must satisfy 1NF
- Remove partial dependency

---

## Third Normal Form (3NF)

- Must satisfy 2NF
- Remove transitive dependency

---

# Relationships

### One-to-One

Example:

User → User Profile

---

### One-to-Many

Example:

User → Orders

---

### Many-to-Many

Example:

Orders ↔ Products

Implemented using Order_Items.

---

# SQL Joins

## INNER JOIN

Returns matching records.

---

## LEFT JOIN

Returns all left table records.

---

## RIGHT JOIN

Returns all right table records.

---

## FULL JOIN

Returns all matching and non-matching records.

---

# Indexes

Indexes improve query performance by reducing search time.

Common columns:

- user_id
- product_id
- order_id
- created_at

---

# Views

A View is a virtual table created from one or more SQL queries.

Advantages:

- Security
- Reusability
- Simplicity

---

# Stored Procedures

Reusable SQL programs stored inside the database.

Advantages:

- Faster execution
- Reusable
- Better security

---

# Triggers

Triggers execute automatically when an INSERT, UPDATE, or DELETE occurs.

Uses:

- Audit logs
- Inventory updates
- Notifications

---

# Transactions

Transaction Properties (ACID)

- Atomicity
- Consistency
- Isolation
- Durability

---

# Database Optimization

- Use indexes.
- Avoid duplicate data.
- Normalize tables.
- Write optimized queries.
- Avoid unnecessary joins.
- Select only required columns.
- Use proper constraints.

---

# Frequently Asked Interview Questions

### Q1. Difference between Primary Key and Foreign Key?

Answer:

Primary Key uniquely identifies a record.

Foreign Key connects two related tables.

---

### Q2. What is Normalization?

Answer:

Normalization is the process of reducing duplicate data and organizing tables efficiently.

---

### Q3. What is Denormalization?

Answer:

Combining tables to improve read performance by reducing joins.

---

### Q4. What is a Join?

Answer:

A Join combines data from multiple related tables.

---

### Q5. Why do we use Indexes?

Answer:

Indexes improve query speed.

---

### Q6. Difference between DELETE, TRUNCATE and DROP?

DELETE

- Removes selected rows.
- Can use WHERE.
- Can rollback.

TRUNCATE

- Removes all rows.
- Faster.
- Cannot remove individual rows.

DROP

- Deletes the entire table.

---

### Q7. What is ACID?

Answer:

Atomicity

Consistency

Isolation

Durability

---

### Q8. What is a View?

Answer:

A virtual table created using SQL queries.

---

### Q9. What is a Trigger?

Answer:

A database object that executes automatically after specific events.

---

### Q10. What is a Stored Procedure?

Answer:

A reusable SQL program stored inside the database.

---

# Best Practices

- Always use Primary Keys.
- Use Foreign Keys for relationships.
- Normalize databases.
- Create indexes on frequently searched columns.
- Use meaningful table names.
- Keep backups before major changes.
- Avoid duplicate data.
- Write readable SQL queries.

---

# Key Takeaway

Strong database fundamentals, normalization, relationships, SQL optimization, and interview preparation are essential for building scalable applications and succeeding in software developer interviews.