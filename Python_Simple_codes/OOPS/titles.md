1. Classes and Objects
Class: A blueprint for creating objects. Defines a set of attributes and methods.
Object: An instance of a class. Represents a specific entity with the properties and behavior defined by the class.
2. Attributes and Methods
Attributes: Variables that belong to a class. They represent the state or data of an object.
Methods: Functions that belong to a class. They represent the behavior of an object.
3. Encapsulation
Private Attributes/Methods: Using underscores (_ or __) to indicate that attributes/methods are intended for internal use only.
Properties: Using @property decorator to control access to attributes, providing getter, setter, and deleter methods.
4. Inheritance
Single Inheritance: A class inherits attributes and methods from a single parent class.
Multiple Inheritance: A class inherits attributes and methods from multiple parent classes.
Method Overriding: Redefining a method in a subclass that was defined in a parent class.
5. Polymorphism
Method Overloading: Not directly supported in Python, but you can achieve similar functionality using default arguments.
Method Overriding: Same method name but different behavior in a subclass.
Duck Typing: Python’s dynamic typing allows you to use an object if it has the required methods and properties, regardless of its type.
6. Abstraction
Abstract Base Classes (ABCs): Using abc module to define abstract classes and methods that must be implemented by subclasses.
Interfaces: Achieved using ABCs to ensure certain methods are implemented in subclasses.
7. Constructors and Destructors
Constructor (__init__ method): A special method called when an object is instantiated.
Destructor (__del__ method): A special method called when an object is about to be destroyed (not commonly used).
8. Special Methods (Magic Methods)
__str__ and __repr__: For string representation of an object.
__len__, __getitem__, __setitem__, __delitem__: For making objects behave like collections.
Operator Overloading: Using methods like __add__, __sub__, __mul__, etc., to define behavior for operators.
9. Class and Static Methods
Class Methods (@classmethod): Methods that receive the class as the first argument (usually cls).
Static Methods (@staticmethod): Methods that do not receive the instance or class as the first argument.
10. Inheritance Hierarchies
Super() Function: Calling a method from a parent class.
MRO (Method Resolution Order): The order in which base classes are searched when executing a method.
11. Composition
Has-a Relationship: Building complex types by combining objects of other types, rather than inheriting from them.
12. Namespaces and Scope
Class Namespace: The space in which class attributes and methods are defined.
Instance Namespace: The space in which instance attributes and methods are defined.
13. Exception Handling
Try-Except Blocks: Handling exceptions in methods.
Custom Exceptions: Creating user-defined exception classes.
14. Design Patterns
Singleton: Ensuring a class has only one instance.
Factory: Creating objects without specifying the exact class.
Observer: Notifying objects about changes to other objects.
15. Advanced Topics
Metaclasses: Classes of classes. They define how classes behave.
Descriptors: Objects that define the behavior of attribute access.