# Python OOP Real-Word Example

A hands-on Python repository for learning and practicing **Object-Oriented Programming (OOP)** through realistic software projects.

This repository is part of my journey from:

**Master's in Applied Computing → Data Analytics → AI Engineering → Generative AI → AI Agents → Advanced AI**

The goal is not only to learn Python syntax, but to develop the software-engineering foundations required to build reliable, maintainable, and scalable data and AI applications.

---

## 🎯 Purpose

This repository focuses on learning Python OOP through **real-world software scenarios** rather than isolated syntax exercises.

The projects progressively cover:

* Classes and Objects
* Encapsulation
* Inheritance
* Abstraction
* Polymorphism
* Object relationships
* Exception handling
* Type hints
* Modular Python applications
* Controllers and separation of concerns
* Clean code structure
* Reusable components
* Professional Python development practices

The examples are intentionally based on realistic business domains so that the Python concepts can later transfer naturally into Data Analytics, Machine Learning, AI Engineering, Generative AI, and AI Agent development.

---

# 📚 Learning Roadmap

## 01 — Classes & Objects

### Real-world project

**E-commerce Order System**

### Concepts

* Classes
* Objects
* Constructors
* `__init__`
* `self`
* Instance attributes
* Class attributes
* Instance methods
* Parameters and arguments
* Return values
* Type hints
* Validation
* Exceptions
* Lists
* Loops
* `Decimal`
* UUID
* `__str__`
* Modules and imports
* Object relationships
* Controller pattern
* Thin `main.py`

### Domain objects

```text
Customer
Product
OrderItem
Order
```

The project demonstrates how real-world entities can be represented as Python objects and how those objects interact with each other.

---

## 02 — Encapsulation

### Real-world project

**Bank Account System**

### Concepts

* Encapsulation
* Protected attributes
* `_attribute` convention
* Controlled state changes
* Getter methods
* Validation
* `raise ValueError`
* Error handling
* Internal helper methods
* Separation of concerns

### Main idea

Sensitive internal state should not be changed freely from outside the object.

Example:

```python
account.withdraw(Decimal("250.00"))
```

instead of directly manipulating:

```python
account._balance
```

The class controls how its internal state changes.

---

## 03 — Inheritance

### Real-world project

**Employee Management System**

### Concepts

* Parent/base classes
* Child/derived classes
* Inheritance
* `super()`
* Constructor reuse
* Shared behavior
* Specialized behavior
* Method overriding
* `isinstance()`

### Example hierarchy

```text
Employee
   │
   ├── Developer
   │
   └── Manager
```

A `Developer` and `Manager` are both employees, so they can reuse common employee functionality while adding their own specialized behavior.

---

## 04 — Abstraction

### Real-world project

**Payment System**

### Concepts

* Abstract classes
* `ABC`
* `@abstractmethod`
* Interfaces/contracts
* Concrete implementations
* `super()`
* Hiding implementation details

### Example hierarchy

```text
Payment
   │
   ├── CreditCardPayment
   │
   └── BankTransferPayment
```

The abstract `Payment` class defines what every payment method must provide, while each concrete payment class determines how the operation works.

---

## 05 — Polymorphism

### Real-world project

**Notification System**

### Concepts

* Polymorphism
* Common interfaces
* Different implementations
* Method overriding
* Dynamic method behavior
* Programming against abstractions

### Example hierarchy

```text
Notification
   │
   ├── EmailNotification
   ├── SMSNotification
   └── PushNotification
```

All notification types provide:

```python
send()
```

but each implementation behaves differently.

The application can therefore work with:

```python
notification.send()
```

without needing to know the exact notification type.

---

# 🧩 06 — All Four OOP Pillars

The next project combines the four major OOP concepts:

```text
                 OOP
                  │
      ┌───────────┼───────────┐
      │           │           │
      ↓           ↓           ↓
Encapsulation  Inheritance  Polymorphism
      │           │           │
      └───────────┼───────────┘
                  ↓
             Abstraction
```

The goal is to understand how these concepts work together in a larger application rather than treating them as isolated topics.

---

# 🗂️ Repository Structure

```text
python-oop-practice/
│
├── README.md
│
├── 01_classes_objects/
│   ├── __init__.py
│   ├── customer.py
│   ├── product.py
│   ├── order_item.py
│   ├── order.py
│   ├── controller.py
│   └── main.py
│
├── 02_encapsulation/
│   ├── __init__.py
│   ├── bank_account.py
│   ├── controller.py
│   └── main.py
│
├── 03_inheritance/
│   ├── __init__.py
│   ├── employee.py
│   ├── developer.py
│   ├── manager.py
│   ├── controller.py
│   └── main.py
│
├── 04_abstraction/
│   ├── __init__.py
│   ├── payment.py
│   ├── credit_card_payment.py
│   ├── bank_transfer_payment.py
│   ├── controller.py
│   └── main.py
│
└── 05_polymorphism/
    ├── __init__.py
    ├── notification.py
    ├── email_notification.py
    ├── sms_notification.py
    ├── push_notification.py
    ├── controller.py
    └── main.py
```

---

# 🏗️ Project Architecture

The projects generally follow a simple separation of responsibilities:

```text
             main.py
                │
                ↓
           controller.py
                │
        ┌───────┼───────┐
        ↓       ↓       ↓
      Class   Class   Class
        │       │       │
        └───────┴───────┘
             Domain
             Logic
```

### `main.py`

Responsible for starting the application.

It should remain lightweight and readable.

### `controller.py`

Responsible for coordinating the workflow between objects.

The controller should **coordinate**, not contain every piece of business logic.

### Domain classes

Responsible for their own data and behavior.

For example:

```text
Product
   ↓
inventory behavior

Order
   ↓
order behavior

BankAccount
   ↓
account behavior
```

This separation makes the code easier to understand, test, maintain, and extend.

---

# 🛡️ Error Handling

The projects also practice professional exception handling.

Typical pattern:

```python
try:
    # Application operation

except ValueError as error:
    print(f"Invalid data: {error}")

except TypeError as error:
    print(f"Invalid type: {error}")

except RuntimeError as error:
    print(f"Application error: {error}")

except Exception as error:
    print(f"Unexpected error: {error}")
```

Domain classes are responsible for detecting invalid states and raising appropriate exceptions.

The application boundary is responsible for handling those exceptions and presenting useful feedback.

---

# 🐍 Python Skills Practiced

Throughout these projects, the repository reinforces:

### Python Fundamentals

* Variables
* Strings
* Integers
* Floats
* `Decimal`
* Lists
* Loops
* Conditional statements
* Functions
* Parameters
* Arguments
* Return values

### Object-Oriented Programming

* Classes
* Objects
* Constructors
* Attributes
* Methods
* Class attributes
* Instance attributes
* Encapsulation
* Inheritance
* Abstraction
* Polymorphism
* Object composition
* Object relationships

### Professional Python

* Type hints
* Docstrings
* Validation
* Exception handling
* Modules
* Imports
* Multi-file applications
* Separation of concerns
* Controllers
* Readable code
* Reusable components

---

