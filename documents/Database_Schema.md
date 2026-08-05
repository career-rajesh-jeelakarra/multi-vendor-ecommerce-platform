# Database Schema

## Table 1: Users

### Purpose

Stores customer and admin account information.

---

### Fields

| Field Name | Data Type | Constraint | Description |
|------------|-----------|------------|-------------|
| user_id | BIGINT | Primary Key, Auto Increment | Unique user ID |
| first_name | VARCHAR(100) | NOT NULL | User first name |
| last_name | VARCHAR(100) | NOT NULL | User last name |
| email | VARCHAR(255) | UNIQUE, NOT NULL | User email |
| phone | VARCHAR(15) | UNIQUE | Mobile number |
| password | VARCHAR(255) | NOT NULL | Encrypted password |
| role | ENUM('Customer','Admin') | DEFAULT 'Customer' | User role |
| status | ENUM('Active','Inactive','Blocked') | DEFAULT 'Active' | Account status |
| created_at | TIMESTAMP | DEFAULT CURRENT_TIMESTAMP | Created date |
| updated_at | TIMESTAMP | DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP | Last updated date |

---

### Primary Key

- user_id

---

### Relationships

- One User can place many Orders.
- One User can have multiple Addresses.
- One User can create multiple Reviews.
- One User can have one Wishlist.
- One User can have one Cart.

---

### Business Rules

- Email must be unique.
- Phone number should be unique.
- Password must be stored in encrypted format.
- Admin and Customer are stored in the same table.

---

### Real-Time Example

Rajesh creates an account using his email and password.

The system stores his details in the Users table.

Later he logs in, places orders, writes reviews, and manages his profile using this record.

---

### Interview Question

Q. Why is email usually marked as UNIQUE?

Answer:

Because every user account must have a unique login identity.

---

### Key Takeaway

The Users table is the foundation of authentication and customer management in an E-Commerce application.


## Table 2: Vendors

### Purpose

Stores vendor (seller) account information for the Multi-Vendor E-Commerce Platform.

---

### Fields

| Field Name | Data Type | Constraint | Description |
|------------|-----------|------------|-------------|
| vendor_id | BIGINT | Primary Key, Auto Increment | Unique vendor ID |
| business_name | VARCHAR(255) | NOT NULL | Vendor business name |
| owner_name | VARCHAR(255) | NOT NULL | Vendor owner name |
| email | VARCHAR(255) | UNIQUE, NOT NULL | Vendor email |
| phone | VARCHAR(15) | UNIQUE | Vendor phone number |
| password | VARCHAR(255) | NOT NULL | Encrypted password |
| gst_number | VARCHAR(30) | UNIQUE | GST registration number |
| address | TEXT | NOT NULL | Business address |
| status | ENUM('Pending','Approved','Rejected','Blocked') | DEFAULT 'Pending' | Vendor account status |
| created_at | TIMESTAMP | DEFAULT CURRENT_TIMESTAMP | Created date |
| updated_at | TIMESTAMP | DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP | Last updated date |

---

### Primary Key

- vendor_id

---

### Relationships

- One Vendor can add many Products.
- One Vendor receives many Orders through their Products.
- One Vendor can have multiple Product Images.

---

### Business Rules

- Email must be unique.
- GST Number should be unique.
- Password must be stored in encrypted format.
- Vendor account must be approved before selling products.

---

### Real-Time Example

ABC Fashion Store registers as a vendor.

After admin approval, the vendor logs in and uploads products for customers to purchase.

---

### Interview Question

Q. Why do we keep Vendors in a separate table instead of the Users table?

Answer:

Because vendors have business-specific information like GST number, business name, approval status, and product management, which are different from normal customer details.

---

### Key Takeaway

The Vendors table manages seller accounts and is the core of every Multi-Vendor E-Commerce platform.


## Table 3: Categories

### Purpose

Stores product categories used to organize products for easy browsing and searching.

---

### Fields

