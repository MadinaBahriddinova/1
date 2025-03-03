import math
import os
import json

# Vector Class
class Vector:
    def __init__(self, *components):
        self.components = components
    
    def __repr__(self):
        return f"Vector{self.components}"
    
    def __add__(self, other):
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must have the same dimensions for addition")
        return Vector(*(a + b for a, b in zip(self.components, other.components)))
    
    def __sub__(self, other):
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must have the same dimensions for subtraction")
        return Vector(*(a - b for a, b in zip(self.components, other.components)))
    
    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Vector(*(a * other for a in self.components))
        elif isinstance(other, Vector):
            if len(self.components) != len(other.components):
                raise ValueError("Vectors must have the same dimensions for dot product")
            return sum(a * b for a, b in zip(self.components, other.components))
        else:
            raise TypeError("Unsupported operand type")
    
    def magnitude(self):
        return math.sqrt(sum(a**2 for a in self.components))
    
    def normalize(self):
        mag = self.magnitude()
        if mag == 0:
            raise ValueError("Cannot normalize a zero vector")
        return Vector(*(a / mag for a in self.components))

# Employee Management System
class Employee:
    def __init__(self, employee_id, name, position, salary):
        self.employee_id = employee_id
        self.name = name
        self.position = position
        self.salary = salary
    
    def __repr__(self):
        return f"{self.employee_id}, {self.name}, {self.position}, {self.salary}"

class EmployeeManager:
    FILE_NAME = "employees.txt"

    def __init__(self):
        self.employees = self.load_employees()
    
    def load_employees(self):
        if not os.path.exists(self.FILE_NAME):
            return {}
        with open(self.FILE_NAME, "r") as file:
            return json.load(file)
    
    def save_employees(self):
        with open(self.FILE_NAME, "w") as file:
            json.dump(self.employees, file, indent=4)
    
    def add_employee(self, employee_id, name, position, salary):
        if employee_id in self.employees:
            print("Employee ID already exists!")
            return
        self.employees[employee_id] = {
            "name": name,
            "position": position,
            "salary": salary
        }
        self.save_employees()
        print("Employee added successfully!")
    
    def view_employees(self):
        for emp_id, data in self.employees.items():
            print(f"{emp_id}, {data['name']}, {data['position']}, {data['salary']}")
    
    def search_employee(self, employee_id):
        return self.employees.get(employee_id, "Employee not found")
    
    def update_employee(self, employee_id, name=None, position=None, salary=None):
        if employee_id not in self.employees:
            print("Employee not found!")
            return
        if name:
            self.employees[employee_id]["name"] = name
        if position:
            self.employees[employee_id]["position"] = position
        if salary:
            self.employees[employee_id]["salary"] = salary
        self.save_employees()
        print("Employee updated successfully!")
    
    def delete_employee(self, employee_id):
        if employee_id in self.employees:
            del self.employees[employee_id]
            self.save_employees()
            print("Employee deleted successfully!")
        else:
            print("Employee not found!")

# Example Usage
if __name__ == "__main__":
    manager = EmployeeManager()
    manager.add_employee("1001", "John Doe", "Software Engineer", 75000)
    manager.view_employees()
    print(manager.search_employee("1001"))
    manager.update_employee("1001", salary=80000)
    manager.delete_employee("1001")
