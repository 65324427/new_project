---
name: "best-practices"
description: "Best practices and coding standards for software development. Invoke when user asks for best practices, coding standards, or code quality guidelines."
---

# Best Practices Guide

This skill provides comprehensive best practices and coding standards for software development.

## When to Invoke

- User asks for best practices
- User requests coding standards
- User wants code quality guidelines
- User mentions "code review" or "clean code"
- User asks for performance optimization
- User requests security guidelines
- User wants to follow industry standards

## Coding Standards

### 1. Naming Conventions
- Use descriptive names for variables, functions, and classes
- Follow language-specific conventions (PEP 8 for Python, camelCase for JavaScript)
- Avoid abbreviations unless widely understood
- Use verbs for function names (get, set, create, update, delete)
- Use nouns for class names (UserManager, APIHandler, Database)

### 2. Code Organization
- Group related functionality together
- Separate concerns (business logic, data access, presentation)
- Use modules and packages appropriately
- Keep files focused and single-purpose
- Follow project structure conventions

### 3. Documentation
- Add docstrings to all functions and classes
- Use inline comments for complex logic
- Document public APIs
- Provide usage examples
- Keep documentation up to date

### 4. Error Handling
- Use specific exceptions rather than generic ones
- Provide meaningful error messages
- Log errors appropriately
- Handle edge cases gracefully
- Validate inputs before processing

### 5. Testing
- Write unit tests for all functions
- Write integration tests for critical paths
- Test both positive and negative scenarios
- Maintain test coverage
- Use descriptive test names

### 6. Security
- Validate all user inputs
- Sanitize data before processing
- Use parameterized queries to prevent SQL injection
- Never log sensitive information
- Follow OWASP security guidelines
- Use HTTPS for all network communications

### 7. Performance
- Avoid unnecessary computations
- Use appropriate data structures
- Cache expensive operations
- Optimize database queries
- Use lazy loading where appropriate
- Profile code for bottlenecks

### 8. Version Control
- Use semantic versioning
- Write clear commit messages
- Follow branching strategies
- Use feature branches for new features
- Keep commit history clean

### 9. Code Review
- Review code before merging
- Use pull requests for discussions
- Provide constructive feedback
- Address all review comments
- Keep reviews professional and respectful

## Language-Specific Guidelines

### Python Best Practices
- Follow PEP 8 style guide
- Use type hints for better IDE support
- Use list comprehensions and generators
- Avoid global variables
- Use context managers for resource management
- Use f-strings for simple formatting
- Use `__main__` guard for module execution

### JavaScript Best Practices
- Use ES6+ features appropriately
- Use const and let for variables
- Use arrow functions for functional programming
- Avoid var (use let and const)
- Use template literals for multi-line strings
- Use async/await for asynchronous operations
- Handle promises properly

### Database Best Practices
- Use transactions for multi-step operations
- Index frequently queried columns
- Use parameterized queries
- Optimize N+1 queries
- Use connection pooling
- Handle connection errors gracefully

## Architecture Patterns

### 1. MVC Pattern
- Separate concerns (Model, View, Controller)
- Use dependency injection
- Keep business logic in models
- Keep views simple and focused

### 2. Repository Pattern
- Separate data access logic
- Use repository pattern for data operations
- Implement unit of work pattern
- Use transactions for consistency

### 3. Service Layer Pattern
- Separate business logic from data access
- Use service interfaces
- Implement caching where appropriate
- Handle service failures gracefully

### 4. Factory Pattern
- Use factory methods for object creation
- Encapsulate object creation logic
- Make dependencies explicit
- Support different implementations

## Common Anti-Patterns

### 1. Code Duplication
- Don't repeat code
- Extract common functionality into functions
- Use inheritance and composition
- Create utility classes

### 2. God Objects
- Avoid classes that do too many things
- Follow single responsibility principle
- Keep classes focused and cohesive
- Use composition over inheritance

