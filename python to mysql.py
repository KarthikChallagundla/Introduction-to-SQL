import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="password",
  database="classicmodels"
)

cursor = mydb.cursor()

print("-------------------------------MYSQL WITH PYTHON----------------------------")

'''
CREATE A DATABASE
cursor.execute("CREATE DATABASE IF NOT EXISTS classicmodels;")
for x in cursor:
  print(x)
'''

print("------------------------DATABASES-------------------------")
cursor.execute("SHOW DATABASES")  # MYSQL command to show all the databases
for x in cursor.fetchall():
  print(x)
  
"""
CREATE ALL THE REQUIRED TABLES

cursor.execute('''CREATE TABLE productlines (
  productLine varchar(50),
  textDescription varchar(4000) DEFAULT NULL,
  htmlDescription mediumtext,
  image mediumblob,
  PRIMARY KEY (productLine)
);''')
cursor.fetchall()

cursor.execute('''CREATE TABLE products (
  productCode varchar(15),
  productName varchar(70) NOT NULL,
  productLine varchar(50) NOT NULL,
  productScale varchar(10) NOT NULL,
  productVendor varchar(50) NOT NULL,
  productDescription text NOT NULL,
  quantityInStock smallint(6) NOT NULL,
  buyPrice decimal(10,2) NOT NULL,
  MSRP decimal(10,2) NOT NULL,
  PRIMARY KEY (productCode),
  FOREIGN KEY (productLine) REFERENCES productlines (productLine)
);
''')
cursor.fetchall()

cursor.execute('''CREATE TABLE offices (
  officeCode varchar(10),
  city varchar(50) NOT NULL,
  phone varchar(50) NOT NULL,
  addressLine1 varchar(50) NOT NULL,
  addressLine2 varchar(50) DEFAULT NULL,
  state varchar(50) DEFAULT NULL,
  country varchar(50) NOT NULL,
  postalCode varchar(15) NOT NULL,
  territory varchar(10) NOT NULL,
  PRIMARY KEY (officeCode)
);''')
cursor.fetchall()

cursor.execute('''CREATE TABLE employees (
  employeeNumber int,
  lastName varchar(50) NOT NULL,
  firstName varchar(50) NOT NULL,
  extension varchar(10) NOT NULL,
  email varchar(100) NOT NULL,
  officeCode varchar(10) NOT NULL,
  reportsTo int DEFAULT NULL,
  jobTitle varchar(50) NOT NULL,
  PRIMARY KEY (employeeNumber),
  FOREIGN KEY (reportsTo) REFERENCES employees (employeeNumber),
  FOREIGN KEY (officeCode) REFERENCES offices (officeCode)
);''')
cursor.fetchall()

cursor.execute('''CREATE TABLE customers (
  customerNumber int,
  customerName varchar(50) NOT NULL,
  contactLastName varchar(50) NOT NULL,
  contactFirstName varchar(50) NOT NULL,
  phone varchar(50) NOT NULL,
  addressLine1 varchar(50) NOT NULL,
  addressLine2 varchar(50) DEFAULT NULL,
  city varchar(50) NOT NULL,
  state varchar(50) DEFAULT NULL,
  postalCode varchar(15) DEFAULT NULL,
  country varchar(50) NOT NULL,
  salesRepEmployeeNumber int DEFAULT NULL,
  creditLimit decimal(10,2) DEFAULT NULL,
  PRIMARY KEY (customerNumber),
  FOREIGN KEY (salesRepEmployeeNumber) REFERENCES employees (employeeNumber)
);''')
cursor.fetchall()

cursor.execute('''CREATE TABLE payments (
  customerNumber int,
  checkNumber varchar(50) NOT NULL,
  paymentDate date NOT NULL,
  amount decimal(10,2) NOT NULL,
  PRIMARY KEY (customerNumber,checkNumber),
  FOREIGN KEY (customerNumber) REFERENCES customers (customerNumber)
);''')
cursor.fetchall()

cursor.execute('''CREATE TABLE orders (
  orderNumber int,
  orderDate date NOT NULL,
  requiredDate date NOT NULL,
  shippedDate date DEFAULT NULL,
  status varchar(15) NOT NULL,
  comments text,
  customerNumber int NOT NULL,
  PRIMARY KEY (orderNumber),
  FOREIGN KEY (customerNumber) REFERENCES customers (customerNumber)
);''')
cursor.fetchall()

cursor.execute('''CREATE TABLE orderdetails (
  orderNumber int,
  productCode varchar(15) NOT NULL,
  quantityOrdered int NOT NULL,
  priceEach decimal(10,2) NOT NULL,
  orderLineNumber smallint(6) NOT NULL,
  PRIMARY KEY (orderNumber,productCode),
  FOREIGN KEY (orderNumber) REFERENCES orders (orderNumber),
  FOREIGN KEY (productCode) REFERENCES products (productCode)
);''')
cursor.fetchall()
"""


print("----------------------------TABLES------------------------")
cursor.execute("SHOW TABLES")  # MYSQL command to show all the available tables
for x in cursor.fetchall():
  print(x)
  
print("------------------------------------MYSQL COMMANDS----------------------------------")
cursor.execute("SELECT * FROM productlines") # Selects all the columns in the table
for (productLine, textDescription, htmlDescription, image) in cursor.fetchall():
  print(productLine, "\n", textDescription, "\n", htmlDescription)
  
