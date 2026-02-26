---
name: "skill-template"
description: "Template for creating high-quality GitHub Skills. Use this as a starting point for your own skill development."
---

# GitHub Skill Template

This is a comprehensive template for creating GitHub Skills based on industry best practices.

## Skill Structure

### Required Frontmatter
```yaml
---
name: "your-skill-name"
description: "Brief description of what the skill does"
version: "1.0.0"
author: "Your Name"
tags: ["tag1", "tag2"]
---
```

### Required Sections

1. **When to Invoke** - When should this skill be triggered
2. **Description** - Detailed explanation of the skill's purpose
3. **Usage Examples** - Clear examples of how to use the skill
4. **Best Practices** - Guidelines for optimal performance
5. **Troubleshooting** - Common issues and solutions

## When to Invoke

Use this section to clearly define when the skill should be activated.

### Example
```markdown
## When to Invoke

- User asks for "code generation"
- User requests "help with coding"
- User mentions "create a function"
- User needs "write tests"
- User wants to "optimize code"
```

## Description

Provide a comprehensive description of what the skill does and how it works.

### Example
```markdown
## Description

This skill helps developers create high-quality, well-tested code through AI assistance. It includes:

- Code generation from natural language descriptions
- Code explanation and documentation
- Code optimization and refactoring
- Test case generation
- Bug detection and fixing
- Best practices enforcement

The skill uses advanced AI models to understand context and generate appropriate code solutions.
```

## Usage Examples

Provide clear, practical examples of how to use the skill.

### Example
```markdown
## Usage Examples

### Example 1: Code Generation
User: "Create a Python function that sorts a list of dictionaries by a specific key"

AI Response:
```python
def sort_by_key(data_list, sort_key):
    """
    Sort a list of dictionaries by a specific key.
    
    Args:
        data_list: List of dictionaries to sort
        sort_key: Key to sort by
    
    Returns:
        Sorted list of dictionaries
    """
    return sorted(data_list, key=lambda x: x[sort_key])

# Example usage
users = [
    {'name': 'Alice', 'age': 30},
    {'name': 'Bob', 'age': 25},
    {'name': 'Charlie', 'age': 35}
]