| Field Name | Data Type | Constraint | Description |
|------------|-----------|------------|-------------|
| category_id | BIGINT | Primary Key, Auto Increment | Unique category ID |
| category_name | VARCHAR(150) | UNIQUE, NOT NULL | Category name |
| description | TEXT | NULL | Category description |
| image | VARCHAR(255) | NULL | Category image |
| status | ENUM('Active','Inactive') | DEFAULT 'Active' | Category status |
| created_at | TIMESTAMP | DEFAULT CURRENT_TIMESTAMP | Created date |
| updated_at | TIMESTAMP | DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP | Last updated date |

---

### Primary Key

- category_id

---

### Relationships

- One Category can contain many Products.
- Every Product belongs to one Category.

---

### Business Rules

- Category name must be unique.
- Only active categories should be visible to customers.
- A category cannot be deleted if products are assigned to it.

---

### Real-Time Example

An admin creates categories like Electronics, Fashion, Home Appliances, and Books.

Customers browse products using these categories.

---

### Interview Question

Q. Why do we use a separate Categories table?

Answer:

Because it organizes products into groups, improves searching and filtering, and avoids repeating category names for every product.

---

### Key Takeaway

The Categories table keeps products organized and makes navigation easier for both customers and administrators.


## Table 4: Products

### Purpose

Stores all product information uploaded by vendors for customers to browse and purchase.

---

### Fields

| Field Name | Data Type | Constraint | Description |
|------------|-----------|------------|-------------|
| product_id | BIGINT | Primary Key, Auto Increment | Unique product ID |
| vendor_id | BIGINT | Foreign Key, NOT NULL | References Vendors table |
| category_id | BIGINT | Foreign Key, NOT NULL | References Categories table |
| product_name | VARCHAR(255) | NOT NULL | Product name |
| slug | VARCHAR(255) | UNIQUE | SEO-friendly product URL |
| short_description | TEXT | NULL | Short description |
| description | LONGTEXT | NOT NULL | Detailed product description |
| brand | VARCHAR(100) | NULL | Product brand |
| sku | VARCHAR(100) | UNIQUE | Stock Keeping Unit |
| price | DECIMAL(10,2) | NOT NULL | Selling price |
| discount_price | DECIMAL(10,2) | NULL | Discounted price |
| stock_quantity | INT | DEFAULT 0 | Available stock |
| weight | DECIMAL(8,2) | NULL | Product weight |
| thumbnail | VARCHAR(255) | NULL | Main product image |
| status | ENUM('Draft','Active','Out of Stock','Inactive') | DEFAULT 'Draft' | Product status |
| created_at | TIMESTAMP | DEFAULT CURRENT_TIMESTAMP | Created date |
| updated_at | TIMESTAMP | DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP | Last updated date |

---

### Primary Key

- product_id

---

### Foreign Keys

- vendor_id → Vendors.vendor_id
- category_id → Categories.category_id

---

### Relationships

- One Vendor can upload many Products.
- One Category can contain many Products.
- One Product can have multiple Product Images.
- One Product can have many Reviews.
- One Product can appear in many Order Items.
- One Product can be added to many Wishlists.
- One Product can be added to many Cart Items.

---

### Business Rules

- Product name cannot be empty.
- Price must be greater than zero.
- Stock cannot be negative.
- Every product must belong to one Vendor.
- Every product must belong to one Category.
- SKU must be unique.
- Only Active products should be visible to customers.

---

### Real-Time Example

ABC Fashion uploads a Men's Cotton T-Shirt.

The product belongs to the Fashion category.

Price is ₹799.

Stock is 120 pieces.

Customers can search, view, add to cart, and purchase this product.

---

### Interview Question

Q. Why do we store vendor_id and category_id in the Products table?

Answer:

Because every product belongs to one vendor and one category. Using foreign keys maintains relationships and prevents duplicate data.

---

### Key Takeaway

The Products table is the core of the Multi-Vendor E-Commerce Platform because almost every module such as Cart, Wishlist, Orders, Reviews, Payments, and Inventory depends on it.


## Table 5: Product Images

### Purpose

Stores multiple images for each product.

---

### Fields

| Field Name | Data Type | Constraint | Description |
|------------|-----------|------------|-------------|
| image_id | BIGINT | Primary Key, Auto Increment | Unique image ID |
| product_id | BIGINT | Foreign Key, NOT NULL | References Products table |
| image_url | VARCHAR(255) | NOT NULL | Product image path or URL |
| is_primary | BOOLEAN | DEFAULT FALSE | Main product image |
| created_at | TIMESTAMP | DEFAULT CURRENT_TIMESTAMP | Created date |

