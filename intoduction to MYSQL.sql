-- CREATE TABLES

CREATE TABLE students(
NAME VARCHAR (20),
rollno INT,
course VARCHAR(30),
dept VARCHAR(20),
age int);

CREATE TABLE teachers(
NAME VARCHAR(24),
id INT,
course VARCHAR(25),
dept VARCHAR(10),
age INT
);

-- INSERT DATA TO TABLES

INSERT INTO students VALUES("karthik", 100, "maths", "cse", 20);
INSERT INTO students VALUES("anil", 101, "social", "civil", 21);
INSERT INTO students VALUES("pavan", 102, "computers", "ece", 20);
INSERT INTO students VALUES("rishik", 103, "physics", "eee", 19);
INSERT INTO students VALUES("mythresh", 104, "data science", "cse", 20);

INSERT INTO teachers VALUES("rajesh", 200, "discrete maths", "cse", 30);
INSERT INTO teachers VALUES("satish", 201, "physics", "ece", 32);
INSERT INTO teachers VALUES("krishna", 202, "oops", "eee", 40);
INSERT INTO teachers VALUES("bhavani", 203, "materials", "mme", 35);
INSERT INTO teachers VALUES("sampath", 204, "c programming", "civil", 39);

-- SELECT COMMAND

SELECT * FROM students; -- displays all the values
SELECT NAME FROM students; -- displays specified values

-- DISTINCT COMMAND

SELECT DISTINCT dept FROM students; -- displays only distinct values

-- WHERE COMMAND

SELECT NAME FROM students WHERE age >= 20;
SELECT NAME FROM teachers WHERE dept='cse';

-- AND OR NOT COMMANDS

SELECT NAME FROM students WHERE age>=20 AND dept='cse';
SELECT id FROM teachers WHERE age>=30 OR dept='cse';
SELECT NAME FROM students WHERE NOT dept='cse';

-- BETWEEN CONDITION

SELECT NAME FROM students WHERE age BETWEEN 20 AND 21;

-- IN AND NOT IN COMMAND

SELECT NAME FROM students WHERE dept IN ('cse', 'ece');
SELECT NAME FROM students WHERE dept NOT IN ('cse', 'ece');

-- AS COMMAND

SELECT max(age) AS maximumage FROM students; -- RENAMES THE COLUMN NAME

-- LIMIT COMMAND

SELECT NAME FROM students LIMIT 1; -- LIMITS THE OUTPUT ROWS

-- AGGREGATE FUNCTIONS
-- MIN AND MAX COMMAND

SELECT max(age) FROM students;
SELECT min(age) FROM students;

-- COUNT AVG SUM COMMANDS

SELECT count(NAME) FROM students;
SELECT avg(age) FROM students;
SELECT sum(age) FROM students;

-- LIKE COMMAND

SELECT * FROM students WHERE NAME LIKE "karthik";

-- WILDCARS LIKE % --BEFORE % AND AFTER %

SELECT * FROM students WHERE NAME LIKE "a%"; -- ALL NAMES STARTED WITH LETTER 'a' OR WORD
SELECT * FROM students WHERE NAME LIKE "%k"; -- ALL NAMES ENDED WITH LETTER 'k' OR WORD

-- NOT LIKE COMMAND

SELECT * FROM students WHERE dept NOT LIKE "cse";

-- UNION COMMAND

SELECT dept FROM students UNION SELECT dept FROM teachers;

-- ORDER BY COMMAND

SELECT NAME FROM students ORDER BY age ASC;
SELECT NAME FROM teachers ORDER BY age DESC;

-- GROUP BY COMMAND -- MAINLY USED BY AGGREGATE FUNCTIONS LIKE MIN MAX COUNT AVG SUM

SELECT min(age) FROM students GROUP BY rollno;

-- UPDATE COMMAND

UPDATE students SET NAME = "rahul" WHERE rollno="101"; -- NOT UPDATING VALUES(ERROR)

-- ALTER COMMAND -- ADD DELETE MODIFY COLUMNS

ALTER TABLE students ADD gender VARCHAR(20);
ALTER TABLE students DROP COLUMN gender;
ALTER TABLE students MODIFY COLUMN age FLOAT; -- AGE COLUMN CHANGED FROM INT TO FLOAT
ALTER TABLE students MODIFY COLUMN age INT;
SELECT * FROM students;

-- CHANGE TABLE NAME AND COLUMN NAME USING ALTER COMMAND

ALTER TABLE students RENAME student;
ALTER TABLE student RENAME students;

ALTER TABLE students CHANGE COLUMN dept department VARCHAR(20);
ALTER TABLE students CHANGE COLUMN department dept VARCHAR(20);

-- SAVEPOINT COMMIT ROLLBACK COMMAND  -- TRANSACTIONS CONTROL

START TRANSACTION;  -- COMMAND TO START THE TRANSACTION COMMANDS
SAVEPOINT point_name;
ROLLBACK TO SAVEPOINT point_name;  -- IT UNDO ALL THE CHANGES AFTER THE SAVEPOINT
COMMIT; -- PERMANTLY SAVED IN MYSQL NO CHANGES ARE PERMITABLE
