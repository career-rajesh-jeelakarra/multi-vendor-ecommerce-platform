# System Architecture

## Definition

## Why System Architecture?

## Architecture Diagram


```text
                    +----------------------+
                    |      Customer        |
                    +----------+-----------+
                               |
                               |
                    +----------v-----------+
                    |      React Frontend  |
                    +----------+-----------+
                               |
                    REST API (HTTP/HTTPS)
                               |
                    +----------v-----------+
                    | Django REST Backend  |
                    +----------+-----------+
                               |
          +--------------------+--------------------+
          |                    |                    |
          |                    |                    |
+---------v--------+  +--------v--------+  +--------v--------+
| Authentication   |  | Business Logic  |  | Notification    |
| (JWT/Login)      |  | Products/Orders |  | Email/SMS       |
+---------+--------+  +--------+--------+  +--------+--------+
          |                    |                    |
          +--------------------+--------------------+
                               |
                    +----------v-----------+
                    |      MySQL Database  |
                    +----------+-----------+
                               |
          +--------------------+--------------------+
          |                                         |
+---------v--------+                     +----------v---------+
| Payment Gateway  |                     |      Admin Panel   |
+------------------+                     +--------------------+

                               ^
                               |
                     +---------+---------+
                     |      Seller       |
                     +-------------------+
```

## Technology Stack

The Multi-Vendor E-Commerce Platform uses the following technologies:

| Layer | Technology |
|--------|------------|
| Frontend | React.js, HTML5, CSS3, JavaScript, Bootstrap |
| Backend | Python, Django, Django REST Framework |
| Database | MySQL |
| Authentication | Django Authentication, JWT |
| API Testing | Postman |
| Version Control | Git, GitHub |
| Code Editor | Visual Studio Code |
| Web Server | Django Development Server |
| Deployment | Render / AWS / DigitalOcean |

## Modules

The Multi-Vendor E-Commerce Platform is divided into the following major modules:

### Authentication Module
Responsible for user registration, login, logout, password reset, and role-based authentication for customers, sellers, and administrators.

### Customer Module
Handles customer activities such as browsing products, searching, filtering, adding products to cart, placing orders, tracking orders, managing wishlist, and writing reviews.

### Seller Module
Allows sellers to manage their products, inventory, orders, sales reports, and seller dashboard.

### Admin Module
Provides complete control over the platform, including managing customers, sellers, products, categories, orders, reports, and approving seller accounts.

### Payment Module
Handles secure online payment processing, payment verification, payment history, refunds, and transaction management.

### Notification Module
Sends important notifications such as order confirmations, payment updates, shipping updates, promotional offers, and account-related alerts through email or other notification services.

## Data Flow

The Multi-Vendor E-Commerce Platform follows the data flow shown below:

```text
Customer / Seller / Admin
           │
           ▼
     React Frontend
           │
    HTTP / HTTPS Request
           │
           ▼
   Django REST API Backend
           │
           ▼
 Business Logic Processing
           │
           ├──────────────► Authentication
           │
           ├──────────────► Payment Gateway
           │
           ├──────────────► Notification Service
           │
           ▼
      MySQL Database
           │
           ▼
   Response to Frontend
           │
           ▼
Customer / Seller / Admin
```

### Flow Explanation

1. Customer, Seller, or Admin sends a request from the React frontend.
2. The request reaches the Django REST API through HTTP/HTTPS.
3. The backend authenticates the user.
4. Business logic processes the request.
5. The backend communicates with the MySQL database.
6. If required, payment processing and notifications are triggered.
7. The backend sends the response back to the React frontend.
8. The user receives the updated information on the screen.

## Advantages

A well-designed system architecture provides the following benefits:

1. Clear separation between frontend and backend.
2. Easy to maintain and extend the application.
3. Improves code reusability and modularity.
4. Supports multiple user roles such as Customer, Seller, and Admin.
5. Makes debugging and testing easier.
6. Enhances security through authentication and authorization.
7. Supports scalability for future growth.
8. Enables integration with third-party services like payment gateways and email services.
9. Improves overall system performance and reliability.
10. Simplifies deployment and future maintenance.

## Interview Questions


### 1. What is System Architecture?

**Answer:**
System Architecture is the high-level design of a software system that defines how different components interact with each other.

---

### 2. Why is System Architecture important?

**Answer:**
It improves scalability, maintainability, security, performance, and makes development easier.

---

### 3. What are the layers in your project architecture?

**Answer:**
- Frontend (React)
- Backend (Django REST Framework)
- Database (MySQL)
- Authentication (JWT)
- Payment Gateway
- Notification Service

---

### 4. Which architecture are you using?

**Answer:**
Three-Tier Architecture consisting of Presentation Layer, Business Logic Layer, and Data Layer.

---

### 5. How does data flow in your project?

**Answer:**
User → React → REST API → Django Backend → MySQL → Response → React → User.

---

### 6. Why did you choose Django REST Framework?

**Answer:**
Because it simplifies API development, provides security, authentication, serialization, and scalability.

---

### 7. Why React for frontend?

**Answer:**
React provides reusable components, fast rendering, and an excellent user experience.

---

### 8. Why MySQL?

**Answer:**
MySQL is reliable, fast, secure, open-source, and widely used in production applications.

## Real Company Notes


### Industry Best Practices

- Design the system architecture before writing code.
- Keep frontend, backend, and database independent.
- Build reusable and modular components.
- Follow clean coding principles and project structure.
- Secure APIs using authentication and authorization.
- Validate all user inputs on both frontend and backend.
- Use Git and GitHub for version control.
- Document the architecture and APIs before development.
- Keep business logic inside the backend instead of the frontend.
- Plan for scalability so the application can support future growth.

### Architecture Used in Our Project

- Architecture Pattern: Three-Tier Architecture
- Frontend: React.js
- Backend: Django REST Framework
- Database: MySQL
- Authentication: JWT
- API Communication: REST API (HTTP/HTTPS)
- Version Control: Git & GitHub

### Interview Tip

When an interviewer asks, "Explain your project architecture," explain it in this order:

1. Users
2. Frontend (React)
3. REST API
4. Django Backend
5. Business Logic
6. MySQL Database
7. Payment Gateway
8. Notification Service
9. Response back to the user

This is the same flow followed in many real-world web applications.