---

### Primary Key

- image_id

---

### Foreign Keys

- product_id → Products.product_id

---

### Relationships

- One Product can have many Product Images.
- Every Product Image belongs to one Product.

---

### Business Rules

- Every image must belong to a valid product.
- Only one image should be marked as the primary image.
- Image URL cannot be empty.

---

### Real-Time Example

A Mobile Phone product has:

- Front View
- Back View
- Side View
- Box Image

One of them is marked as the primary image displayed first to customers.

---

### Interview Question

Q. Why do we store product images in a separate table?

Answer:

Because one product can have multiple images. Storing them in a separate table avoids repeating image columns and follows database normalization.

---

### Key Takeaway

The Product Images table allows every product to store multiple images while keeping the database flexible and well organized.


## Table 6: Inventory

### Purpose

Stores stock information for each product and helps manage product availability.

---

### Fields

| Field Name | Data Type | Constraint | Description |
|------------|-----------|------------|-------------|
| inventory_id | BIGINT | Primary Key, Auto Increment | Unique inventory ID |
| product_id | BIGINT | Foreign Key, UNIQUE, NOT NULL | References Products table |
| available_stock | INT | NOT NULL | Current available stock |
| reserved_stock | INT | DEFAULT 0 | Stock reserved for pending orders |
| sold_stock | INT | DEFAULT 0 | Total sold quantity |
| low_stock_limit | INT | DEFAULT 10 | Low stock alert level |
| created_at | TIMESTAMP | DEFAULT CURRENT_TIMESTAMP | Created date |
| updated_at | TIMESTAMP | DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP | Last updated date |

---

### Primary Key

- inventory_id

---

### Foreign Keys

- product_id → Products.product_id

---

### Relationships

- One Product has one Inventory record.
- Every Inventory record belongs to one Product.

---

### Business Rules

- Available stock cannot be negative.
- Reserved stock cannot exceed available stock.
- Inventory record must exist for every product.
- Low stock alert should trigger when available stock reaches the low_stock_limit.

---

### Real-Time Example

ABC Fashion uploads a Men's Cotton T-Shirt.

Available Stock: 120

Reserved Stock: 5

Sold Stock: 35

When customers purchase the product, the available stock decreases and the sold stock increases automatically.

---

### Interview Question

Q. Why do we keep Inventory in a separate table instead of storing stock directly in the Products table?

Answer:

Because inventory changes frequently. Keeping it in a separate table improves scalability, performance, and inventory management without modifying product information.

---

### Key Takeaway

The Inventory table manages product stock efficiently and supports real-time inventory tracking for every product.


# Database Schema

## Table 7: Cart

### Purpose

Stores the products added by customers before they proceed to checkout.

---

### Fields

| Field Name | Data Type | Constraint | Description |
|------------|-----------|------------|-------------|
| cart_id | BIGINT | Primary Key, Auto Increment | Unique cart item ID |
| user_id | BIGINT | Foreign Key, NOT NULL | References Users table |
| product_id | BIGINT | Foreign Key, NOT NULL | References Products table |
| quantity | INT | NOT NULL, DEFAULT 1 | Quantity of product |
| price | DECIMAL(10,2) | NOT NULL | Product price when added to cart |
| created_at | TIMESTAMP | DEFAULT CURRENT_TIMESTAMP | Created date |
| updated_at | TIMESTAMP | DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP | Last updated date |

---

### Primary Key

- cart_id

---

### Foreign Keys

- user_id → Users.user_id
- product_id → Products.product_id

---

### Relationships

- One User can have many Cart Items.
- One Product can appear in many Cart Items.
- Every Cart Item belongs to one User.
- Every Cart Item belongs to one Product.

---

### Business Rules

- Quantity must be greater than zero.
- Quantity cannot exceed available stock.
- A user cannot have duplicate entries for the same product in the cart.
- Only Active products can be added to the cart.
- Cart items are removed after a successful order placement.

---

