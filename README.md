# Coffee Shop Management

This repository contains three classes implemented in Python: `Customer`, `Coffee`, and `Order`. These classes are designed to manage customers, coffee types, and orders in a coffee shop.

## Classes and Features

### Customer Class

- **Initialization**: Create a `Customer` object with a name.
- **Name Property**: Get and set the customer's name with validation.
- **Orders Method**: Returns a list of all orders for that customer.
- **Coffees Method**: Returns a unique list of all coffees a customer has ordered.
- **Create Order Method**: Creates and returns a new `Order` instance associated with the customer and the provided coffee.

### Coffee Class

- **Initialization**: Create a `Coffee` object with a name.
- **Name Property**: Get the coffee's name with validation and immutability.
- **Orders Method**: Returns a list of all orders for that coffee.
- **Customers Method**: Returns a unique list of all customers who have ordered a particular coffee.
- **Num Orders Method**: Returns the total number of times a coffee has been ordered.
- **Average Price Method**: Returns the average price for a coffee based on its orders.

### Order Class

- **Initialization**: Create an `Order` object with a `Customer` instance, a `Coffee` instance, and a price.
- **Price Property**: Get the price for the order with validation and immutability.
- **Customer Property**: Returns the customer object for that order.
- **Coffee Property**: Returns the coffee object for that order.

## Usage

### Customer Class

#### Initialization

To create a new `Customer` object, simply pass the name as an argument to the constructor:

```python
customer = Customer("Victor Koech")
```
