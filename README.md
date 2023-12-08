# Bank Management System
**Bank Management System**
   - Prompt: Develop a console-based application that simulates a basic bank management system. This can involve classes, inheritance, and file handling for storing customer data.
 ***
 **Table of Contents**
- [Bank Management System](#bank-management-system)
- [1 The Design Problem](#1-the-design-problem)
- [2 Requirements](#2-requirements)
	- [2.1 Functional Requirements](#21-functional-requirements)
	- [2.2 Non-Functional Requirements](#22-non-functional-requirements)
	- [2.3 Restrictions](#23-restrictions)
- [3 Categorising and Prioritising Requirements](#3-categorising-and-prioritising-requirements)
	- [3.1 Classes and Modules](#31-classes-and-modules)
 ***
 # 1 The Design Problem
 Develop a console-based application that simulates a basic bank management system. This can involve classes, inheritance, and file handling for storing customer data. The application should allow users to log in and out of their account (I can store data via `csv` files). New users can sign up for an account- all users info will be stored in a `csv` or `txt` file. Users can view their balance deposit money, withdraw money, and also send/transfer money to other users (as long as they have their account number). They can view their information and modify it. Users can also close their account.
 
 # 2 Requirements
 ## 2.1 Functional Requirements
 1. Users can login / logout.
 2. New users can signup and existing users can close their account.
 3. Users can view their balance.
 5. Users can deposit money.
 6. Users can withdraw money.
 7. Users can transfer money to other existing users.
 8. Users can view their account information.
 9. Users can modify their account information.

## 2.2 Non-Functional Requirements
1. Instructions are intuitive.
2. Text font and size is easy to read.
3. Ease of flow.

## 2.3 Restrictions
1. A command-line app (though this the app could later be extended). 

# 3 Categorising and Prioritising Requirements
Since there are so few requirements, and they are all necessary for basic functionality, all of them will be implemented (they are all must-haves).

## 3.1 Classes and Modules
**Name**
- `first_name`: string
- `last_name`: string

**Address**
- `country`: string
- `state`: string
- `city`: string
- `street_address`: string
- `post_code`: string
- `user_id`: string
  
**User**
- `id`: string
- `email`: string
- `dob`: date
- `address`: object
- `username`: string
- `password`: string
- `generateId()`: string

**Bank**
- `authenticateAccount()`: void
- `createAccount()`: void
- `closeAccount()`: void
- `number_of_accounts`: double
- `generateAccountNumber()`: string

**Account**
- `user_id`: string
- `account_number`: string
- `balance`: float
- `viewBalance()`: void
- `depositMoney()`: void
- `withdrawMoney()`: void
- `transferMoney()`: void
-  `viewAccountInfo()`: void
-  `updateAccountInfo()`: void
-  `generateAccountNumber()`: string

**Display**
- `welcomeMessage()`: void
- `displayMenu()`: void
- `startBank()`: void