### Real-Time Example

Rajesh logs into the application.

He adds:

- Men's Cotton T-Shirt × 2
- Wireless Mouse × 1

The system stores both products in the Cart table.

When Rajesh places the order, the cart items are converted into Order Items and removed from the Cart table.

---

### Interview Question

Q. Why do we use a separate Cart table instead of storing cart information in the Users table?

Answer:

Because one user can add multiple products to the cart. A separate Cart table maintains a one-to-many relationship, avoids data duplication, supports database normalization, and makes cart management easier.

---

### Key Takeaway

The Cart table temporarily stores customer-selected products before checkout and acts as the bridge between product browsing and order placement.


# Database Schema

## Table 8: Wishlist

### Purpose

Stores the products that customers save for future purchase.

---

### Fields

| Field Name | Data Type | Constraint | Description |
|------------|-----------|------------|-------------|
| wishlist_id | BIGINT | Primary Key, Auto Increment | Unique wishlist item ID |
| user_id | BIGINT | Foreign Key, NOT NULL | References Users table |
| product_id | BIGINT | Foreign Key, NOT NULL | References Products table |
| created_at | TIMESTAMP | DEFAULT CURRENT_TIMESTAMP | Created date |

---

### Primary Key

- wishlist_id

---

### Foreign Keys

- user_id → Users.user_id
- product_id → Products.product_id

---

### Relationships

- One User can have many Wishlist Items.
- One Product can appear in many Wishlists.
- Every Wishlist Item belongs to one User.
- Every Wishlist Item belongs to one Product.

---

### Business Rules

- A user cannot add the same product to the wishlist more than once.
- Only Active products can be added to the wishlist.
- A wishlist item can be moved to the Cart.
- Wishlist items remain until the user removes them.
- If a product is deleted, its wishlist entries should also be removed.

---

### Real-Time Example

Rajesh likes a Wireless Headphone but does not want to purchase it today.

He clicks **Add to Wishlist**.

The system stores the product in the Wishlist table.

Later, Rajesh moves the product from the Wishlist to the Cart and completes the purchase.

---

### Interview Question

Q. Why do we maintain a separate Wishlist table instead of storing wishlist information in the Users table?

Answer:

Because one user can save multiple products for future purchase. A separate Wishlist table maintains a one-to-many relationship, avoids duplicate data, follows database normalization, and makes wishlist management simple and efficient.

---

### Key Takeaway

The Wishlist table allows customers to save products for future purchase, improving the shopping experience and increasing the chances of future sales.


# Database Schema

## Table 9: Orders

### Purpose

Stores the order information placed by customers after successful checkout.

---

### Fields

| Field Name | Data Type | Constraint | Description |
|------------|-----------|------------|-------------|
| order_id | BIGINT | Primary Key, Auto Increment | Unique order ID |
| user_id | BIGINT | Foreign Key, NOT NULL | References Users table |
| order_number | VARCHAR(50) | UNIQUE, NOT NULL | Unique order number |
| total_amount | DECIMAL(10,2) | NOT NULL | Total order amount |
| payment_status | ENUM('Pending','Paid','Failed','Refunded') | DEFAULT 'Pending' | Payment status |
| order_status | ENUM('Pending','Confirmed','Packed','Shipped','Delivered','Cancelled') | DEFAULT 'Pending' | Order status |
| shipping_address | TEXT | NOT NULL | Delivery address |
| created_at | TIMESTAMP | DEFAULT CURRENT_TIMESTAMP | Order creation date |
| updated_at | TIMESTAMP | DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP | Last updated date |

---

### Primary Key

- order_id

---

### Foreign Keys

- user_id → Users.user_id

---

### Relationships

- One User can place many Orders.
- Every Order belongs to one User.
- One Order can contain many Order Items.
- One Order can have one Payment.
- One Order can have one Shipping record.

---

### Business Rules

- Every order must belong to a valid user.
- Total amount must be greater than zero.
- An order must contain at least one Order Item.
- Payment status should be updated after payment.
- Delivered or Cancelled orders cannot be modified.

---

### Real-Time Example

Rajesh purchases:

- Men's Cotton T-Shirt × 2
- Wireless Mouse × 1

