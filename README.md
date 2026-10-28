Crop Yield Monitoring System

1. Introduction

The Crop Yield Monitoring System is a simple Python application developed using Object-Oriented Programming (OOP) concepts. The system helps users record, display, search, and update information about crops and their yields.

The project focuses on agriculture and demonstrates how Python can be used to manage crop-monitoring records.

2. Objectives

The objectives of this project are to:

* Apply classes and objects in Python.
* Store multiple crop records using a list.
* Add and display crop records.
* Search for crop records using their IDs.
* Update actual crop yield and monitoring status.
* Demonstrate instance methods, class methods, and a static method.

3. System Features

The system provides the following features:

1. Display all crop records.
2. Add a new crop record.
3. Search for a crop record.
4. Update actual yield and crop status.
5. Count the total number of records.
6. Exit the program.

4. Technologies Used

* Programming language: Python
* Development environment: PyCharm
* Programming approach: Object-Oriented Programming
* Data structure: Python list
* Version control and sharing: GitHub

5. Project File Structure

* main.py — Controls the main program and menu.
* models.py — Defines the CropRecord and CropMonitoringSystem classes.
* input_handler.py — Collects and validates user input.
* output_handler.py — Displays menus, crop records, messages, and record counts.

6. How to Run the Program

1. Install Python on your computer.
2. Open the project folder in PyCharm.
3. Ensure all four Python files are in the same folder.
4. Open main.py.
5. Run the program.
6. Select an option from the displayed menu.

7. Example of Program Input and Output

Example Input

The user selects option 2 to add a crop record and enters the following information:

* Record ID: CR004
* Crop name: Groundnut
* Farm area: 3 hectares
* Expected yield: 2000 kg
* Actual yield: 1800 kg
* Status: Harvested

Example Output

Crop record added successfully.

When the user selects option 1, the system displays the stored crop records, including the newly added Groundnut record.

8. Object-Oriented Programming Concepts

Classes and Objects

The CropRecord class represents an individual crop record. The CropMonitoringSystem class manages the collection of crop records.

Objects are created from the CropRecord class and stored in a list managed by the monitoring system.

Attributes

The crop record attributes include record ID, crop name, farm area, expected yield, actual yield, and status.

Methods

The system uses methods to display and update crop information, add records, search for records, and count records.

Python Data Structure

A Python list stores multiple crop objects. This allows the program to manage and display several records.

Instance, Class, and Static Methods

The project includes instance methods for working with crop records, class methods for returning the system name and counting records, and a static method for validating yield values.

9. Digital Public Goods Alignment

Open Source

The project can be shared through GitHub so that others can inspect, learn from, and improve the code. An appropriate open-source licence should be included when publishing the project.

Inclusive and Accessible Design

The system uses a simple text-based menu with clearly numbered options, making it straightforward to use.

Privacy Respect

The program uses fictional sample crop records and does not require sensitive personal information.

Modular and Reusable Design

The code is divided into separate files for the main program, input handling, output handling, and class definitions. This makes the project easier to understand, maintain, and extend.

10. Limitations

The program stores records in memory using a Python list. Records are not permanently saved when the program closes. The system is a basic educational prototype and does not include a database or graphical user interface.

11. Conclusion

The Crop Yield Monitoring System demonstrates the practical application of Object-Oriented Programming in Python. It provides basic crop-record management functionality while demonstrating classes, objects, methods, lists, input validation, and modular programming.