### 3. Magic Numbers
- Avoid hardcoded numbers
- Use named constants
- Use configuration files
- Document magic numbers with comments

### 4. Spaghetti Code
- Avoid deeply nested conditionals
- Use early returns
- Extract complex conditions into functions
- Use guard clauses instead of nested if

## Code Quality Metrics

### 1. Cyclomatic Complexity
- Measure complexity of functions
- Keep complexity below 10 for simple functions
- Keep complexity below 20 for complex functions
- Refactor complex functions

### 2. Code Coverage
- Aim for 80%+ coverage
- Test critical paths thoroughly
- Cover edge cases
- Monitor coverage trends

### 3. Code Duplication
- Keep duplication below 5%
- Extract common functionality
- Use inheritance and composition
- Create utility classes

### 4. Technical Debt
- Track technical debt items
- Schedule regular refactoring
- Pay down debt before it accumulates
- Document debt decisions

## Security Best Practices

### 1. Input Validation
- Validate all user inputs
- Sanitize data before processing
- Use parameterized queries
- Validate file uploads
- Check for SQL injection

### 2. Authentication & Authorization
- Use strong password policies
- Implement rate limiting
- Use JWT or session-based auth
- Secure session storage
- Implement proper logout

### 3. Data Protection
- Encrypt sensitive data at rest
- Use HTTPS for all communications
- Never log sensitive information
- Implement proper access controls
- Follow GDPR and other privacy regulations

### 4. API Security
- Use API keys properly
- Implement rate limiting
- Validate API requests
- Use CORS appropriately
- Implement proper error responses
- Log API access for auditing

## Performance Optimization

### 1. Database Optimization
- Use indexes appropriately
- Optimize queries
- Use connection pooling
- Implement caching
- Use read replicas for scaling
- Partition large tables

### 2. Caching Strategies
- Cache expensive operations
- Use cache invalidation
- Implement cache warming
- Use appropriate cache TTL
- Monitor cache hit rates

### 3. Frontend Optimization
- Minimize HTTP requests
- Use lazy loading
- Implement code splitting
- Optimize images and assets
- Use service workers
- Implement progressive loading

### 4. Backend Optimization
- Use async operations
- Implement queue processing
- Use connection pooling
- Optimize algorithms
- Profile code regularly
- Use appropriate data structures

## Testing Best Practices

### 1. Unit Testing
- Test individual functions in isolation
- Use descriptive test names
- Test both positive and negative cases
- Mock external dependencies
- Keep tests fast and focused
- Maintain test coverage

### 2. Integration Testing
- Test component interactions
- Test API endpoints
- Test database operations
- Test user workflows
- Use test databases
- Test error handling

### 3. End-to-End Testing
- Test complete user flows
- Test critical paths
- Test performance under load
- Test security features
- Test cross-browser compatibility
- Use real test data

### 4. Test Automation
- Run tests in CI/CD
- Use test coverage reports
- Fail builds on test failures
- Generate test reports
- Integrate with issue tracking

## Deployment Best Practices

### 1. Environment Configuration
- Use environment variables
- Use configuration files
- Separate dev/staging/prod configs
- Never hardcode sensitive data
- Use secrets management
- Document all configuration options

### 2. CI/CD Pipeline
- Use automated testing
- Implement code quality gates
- Use automated deployment
- Monitor build performance
- Roll back failed deployments
- Use blue-green deployments

### 3. Monitoring
- Implement logging
- Monitor performance metrics
- Set up alerts
- Track errors and exceptions
- Monitor resource usage
- Use APM tools

### 4. Backup & Recovery
- Implement regular backups
- Test backup restoration
- Document backup procedures
- Monitor backup integrity
- Use off-site backups for critical data

## Documentation Best Practices

### 1. Code Documentation
- Document all public APIs
- Provide usage examples
- Document architecture decisions
- Keep documentation up to date
- Use diagrams for complex systems
- Document error codes

### 2. README Files
- Include project description
- Provide installation instructions
- Include usage examples
- Document configuration options
- Include troubleshooting section
- Add screenshots for UI projects
- Keep README concise and clear