Total Amount: ₹2,398

Payment Status: Paid

Order Status: Confirmed

The system creates a new order in the Orders table and generates a unique order number.

---

### Interview Question

**Q. Why do we store Orders separately instead of storing order details in the Users table?**

**Answer:**

Because one user can place multiple orders over time. A separate Orders table maintains a one-to-many relationship, avoids data duplication, follows database normalization, and simplifies order management.

---

### Key Takeaway

The Orders table stores every customer purchase and acts as the central table connecting users, order items, payments, shipping, and order tracking.


## Table 10: Order Items

### Purpose

Stores individual products included in each order.

---

### Fields

| Field Name | Data Type | Constraint | Description |
|------------|-----------|------------|-------------|
| order_item_id | BIGINT | Primary Key, Auto Increment | Unique order item ID |
| order_id | BIGINT | Foreign Key, NOT NULL | References Orders table |
| product_id | BIGINT | Foreign Key, NOT NULL | References Products table |
| quantity | INT | NOT NULL | Quantity ordered |
| unit_price | DECIMAL(10,2) | NOT NULL | Price of one product |
| total_price | DECIMAL(10,2) | NOT NULL | Quantity × Unit Price |
| created_at | TIMESTAMP | DEFAULT CURRENT_TIMESTAMP | Created date |

---

### Primary Key

- order_item_id

---

### Foreign Keys

- order_id → Orders.order_id
- product_id → Products.product_id

---

### Relationships

- One Order can have many Order Items.
- One Product can appear in many Order Items.
- Every Order Item belongs to one Order.
- Every Order Item belongs to one Product.

---

### Business Rules

- Quantity must be greater than zero.
- Unit price must be greater than zero.
- Total price = Quantity × Unit Price.
- Every Order Item must belong to a valid Order.
- Every Order Item must reference a valid Product.

---

### Real-Time Example

Rajesh places an order containing:

- Men's Cotton T-Shirt × 2
- Wireless Mouse × 1

The system creates:

Order Item 1
Product: Men's Cotton T-Shirt
Quantity: 2

Order Item 2
Product: Wireless Mouse
Quantity: 1

---

### Interview Question

Q. Why do we create an Order Items table instead of storing products directly in the Orders table?

Answer:

Because one order can contain multiple products. The Order Items table implements the many-to-many relationship between Orders and Products while keeping the database normalized and scalable.

---

### Key Takeaway

The Order Items table stores every product purchased in an order and acts as the bridge between the Orders and Products tables.


# Database Schema

## Table 11: Payments

### Purpose

Stores payment information for every order made by customers.

---

### Fields

| Field Name | Data Type | Constraint | Description |
|------------|-----------|------------|-------------|
| payment_id | BIGINT | Primary Key, Auto Increment | Unique payment ID |
| order_id | BIGINT | Foreign Key, UNIQUE, NOT NULL | References Orders table |
| payment_method | ENUM('UPI','Credit Card','Debit Card','Net Banking','Cash on Delivery','Wallet') | NOT NULL | Payment method |
| transaction_id | VARCHAR(100) | UNIQUE | Payment gateway transaction ID |
| amount | DECIMAL(10,2) | NOT NULL | Amount paid |
| payment_status | ENUM('Pending','Success','Failed','Refunded') | DEFAULT 'Pending' | Current payment status |
| paid_at | TIMESTAMP | NULL | Payment completion date |
| created_at | TIMESTAMP | DEFAULT CURRENT_TIMESTAMP | Record creation date |

---

### Primary Key

- payment_id

---

### Foreign Keys

- order_id → Orders.order_id

---

### Relationships

- One Order has one Payment.
- Every Payment belongs to one Order.

---

### Business Rules

- Payment amount must be greater than zero.
- Successful payment should update the Order status.
- Transaction ID must be unique.
- Refund status is applicable only after a successful payment.
- Cash on Delivery payments remain Pending until delivery confirmation.

---

### Real-Time Example

Rajesh purchases:

- Men's Cotton T-Shirt × 2
- Wireless Mouse × 1

Total Amount: ₹2,398

Payment Method: UPI

Transaction ID: TXN984563210

Payment Status: Success

