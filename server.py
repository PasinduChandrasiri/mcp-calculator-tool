"""
🚀 Advanced FastMCP Calculator Tool

Run this server using:
    uv run server.py

Then connect it in Claude Desktop using your mcp.json config.

Features:
- 🧮 Basic Math: add, subtract, multiply, divide
- 🧠 Advanced Math: power, square root, factorial, percentage, BMI
- 📊 Summary tool: multiple operations at once
- 💬 Greeting resource & styled greeting prompt
"""

from math import sqrt, factorial
from mcp.server.fastmcp import FastMCP

# 🌟 Create the MCP server
mcp = FastMCP("AdvancedCalculatorMCP", description="An intelligent math and greeting MCP server.")


# 🧮 Basic Math Tools
@mcp.tool()
def add(a: float, b: float) -> float:
    """Add two numbers."""
    return a + b

@mcp.tool()
def subtract(a: float, b: float) -> float:
    """Subtract b from a."""
    return a - b

@mcp.tool()
def multiply(a: float, b: float) -> float:
    """Multiply two numbers."""
    return a * b

@mcp.tool()
def divide(a: float, b: float) -> float:
    """Divide a by b (with zero check)."""
    if b == 0:
        raise ValueError("Division by zero is not allowed.")
    return a / b


# 🧠 Advanced Math Tools
@mcp.tool()
def power(base: float, exponent: float) -> float:
    """Raise a number to a power."""
    return base ** exponent

@mcp.tool()
def square_root(x: float) -> float:
    """Compute the square root of a number (non-negative)."""
    if x < 0:
        raise ValueError("Cannot take square root of a negative number.")
    return sqrt(x)

@mcp.tool()
def factorial_tool(n: int) -> int:
    """Calculate the factorial of a non-negative integer."""
    if n < 0:
        raise ValueError("Factorial is only defined for non-negative integers.")
    return factorial(n)

@mcp.tool()
def percentage(part: float, whole: float) -> float:
    """Calculate what percentage `part` is of `whole`."""
    if whole == 0:
        raise ValueError("Cannot divide by zero.")
    return (part / whole) * 100

@mcp.tool()
def bmi(weight_kg: float, height_m: float) -> float:
    """Calculate Body Mass Index (BMI) = weight / height²."""
    if height_m <= 0:
        raise ValueError("Height must be greater than zero.")
    return weight_kg / (height_m ** 2)


# 📊 Summary Tool
@mcp.tool()
def math_summary(a: float, b: float) -> dict:
    """Return a summary of multiple math operations on two numbers."""
    return {
        "add": a + b,
        "subtract": a - b,
        "multiply": a * b,
        "divide": a / b if b != 0 else "undefined",
        "power": a ** b
    }


# 🌐 Greeting Resource
@mcp.resource("greeting://{name}")
def greeting(name: str) -> str:
    """Get a personalized greeting message."""
    return f"👋 Hello {name}, welcome to the Advanced Calculator MCP!"


# 💬 Greeting Prompt
@mcp.prompt()
def greet_user(name: str, style: str = "friendly") -> str:
    """Generate a greeting prompt in different styles."""
    styles = {
        "friendly": f"Hey {name}! 😊 Hope you’re having a great day!",
        "formal": f"Good day, {name}. It’s a pleasure to meet you.",
        "casual": f"Yo {name}! 👋 What’s up?",
    }
    return styles.get(style, styles["friendly"])


# 🏁 Run the MCP server
if __name__ == "__main__":
    print("🚀 Starting Advanced Calculator MCP Server...")
    mcp.run()
