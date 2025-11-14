# Company-Compensation-Report

A Python program to track, analyze, and summarize employee salaries per department.

What It Does

Lets you add departments and employees with their salaries.

Automatically detects the top-paid and lowest-paid employees in the company.

Calculates average salary per department.

Saves a JSON report for programmatic use and a readable TXT report for quick reference.

Provides a timestamped snapshot of the company’s payroll.

Features

Handles nested dictionaries (company[department][employee] = salary) to organize data.

Validates input to avoid negative or invalid salaries.

Supports any number of departments and employees.

Generates both JSON and human-readable reports.

How to Use

Run the program.

Enter the department name.

Add employee names and their salaries.

Type Done to finish a department, or Exit to quit entirely.

Once finished, the program calculates stats and saves reports as:

company_report.json

company_report.txt

Concepts Used

Loops and input handling

Nested dictionaries

Functions (average calculation)

Conditionals for top/bottom salary detection

File handling (JSON & TXT)

Datetime for timestamping

Why This Project

This project demonstrates the ability to:

Organize hierarchical data using nested dictionaries.

Perform real-world calculations and analytics.

Produce professional reports from user input.

Handle edge cases like invalid or negative salaries.