The system stores the payment details in the Payments table and links them to the corresponding Order.

---

### Interview Question

**Q. Why do we maintain a separate Payments table instead of storing payment information directly in the Orders table?**

**Answer:**

Because payment information has its own lifecycle, including payment methods, transaction IDs, refunds, failures, and payment status updates. Keeping it in a separate table follows database normalization, improves scalability, and simplifies payment management.

---

### Key Takeaway

The Payments table securely stores transaction details for every order and acts as the bridge between customer orders and payment gateways.


# Database Schema

## Table 12: Shipping

### Purpose

Stores shipping and delivery information for every customer order.

---

### Fields

| Field Name | Data Type | Constraint | Description |
|------------|-----------|------------|-------------|
| shipping_id | BIGINT | Primary Key, Auto Increment | Unique shipping ID |
| order_id | BIGINT | Foreign Key, UNIQUE, NOT NULL | References Orders table |
| courier_name | VARCHAR(100) | NULL | Courier service provider |
| tracking_number | VARCHAR(100) | UNIQUE | Shipment tracking number |
| shipping_status | ENUM('Pending','Packed','Shipped','Out for Delivery','Delivered','Returned') | DEFAULT 'Pending' | Current shipping status |
| estimated_delivery | DATE | NULL | Expected delivery date |
| delivered_at | TIMESTAMP | NULL | Actual delivery date and time |
| created_at | TIMESTAMP | DEFAULT CURRENT_TIMESTAMP | Record creation date |
| updated_at | TIMESTAMP | DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP | Last updated date |

---

### Primary Key

- shipping_id

---

### Foreign Keys

- order_id → Orders.order_id

---

### Relationships

- One Order has one Shipping record.
- Every Shipping record belongs to one Order.

---

### Business Rules

- Shipping record must exist for every confirmed order.
- Tracking number must be unique.
- Shipping status cannot move backwards (e.g., Delivered → Shipped).
- Delivered orders must have a delivered_at timestamp.
- Returned orders can only exist after shipment.

---

### Real-Time Example

Rajesh places an order for:

- Men's Cotton T-Shirt × 2
- Wireless Mouse × 1

Courier Name: Blue Dart

Tracking Number: BD987654321IN

Shipping Status: Shipped

Estimated Delivery: 10-Aug-2026

Once the courier delivers the package, the Shipping Status changes to **Delivered** and the **delivered_at** field is updated automatically.

---

### Interview Question

**Q. Why do we maintain a separate Shipping table instead of storing shipping details in the Orders table?**

**Answer:**

Shipping information changes frequently after an order is placed. Keeping it in a separate Shipping table allows independent tracking of courier details, tracking numbers, delivery status, and estimated delivery dates while keeping the Orders table clean, normalized, and scalable.

---

### Key Takeaway

The Shipping table manages the complete delivery lifecycle of every order and provides real-time shipment tracking from dispatch to successful delivery.


# Database Schema

## Table 13: Reviews

### Purpose

Stores customer ratings and reviews for purchased products.

---

### Fields

| Field Name | Data Type | Constraint | Description |
|------------|-----------|------------|-------------|
| review_id | BIGINT | Primary Key, Auto Increment | Unique review ID |
| user_id | BIGINT | Foreign Key, NOT NULL | References Users table |
| product_id | BIGINT | Foreign Key, NOT NULL | References Products table |
| order_id | BIGINT | Foreign Key, NOT NULL | References Orders table |
| rating | INT | NOT NULL | Rating between 1 and 5 |
| review_text | TEXT | NULL | Customer review |
| review_status | ENUM('Pending','Approved','Rejected') | DEFAULT 'Pending' | Review moderation status |
| created_at | TIMESTAMP | DEFAULT CURRENT_TIMESTAMP | Review creation date |
| updated_at | TIMESTAMP | DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP | Last updated date |

---

### Primary Key

- review_id

---

### Foreign Keys

- user_id → Users.user_id
- product_id → Products.product_id
- order_id → Orders.order_id

---

### Relationships

- One User can write many Reviews.
- One Product can have many Reviews.
- One Order can contain multiple reviewed Products.
- Every Review belongs to one User.
- Every Review belongs to one Product.
- Every Review belongs to one Order.

