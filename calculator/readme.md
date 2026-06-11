# CSC426

## Project Overview
This project entails the development of a user-friendly, responsive desktop Graphical User Interface (GUI) calculator application. Built using the Python programming language and the native Tkinter GUI toolkit, the application delivers a modern, high contrast dark interface tailored to enhance readability and seamless user interactions.

## System Features & Specifications
Required Character Layout Mapping
The implementation natively incorporates a grid network mapping to the exact character specifications outlined in the course documentation:
**Basic Operators** : Addition (+), Subtraction (-), Multiplication (*), Division (/).  
**Specialized Operators**:Integer/Floor Division (\), Exponents/Power (^), Modulo Remainder (%).  
**Control Sequences**: Clear Display Buffer (C), Decimal Float Precision Placement (.), Operational Evaluation (=). 

## Architectural Specifications
**Framework**: Python 3.x with standard Tkinter primitives
**Layout Paradigm**: Dynamic CSS-style responsive grid matrix (5 rows $\times$ 4 columns)
**Interface Scheme**: Custom high-contrast dark aesthetic (#1e1e1e body backdrop, "#0b0f17" accent triggers).

## Algorithmic Source Code Breakdown
The application is structured around an object-oriented paradigm to cleanly separate layout construction from core calculation logic:

Global Mapping Architecture
button_layout = [
    ['C', '^', '%', '/'],
    ['7', '8', '9', '*'],
    ['4', '5', '6', '-'],
    ['1', '2', '3', '+'],
    ['0', '.', '\\', '=']
]

## Safety & Parsing Logic
To comply with Python's core processing interpreter while satisfying the user interface criteria, the application implements real-time dynamic token substitution before code compilation:

## Mapping standard assignment symbols to Python internal math operators
expr_to_eval = self.expression.replace('^', '**').replace('\\', '//')

## Advanced Exception Handling
The evaluation engine handles arithmetic instability gracefully using explicit catch boundaries:

ZeroDivisionError: Intercepts illegal operations where a divisor is exactly zero, returning an error prompt to prevent desktop stack freezes.

Exception: A fallback catchment mechanism for syntactical mismatches or trailing loose operators, cleaning the buffer state automatically.

### Empirical Test Verification Matrix
The engine was tested against multiple computational edge cases to verify arithmetic and logic integrity:

![alt text](image.png)


## Graphical Interface Execution Output
The interface renders as a highly scannable, adaptive interface. Below is the verified graphical production output of the active running module:

![alt text](image-1.png)