### 3. API Documentation
- Document all endpoints
- Include request/response examples
- Document authentication methods
- Document error responses
- Document rate limits
- Include version information

### 4. Changelog
- Document all changes
- Use semantic versioning
- Categorize changes (added, fixed, removed, changed)
- Include migration notes
- Document breaking changes
- Link to related issues

## Code Review Checklist

### Before Submitting
- [ ] Code follows naming conventions
- [ ] Code is well-organized
- [ ] Functions have appropriate complexity
- [ ] Error handling is comprehensive
- [ ] Tests are included
- [ ] Documentation is updated
- [ ] No security vulnerabilities
- [ ] Performance is optimized
- [ ] No hardcoded values
- [ ] Code is properly formatted

### During Review
- [ ] Provide constructive feedback
- [ ] Address all review comments
- [ ] Suggest improvements
- [ ] Ask questions for clarification
- [ ] Be respectful and professional
- [ ] Focus on code quality, not style
- [ ] Consider long-term maintainability

### After Review
- [ ] Address all review comments
- [ ] Make necessary changes
- [ ] Update documentation
- [ ] Add tests if needed
- [ ] Update changelog
- [ ] Verify no regressions
- [ ] Close the review

## Common Pitfalls

### 1. Over-Engineering
- Don't over-design for future requirements
- Keep solutions simple and focused
- Avoid premature optimization
- Focus on current needs
- Use proven technologies

### 2. Under-Engineering
- Don't skip error handling
- Don't ignore security concerns
- Don't hardcode values
- Don't skip documentation
- Don't ignore performance
- Don't skip testing

### 3. Copy-Paste Programming
- Don't copy code without understanding
- Don't use code from untrusted sources
- Don't ignore licenses
- Don't skip attribution
- Don't violate terms of use

### 4. Premature Optimization
- Don't optimize without profiling
- Don't cache without invalidation
- Don't optimize readability for performance
- Don't optimize without testing
- Don't use micro-optimizations that hurt maintainability

## Tools and Automation

### 1. Code Quality Tools
- Linters: ESLint, Pylint, flake8
- Formatters: Prettier, Black, autopep8
- Static Analysis: SonarQube, CodeClimate
- Security Scanners: Bandit, Snyk
- Dependency Checkers: npm audit, pip-audit

### 2. Testing Tools
- Unit Testing: pytest, unittest, Jest
- Integration Testing: Selenium, Cypress
- E2E Testing: Playwright, Puppeteer
- API Testing: Postman, Insomnia
- Performance Testing: JMeter, k6

### 3. CI/CD Tools
- GitHub Actions
- GitLab CI
- CircleCI
- Travis CI
- Jenkins
- Azure DevOps
- AWS CodePipeline

### 4. Documentation Tools
- Sphinx (Python)
- JSDoc (JavaScript)
- Swagger/OpenAPI
- MkDocs
- Docusaurus
- GitBook

## Learning Resources

### 1. Books
- "Clean Code" by Robert C. Martin
- "Refactoring" by Martin Fowler
- "Design Patterns" by Gang of Four
- "The Pragmatic Programmer" by Andrew Hunt
- "Code Complete" by Steve McConnell

### 2. Online Courses
- Coursera
- edX
- Udacity
- Pluralsight
- freeCodeCamp
- Codecademy

### 3. Documentation
- Python Documentation
- MDN Web Docs
- JavaScript Documentation
- Stack Overflow
- GitHub Guides

### 4. Communities
- GitHub
- Stack Overflow
- Reddit (r/programming)
- Dev.to
- Hashnode
- Discord servers

## Conclusion

Following these best practices will help you:
- Write cleaner, more maintainable code
- Reduce bugs and security vulnerabilities
- Improve performance and user experience
- Make collaboration easier
- Build better software faster

Remember: Code quality is a journey, not a destination. Continuously improve and learn from your mistakes.