---

### Business Rules

- Only customers who purchased the product can submit a review.
- Rating must be between 1 and 5.
- A user can review a purchased product only once.
- Reviews must be approved before becoming visible to other customers.
- Deleted products should also remove their associated reviews.

---

### Real-Time Example

Rajesh purchases:

- Men's Cotton T-Shirt × 2

After delivery, he rates the product:

Rating: ⭐⭐⭐⭐⭐ (5/5)

Review:

"Excellent quality, comfortable fabric, and perfect fitting."

Review Status: Approved

The system stores the review and displays it on the product page after approval.

---

### Interview Question

**Q. Why do we maintain a separate Reviews table instead of storing reviews in the Products table?**

**Answer:**

Because one product can receive thousands of reviews from different users. A separate Reviews table maintains a one-to-many relationship, avoids data duplication, follows database normalization, and makes review management scalable and efficient.

---

### Key Takeaway

The Reviews table stores customer feedback and ratings for purchased products, helping future buyers make informed decisions while improving product credibility and customer trust.


# Database Schema

## Table 14: Coupons

### Purpose

Stores discount coupons that customers can apply during checkout to receive price reductions.

---

### Fields

| Field Name | Data Type | Constraint | Description |
|------------|-----------|------------|-------------|
| coupon_id | BIGINT | Primary Key, Auto Increment | Unique coupon ID |
| coupon_code | VARCHAR(50) | UNIQUE, NOT NULL | Unique coupon code |
| discount_type | ENUM('Percentage','Flat') | NOT NULL | Type of discount |
| discount_value | DECIMAL(10,2) | NOT NULL | Discount amount or percentage |
| minimum_order_amount | DECIMAL(10,2) | DEFAULT 0 | Minimum order amount required |
| maximum_discount | DECIMAL(10,2) | NULL | Maximum discount allowed (for percentage coupons) |
| expiry_date | DATE | NOT NULL | Coupon expiration date |
| usage_limit | INT | DEFAULT 1 | Maximum number of coupon usages |
| coupon_status | ENUM('Active','Inactive','Expired') | DEFAULT 'Active' | Coupon status |
| created_at | TIMESTAMP | DEFAULT CURRENT_TIMESTAMP | Coupon creation date |
| updated_at | TIMESTAMP | DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP | Last updated date |

---

### Primary Key

- coupon_id

---

### Relationships

- One Coupon can be used by many Orders.
- One Order can use one Coupon.
- A Coupon may not be used if it is expired or inactive.

---

### Business Rules

- Coupon code must be unique.
- Coupon cannot be used after the expiry date.
- Order amount must satisfy the minimum order amount.
- Percentage discounts cannot exceed the maximum discount amount.
- Inactive or expired coupons cannot be applied.
- Usage limit cannot be exceeded.

---

### Real-Time Example

Rajesh purchases:

- Men's Cotton T-Shirt × 2
- Wireless Mouse × 1

Order Total: ₹2,398

Coupon Applied: **WELCOME10**

Discount Type: Percentage

Discount: 10%

Maximum Discount: ₹250

Final Discount Applied: ₹240

Final Payable Amount: ₹2,158

The system validates the coupon and applies the discount before payment.

---

### Interview Question

**Q. Why do we maintain a separate Coupons table instead of storing coupon information in the Orders table?**

**Answer:**

Because a single coupon can be reused across many customer orders. Keeping coupons in a separate table avoids data duplication, supports reusable discount campaigns, follows database normalization, and simplifies coupon management.

---

### Key Takeaway

The Coupons table centrally manages all discount offers, validates coupon eligibility, and helps increase sales by providing promotional discounts during checkout.


# Database Schema

## Table 15: Notifications

### Purpose

Stores all system notifications sent to users, vendors, and administrators.

---

### Fields

