# python-best-practices
Highlights the focus on best practices in Python programming

## Naming Conventions

Python code should follow clear naming conventions as defined in PEP 8. Good naming is crucial for:
- Code readability
- Maintainability
- Self-documentation
- Team collaboration

### Key Principles

1. **Descriptiveness**: Names should describe the purpose
2. **Consistency**: Follow established patterns
3. **Length vs Clarity**: Balance brevity with clarity

### Convention Summary

- `snake_case` for functions, methods, variables
- `CapWords` for classes
- `UPPER_CASE` for constants
- `_single_leading_underscore` for protected attributes
- `__double_leading_underscore` for name mangling

See `examples/naming.py` for practical examples.

## Type Hints

Python's type hints provide several key benefits:

### Benefits
- Early error detection
- Better IDE support and code completion
- Self-documenting code
- Easier refactoring
- Enhanced code maintainability

### Best Practices
- Use type hints consistently
- Leverage `Optional` for nullable values
- Create type aliases for complex types
- Enable strict mypy checking

### TypedDict vs Pydantic BaseModel

When working with structured data in Python, you have two main approaches:

#### TypedDict
- Pure typing solution with no runtime overhead
- Only provides type checking during development
- No data validation at runtime
- No data conversion
- Best for: Internal data structures where types are known

Example:
```python
from typing import TypedDict

class UserDict(TypedDict):
    name: str
    age: int

# Only type checking, no runtime validation
user: UserDict = {"name": "John", "age": "30"}  # Type error but works at runtime
```

#### Pydantic BaseModel
- Full data validation at runtime
- Automatic type conversion
- JSON serialization/deserialization
- Data validation with custom rules
- Best for: API interfaces, configuration, data validation

Example:
```python
from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int

# Runtime validation and type conversion
user = User(name="John", age="30")  # Converts "30" to int, or raises error if invalid
```

Choose TypedDict when:
- You need pure type checking without runtime overhead
- Working with internal data structures
- Types are known and controlled

Choose Pydantic when:
- Handling external data (APIs, files, etc.)
- Need runtime validation
- Want automatic type conversion
- Building data models with validation rules

See `examples/typing_guide.py` for TypedDict examples.

See `examples/typing_guide.py` for practical examples.