cursor.execute("SELECT orderNumber, status, customerNumber FROM orders") # Selects specified columns in the table
for x in cursor.fetchall():
  print(x)
  
print("ORDER BY COMMAND")
cursor.execute("SELECT orderNumber, productCode FROM orderdetails ORDER BY orderNumber DESC") # Shows the data in an order
for x in cursor.fetchall():
  print(x)

print("LIMIT COMMAND")
cursor.execute("SELECT orderNumber, productCode, quantityOrdered FROM orderdetails ORDER BY orderNumber DESC LIMIT 10") # Limits the rows
for x in cursor.fetchall():
  print(x)
  
print("WHERE COMMAND")
cursor.execute("SELECT orderNumber, productCode FROM orderdetails WHERE orderNumber='10100'") # Shows the data based on condition
for x in cursor.fetchall():
  print(x)
  
print("CASE COMMAND")
cursor.execute("SELECT orderNumber, productCode, CASE WHEN quantityOrdered>30 THEN 'LESS' ELSE 'MORE' END FROM orderdetails")
for x in cursor.fetchall():
  print(x)

print("SELECTING TABLE WITH ALIAS NAME")
cursor.execute("SELECT p.customerNumber, p.checkNumber, p.amount FROM payments p")
for x in cursor.fetchall():
  print(x)
  
print("AND OR NOT COMMANDS")
cursor.execute("SELECT orderNumber, productCode, quantityOrdered FROM orderdetails WHERE quantityOrdered>20 AND quantityOrdered<40")
for x in cursor.fetchall():
  print(x)
  
cursor.execute("SELECT orderNumber, productCode, quantityOrdered FROM orderdetails WHERE quantityOrdered>20 OR orderNumber>11000")
for x in cursor.fetchall():
  print(x)
  
cursor.execute("SELECT orderNumber, productCode, quantityOrdered FROM orderdetails WHERE NOT quantityOrdered>20")
for x in cursor.fetchall():
  print(x)

print("Aggregrate Functions")
cursor.execute("SELECT COUNT(amount), MAX(amount), MIN(amount), AVG(amount), SUM(amount) FROM payments")
for x in cursor.fetchall():
  print(x)
  
print("SELECT WITH CONDITIONS OF MULTIPLE VALUES FROM COLUMN")
# Distinct is used for getting non duplicate values
cursor.execute("SELECT DISTINCT employeeNumber, firstName, lastName, officeCode FROM employees WHERE lastname IN ('Patterson', 'Bow')")
for x in cursor.fetchall():
  print(x)

cursor.execute("SELECT officeCode, COUNT(employeeNumber) FROM employees GROUP BY officeCode")
for x in cursor.fetchall():
  print(x)
  
print("LIKE AND NOT LIKE COMMAND")
cursor.execute("SELECT customerName FROM customers WHERE customerName LIKE 'a%'") # Select queries where customerName starts with a
for x in cursor.fetchall():
  print(x)

cursor.execute("SELECT customerName FROM customers WHERE customerName NOT LIKE 'a%'") # Select queries where customerName not starts with a
for x in cursor.fetchall():
  print(x)
  
print("DESCRIBE COMMAND")
cursor.execute("DESCRIBE payments") # Describes the table
for x in cursor.fetchall():
  print(x)

cursor.execute("SELECT COUNT(*) FROM products") # Print total number of rows
for x in cursor.fetchall():
  print(x)

print("UNION COMMAND")
cursor.execute("SELECT customerNumber FROM orders UNION SELECT customerNumber FROM payments ORDER BY customerNumber DESC")
for x in cursor.fetchall():
  print(x)

print("JOINS")
print("INNER JOIN")
cursor.execute("SELECT orders.orderNumber, customers.customerName FROM orders INNER JOIN customers ON orders.customerNumber = customers.customerNumber")
for x in cursor.fetchall():
  print(x)

print("LEFT JOIN")
cursor.execute("SELECT orders.orderNumber, customers.customerName FROM customers LEFT JOIN orders ON customers.customerNumber = orders.customerNumber")
for x in cursor.fetchall():
  print(x)

print("RIGHT JOIN")
cursor.execute("SELECT orders.orderNumber, customers.customerName FROM customers RIGHT JOIN orders ON customers.customerNumber = orders.customerNumber")
for x in cursor.fetchall():
  print(x)

print("FULL OUTER JOIN")
cursor.execute("SELECT orders.orderNumber, customers.customerName FROM customers LEFT JOIN orders ON customers.customerNumber = orders.customerNumber UNION SELECT orders.orderNumber, customers.customerName FROM customers RIGHT JOIN orders ON customers.customerNumber = orders.customerNumber")
for x in cursor.fetchall():
  print(x)
  
print("INDEX COMMAND")
cursor.execute("CREATE INDEX idx ON customers (customerName)")
  
cursor.execute("SHOW INDEX FROM customers")
for x in cursor.fetchall():
  print(x)
  
cursor.execute("DROP INDEX idx ON customers")
  
print("VIEWS COMMAND")
cursor.execute("CREATE VIEW customer_view AS SELECT customerNumber, customerName FROM customers")

cursor.execute("SHOW FULL TABLES IN classicmodels WHERE TABLE_TYPE LIKE 'VIEW'")
for x in cursor.fetchall():
  print(x)
  
cursor.execute("SELECT * FROM customer_view")
for x in cursor.fetchall():
  print(x)

cursor.execute("DROP VIEW customer_view")

cursor.close() # Closes the cursor
mydb.close() # Closes the database