sorted_users = sort_by_key(users, 'age')
print(sorted_users)
# Output: [{'name': 'Bob', 'age': 25}, {'name': 'Alice', 'age': 30}, {'name': 'Charlie', 'age': 35}]
```

### Example 2: Code Explanation
User: "Explain what this function does"

AI Response:
```python
def calculate_factorial(n):
    """
    Calculate the factorial of a number using recursion.
    
    This function demonstrates:
    - Base case handling (n = 0 or n = 1)
    - Recursive function calls
    - Error handling for negative numbers
    
    Args:
        n: The number to calculate factorial for
    
    Returns:
        The factorial of n
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0 or n == 1:
        return 1
    return n * calculate_factorial(n - 1)
```

### Example 3: Test Generation
User: "Create unit tests for this function"

AI Response:
```python
import unittest

class TestFactorial(unittest.TestCase):
    """Test cases for the factorial function"""
    
    def test_factorial_positive(self):
        """Test with positive numbers"""
        self.assertEqual(calculate_factorial(5), 120)
        self.assertEqual(calculate_factorial(3), 6)
    
    def test_factorial_zero(self):
        """Test with zero"""
        self.assertEqual(calculate_factorial(0), 1)
    
    def test_factorial_negative(self):
        """Test with negative numbers"""
        with self.assertRaises(ValueError):
            calculate_factorial(-5)
```
```

## Best Practices

Follow these guidelines to create high-quality, maintainable skills.

### 1. Clear and Concise
- Use simple, direct language
- Avoid unnecessary complexity
- Focus on the core functionality
- Provide one clear solution rather than multiple alternatives

### 2. Well-Documented
- Include docstrings for all functions
- Add comments for complex logic
- Provide usage examples
- Explain the "why" not just the "how"

### 3. Error Handling
- Handle edge cases gracefully
- Provide meaningful error messages
- Use appropriate exception types
- Log errors for debugging

### 4. Testing
- Include test cases in the skill
- Test both positive and negative scenarios
- Verify edge cases
- Ensure code quality

### 5. Performance
- Consider time and space complexity
- Optimize for common use cases
- Avoid unnecessary computations
- Use appropriate data structures

### 6. Security
- Validate user inputs
- Sanitize data before processing
- Avoid code injection vulnerabilities
- Follow security best practices

### 7. Maintainability
- Use consistent naming conventions
- Follow language style guides
- Keep functions focused and single-purpose
- Avoid code duplication

### 8. User Experience
- Provide clear feedback
- Use appropriate progress indicators
- Handle errors gracefully
- Offer helpful suggestions

## Troubleshooting

Common issues and their solutions.

### Common Issues

1. **Skill Not Loading**
   - **Symptom**: Skill doesn't appear in the skill list
   - **Solution**: Check the frontmatter metadata
   - **Solution**: Verify the file is in the correct directory
   - **Solution**: Restart the IDE

2. **AI Not Responding**
   - **Symptom**: AI doesn't generate code
   - **Solution**: Check API key configuration
   - **Solution**: Verify network connection
   - **Solution**: Try a simpler prompt

3. **Code Not Working**
   - **Symptom**: Generated code has errors
   - **Solution**: Review the error messages
   - **Solution**: Check for syntax errors
   - **Solution**: Test the code in isolation

4. **Performance Issues**
   - **Symptom**: Skill runs slowly
   - **Solution**: Optimize algorithms
   - **Solution**: Reduce API calls
   - **Solution**: Cache results when appropriate

### Debugging Tips

1. **Check the AI response**: Review what the AI actually returned
2. **Test in isolation**: Run the code separately to verify it works
3. **Use logging**: Add print statements to track execution
4. **Review the context**: Ensure the AI has all necessary information
5. **Simplify the prompt**: Break down complex requests into smaller steps

## Advanced Features

Optional features that can enhance the skill.

### 1. Context Awareness
- Understand project structure
- Analyze existing code patterns
- Adapt to coding style
- Use appropriate libraries and frameworks

### 2. Multi-Language Support
- Support multiple programming languages
- Provide language-specific examples
- Handle language-specific syntax

### 3. Integration
- Work with existing tools
- Integrate with CI/CD pipelines
- Support team collaboration

### 4. Customization
- Allow user preferences
- Support custom templates
- Enable/disable specific features

## Example Complete Skill

Here's a complete example of a well-structured skill:

```markdown
---
name: "python-helper"
description: "Comprehensive Python coding assistance for common tasks"
version: "1.0.0"
author: "Your Name"
tags: ["python", "coding", "helper", "assistant"]
---

# Python Helper Skill

This skill provides comprehensive Python coding assistance for common development tasks.

## When to Invoke

- User asks for help with Python code
- User needs to create Python functions
- User wants to optimize Python code
- User requests Python code explanations
- User needs help with Python debugging
- User wants to write Python tests
- User asks for Python best practices

## Description

This skill assists with a wide range of Python development tasks:

### Code Generation
- Create functions from natural language descriptions
- Generate classes and methods
- Implement design patterns
- Create boilerplate code

### Code Explanation
- Explain how code works
- Document function purposes
- Describe algorithm complexity
- Provide usage examples

### Code Optimization
- Improve performance
- Refactor for readability
- Apply Pythonic idioms
- Remove code duplication

### Testing
- Generate unit tests
- Create integration tests
- Suggest test cases
- Help debug test failures

### Debugging
- Identify bugs and errors
- Provide solutions
- Suggest fixes
- Explain root causes

### Best Practices
- Follow PEP 8 guidelines
- Use type hints
- Write docstrings
- Add error handling
- Optimize for performance

## Usage Examples

### Example 1: Function Creation
User: "Create a function to validate email addresses"

AI Response:
```python
import re

def validate_email(email):
    """
    Validate an email address using regular expressions.
    
    Args:
        email (str): The email address to validate
    
    Returns:
        tuple: (is_valid: bool, error_message: str or None)
    """
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    if not email:
        return (False, "Email address is empty")
    
    if not re.match(pattern, email):
        return (False, "Invalid email format")
    
    return (True, None)

# Example usage
email = "user@example.com"
is_valid, error = validate_email(email)

if is_valid:
    print(f"✅ Email is valid: {email}")
else:
    print(f"❌ {error}")
```

### Example 2: Class Creation
User: "Create a class to manage user data"

AI Response:
```python
class UserManager:
    """
    A class to manage user data with CRUD operations.
    
    Attributes:
        users (dict): Dictionary to store user data
        next_id (int): Counter for generating unique user IDs
    """
    
    def __init__(self):
        self.users = {}
        self.next_id = 1
    
    def create_user(self, username, email, password):
        """
        Create a new user.
        
        Args:
            username (str): User's username
            email (str): User's email
            password (str): User's password
        
        Returns:
            dict: User data with ID
        """
        user_id = f"user_{self.next_id}"
        self.users[user_id] = {
            'id': user_id,
            'username': username,
            'email': email,
            'password': password,
            'created_at': datetime.now().isoformat()
        }
        self.next_id += 1
        
        return self.users[user_id]
    
    def get_user(self, user_id):
        """
        Retrieve user data by ID.
        
        Args:
            user_id (str): User's ID
        
        Returns:
            dict: User data or None
        """
        return self.users.get(user_id)
    
    def update_user(self, user_id, **kwargs):
        """
        Update user data.
        
        Args:
            user_id (str): User's ID
            **kwargs: Fields to update
        
        Returns:
            bool: True if successful, False otherwise
        """
        if user_id not in self.users:
            return False
        
        self.users[user_id].update(kwargs)
        return True
    
    def delete_user(self, user_id):
        """
        Delete user by ID.
        
        Args:
            user_id (str): User's ID
        
        Returns:
            bool: True if successful, False otherwise
        """
        if user_id not in self.users:
            return False
        
        del self.users[user_id]
        return True

# Example usage
manager = UserManager()

# Create a user
user1 = manager.create_user("alice", "alice@example.com", "password123")
print(f"Created user: {user1}")

# Get user
retrieved_user = manager.get_user(user1['id'])
print(f"Retrieved user: {retrieved_user}")

# Update user
manager.update_user(user1['id'], email="newalice@example.com")
print(f"Updated user: {manager.get_user(user1['id'])}")

# Delete user
manager.delete_user(user1['id'])
print(f"Deleted user: {user1['id']}")
```

### Example 3: Test Generation
User: "Create unit tests for the UserManager class"

AI Response:
```python
import unittest
from datetime import datetime

class TestUserManager(unittest.TestCase):
    """Test cases for UserManager class"""
    
    def setUp(self):
        self.manager = UserManager()
    
    def test_create_user(self):
        """Test user creation"""
        user = self.manager.create_user("testuser", "test@example.com", "pass123")
        self.assertIn('id', user)
        self.assertEqual(user['username'], "testuser")
        self.assertEqual(user['email'], "test@example.com")
    
    def test_get_user(self):
        """Test user retrieval"""
        user = self.manager.create_user("testuser", "test@example.com", "pass123")
        retrieved = self.manager.get_user(user['id'])
        self.assertEqual(retrieved['username'], "testuser")
    
    def test_update_user(self):
        """Test user update"""
        user = self.manager.create_user("testuser", "test@example.com", "pass123")
        result = self.manager.update_user(user['id'], username="updateduser")
        self.assertTrue(result)
        updated = self.manager.get_user(user['id'])
        self.assertEqual(updated['username'], "updateduser")
    
    def test_delete_user(self):
        """Test user deletion"""
        user = self.manager.create_user("testuser", "test@example.com", "pass123")
        result = self.manager.delete_user(user['id'])
        self.assertTrue(result)
        retrieved = self.manager.get_user(user['id'])
        self.assertIsNone(retrieved)

if __name__ == '__main__':
    unittest.main()
```

## Best Practices

### 1. Clear and Concise
- Use simple, direct language
- Avoid unnecessary complexity
- Focus on the core functionality
- Provide one clear solution rather than multiple alternatives
- Keep functions focused and single-purpose
- Use meaningful variable and function names

### 2. Well-Documented
- Include docstrings for all functions and classes
- Add comments for complex logic
- Provide usage examples
- Explain the "why" not just the "how"
- Document algorithm complexity (time/space)
- Include type hints for better IDE support

### 3. Error Handling
- Handle edge cases gracefully (empty inputs, None values)
- Provide meaningful error messages
- Use appropriate exception types (ValueError, TypeError, etc.)
- Validate user inputs before processing
- Log errors for debugging with print statements
- Use try-except blocks for error handling
- Consider using custom exceptions for domain-specific errors

### 4. Testing
- Include test cases in the skill
- Test both positive and negative scenarios
- Verify edge cases (empty strings, zero values, boundary conditions)
- Ensure code quality and style
- Use descriptive test method names
- Follow AAA pattern (Arrange, Act, Assert)
- Test in isolation, not integration with other code

### 5. Performance
- Consider time and space complexity in docstrings
- Optimize for common use cases
- Avoid unnecessary computations and loops
- Use appropriate data structures (lists vs sets, dictionaries)
- Consider caching for expensive operations
- Use generators for large datasets
- Profile code if performance is critical

### 6. Security
- Validate user inputs (email format, password strength)
- Sanitize data before processing
- Avoid code injection vulnerabilities
- Use parameterized queries instead of string concatenation
- Follow security best practices (OWASP guidelines)
- Never log or expose sensitive data
- Use environment variables for secrets

### 7. Maintainability
- Use consistent naming conventions (PEP 8 for Python)
- Follow language style guides
- Keep functions focused and single-purpose
- Avoid code duplication (DRY principle)
- Use meaningful variable and function names
- Organize code logically (imports, constants, classes, functions)
- Add type hints for better IDE support
- Use relative imports when possible

### 8. User Experience
- Provide clear feedback messages
- Use appropriate progress indicators
- Handle errors gracefully with helpful messages
- Offer suggestions and alternatives
- Provide usage examples
- Make the skill easy to understand and use
- Consider adding interactive features for complex tasks

## Troubleshooting

Common issues and their solutions.

### Common Issues

1. **Skill Not Loading**
   - **Symptom**: Skill doesn't appear in the skill list
   - **Solution**: Check the frontmatter metadata
   - **Solution**: Verify the file is in the correct directory
   - **Solution**: Restart the IDE
   - **Solution**: Check the file extension is .md not .md.txt

2. **AI Not Responding**
   - **Symptom**: AI doesn't generate code
   - **Solution**: Check API key configuration
   - **Solution**: Verify network connection
   - **Solution**: Try a simpler prompt
   - **Solution**: Check if the AI model supports the requested task
   - **Solution**: Review the AI response for errors

3. **Code Not Working**
   - **Symptom**: Generated code has errors
   - **Solution**: Review the error messages
   - **Solution**: Check for syntax errors
   - **Solution**: Test the code in isolation
   - **Solution**: Check for missing imports or dependencies
   - **Solution**: Verify the code matches the language syntax
   - **Solution**: Add error handling for edge cases

4. **Performance Issues**
   - **Symptom**: Skill runs slowly
   - **Solution**: Optimize algorithms
   - **Solution**: Reduce API calls
   - **Solution**: Cache results when appropriate
   - **Solution**: Use more efficient data structures
   - **Solution**: Profile code to identify bottlenecks
   - **Solution**: Consider async operations for I/O bound tasks

5. **Context Issues**
   - **Symptom**: AI doesn't understand the project context
   - **Solution**: Provide more context in the prompt
   - **Solution**: Include relevant code snippets
   - **Solution**: Explain the project structure
   - **Solution**: Reference specific files or functions
   - **Solution**: Use more specific language

### Debugging Tips

1. **Check the AI Response**
   - Review what the AI actually returned
   - Look for error messages in the response
   - Verify the response format is correct
   - Check if the code is complete and not truncated

2. **Test in Isolation**
   - Run the generated code separately
   - Create a minimal test case
   - Verify the output matches expectations
   - Test with different input values

3. **Use Logging**
   - Add print statements to track execution
   - Log intermediate values
   - Log error conditions
   - Use logging module for production code
   - Include timestamps in log messages

4. **Review the Context**
   - Ensure the AI has all necessary information
   - Check if file paths are correct
   - Verify imports are available
   - Review the project structure
   - Consider the coding style and conventions

5. **Simplify the Prompt**
   - Break down complex requests into smaller steps
   - Be more specific about requirements
   - Provide examples of desired output
   - Use clear, unambiguous language
   - Ask for clarification if the request is unclear

## Advanced Features

Optional features that can enhance the skill.

### 1. Context Awareness
- Understand project structure
- Analyze existing code patterns
- Adapt to coding style
- Use appropriate libraries and frameworks
- Recognize common patterns and idioms

### 2. Multi-Language Support
- Support multiple programming languages
- Provide language-specific examples
- Handle language-specific syntax
- Use appropriate standard libraries

### 3. Integration
- Work with existing tools
- Integrate with CI/CD pipelines
- Support team collaboration
- Provide configuration options

### 4. Customization
- Allow user preferences
- Support custom templates
- Enable/disable specific features
- Provide user settings management

## Version History

Track changes and improvements to the skill.

### Version 1.0.0 (2026-02-26)
- Initial release
- Basic skill template
- Core functionality
- Best practices documentation

### Future Enhancements
- Add more language support
- Improve error handling
- Add more examples
- Enhance documentation
- Add interactive features
- Improve performance

## Contributing

How to contribute improvements to this skill.

### Contribution Guidelines
- Follow the existing code style
- Add tests for new features
- Update documentation
- Use clear commit messages
- Follow semantic versioning
- Submit pull requests with descriptions

### Pull Request Process
1. Fork the repository
2. Create a new branch for your feature
3. Make your changes
4. Add tests for new features
5. Update documentation
6. Submit a pull request with a clear description

### Code Review Checklist
- [ ] Code follows best practices
- [ ] Tests are included
- [ ] Documentation is updated
- [ ] No breaking changes
- [ ] Commit message is clear
- [ ] Version is updated

## License

Specify the license for this skill.

### License
MIT License

Copyright (c) 2026 Your Name

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies
or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED,
INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.