| Field Name | Data Type | Constraint | Description |
|------------|-----------|------------|-------------|
| notification_id | BIGINT | Primary Key, Auto Increment | Unique notification ID |
| user_id | BIGINT | Foreign Key | References Users table |
| vendor_id | BIGINT | Foreign Key | References Vendors table |
| title | VARCHAR(255) | NOT NULL | Notification title |
| message | TEXT | NOT NULL | Notification message |
| notification_type | ENUM('Order','Payment','Shipping','Promotion','System','Review') | NOT NULL | Type of notification |
| is_read | BOOLEAN | DEFAULT FALSE | Notification read status |
| created_at | TIMESTAMP | DEFAULT CURRENT_TIMESTAMP | Notification creation date |

---

### Primary Key

- notification_id

---

### Foreign Keys

- user_id → Users.user_id
- vendor_id → Vendors.vendor_id

---

### Relationships

- One User can receive many Notifications.
- One Vendor can receive many Notifications.
- Every Notification belongs to either a User or a Vendor.
- Notifications are generated based on system events.

---

### Business Rules

- Notification title cannot be empty.
- Notification message cannot be empty.
- Notifications should be marked as read after viewing.
- Promotional notifications should only be sent to eligible users.
- System notifications cannot be deleted until they expire.

---

### Real-Time Example

Rajesh places an order.

The system sends:

Title:
Order Confirmed

Message:
Your order #ORD10245 has been confirmed successfully.

Later the system sends:

- Payment Successful
- Order Shipped
- Out for Delivery
- Order Delivered

All these records are stored in the Notifications table.

---

### Interview Question

**Q. Why do we maintain a separate Notifications table instead of storing notifications in the Users table?**

**Answer:**

Because one user or vendor can receive thousands of notifications. A separate Notifications table maintains a one-to-many relationship, follows database normalization, improves scalability, and makes notification management efficient.

---

### Key Takeaway

The Notifications table stores all system-generated messages, helping users and vendors stay updated about orders, payments, shipping, promotions, and important account activities.


# Database Schema

## Table 16: Addresses

### Purpose

Stores customer delivery and billing addresses used during the checkout process.

---

### Fields

| Field Name | Data Type | Constraint | Description |
|------------|-----------|------------|-------------|
| address_id | BIGINT | Primary Key, Auto Increment | Unique address ID |
| user_id | BIGINT | Foreign Key, NOT NULL | References Users table |
| full_name | VARCHAR(150) | NOT NULL | Receiver's full name |
| mobile_number | VARCHAR(15) | NOT NULL | Contact number |
| address_line_1 | VARCHAR(255) | NOT NULL | House No., Street |
| address_line_2 | VARCHAR(255) | NULL | Landmark or Area |
| city | VARCHAR(100) | NOT NULL | City name |
| state | VARCHAR(100) | NOT NULL | State name |
| country | VARCHAR(100) | DEFAULT 'India' | Country name |
| postal_code | VARCHAR(10) | NOT NULL | PIN / ZIP Code |
| address_type | ENUM('Home','Work','Other') | DEFAULT 'Home' | Address type |
| is_default | BOOLEAN | DEFAULT FALSE | Default delivery address |
| created_at | TIMESTAMP | DEFAULT CURRENT_TIMESTAMP | Record creation date |
| updated_at | TIMESTAMP | DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP | Last updated date |

---

### Primary Key

- address_id

---

### Foreign Keys

- user_id → Users.user_id

---

### Relationships

- One User can have multiple Addresses.
- Every Address belongs to one User.
- One Address can be used for multiple Orders.

---

### Business Rules

- Every address must belong to a valid user.
- Mobile number must contain a valid phone number.
- Postal code must be valid.
- A user can have only one default address at a time.
- At least one address must exist before placing an order.

---

### Real-Time Example

Rajesh saves two addresses:

Home

- 12-45, Main Road
- Vijayawada
- Andhra Pradesh
- 520001

Office

- IT Park
- Gachibowli
- Hyderabad
- Telangana
- 500032

During checkout, Rajesh selects the Home address for delivery.

---

### Interview Question

**Q. Why do we maintain a separate Addresses table instead of storing addresses in the Users table?**

**Answer:**

Because one user can have multiple delivery and billing addresses. A separate Addresses table follows database normalization, avoids duplicate data, and makes address management flexible and scalable.

---

### Key Takeaway

The Addresses table stores customer delivery and billing locations, making the checkout process flexible while supporting multiple saved addresses for every user.