---
id: 1
title: constitution-generation
stage: constitution
date: 2026-01-05
surface: agent
model: claude-sonnet-4-5-20250929
feature: none
branch: master
user: ecomw
command: /sp.constitution
labels: [constitution,spec-driven-development,architecture]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
 - .specify/memory/constitution.md
tests:
 - none
---

## Prompt

# Constitution Generation Prompt

You are creating the foundational principles and constraints for the Todo Evolution project. This constitution will govern all technical decisions throughout the 5 phases of development.

## Context
- Project: Todo app evolving from Python console to cloud-native AI chatbot
- Phases: 5 phases from console app to Kubernetes deployment
- Stack: Python 3.14, UV, FastAPI, Next.js, OpenAI Agents SDK, MCP, Kubernetes
- Approach: Spec-Driven Development using Claude Code

## Generate a Constitution Document that includes:

### 1. Core Principles (WHY we build this way)
Define the fundamental values that guide all decisions:
- Spec-driven development (no code without specs)
- AI-first architecture
- Cloud-native design
- User privacy and security
- Scalability from day one

### 2. Technical Constraints (WHAT we must/must not do)
Specify hard requirements:
- Python version: 3.14 exclusively
- Package manager: UV only (no pip allowed)
- Architecture: Monolithic repository structure
- Database: Neon Serverless PostgreSQL
- Frontend: Next.js 16 with App Router
- Backend: FastAPI with async/await
- Authentication: Better Auth with JWT
- AI: OpenAI Agents SDK + Official MCP SDK

### 3. Code Quality Standards
Define expectations for:
- Type hints (required for all Python functions)
- Documentation (docstrings mandatory)
- Testing (minimum coverage requirements)
- Error handling patterns
- Logging standards
- Security practices

### 4. Architecture Patterns
Specify preferred patterns:
- Stateless services with database persistence
- RESTful API design
- Event-driven architecture (Phases 4-5)
- MCP tools for AI interactions
- JWT-based authentication flow

### 5. Development Workflow
Define the process:
- Spec-Kit lifecycle: Specify → Plan → Tasks → Implement
- Git workflow and branching strategy
- Code review requirements
- Testing before merge
- Documentation updates

### 6. Performance Expectations
Set benchmarks for:
- API response times
- Database query optimization
- Frontend load times
- Kubernetes pod startup times
- Event processing latency

### 7. Security Requirements
Mandate security practices:
- No secrets in code
- Environment variables for configuration
- JWT token validation
- User data isolation
- SQL injection prevention
- XSS protection

### 8. Scalability Guidelines
Define scaling approach:
- Horizontal scaling readiness
- Stateless design principles
- Database connection pooling
- Caching strategies
- Load balancing preparation

### 9. DevOps Standards
Specify deployment practices:
- Containerization with Docker
- Helm charts for Kubernetes
- CI/CD pipeline requirements
- Monitoring and logging
- Health checks and readiness probes

### 10. AI Agent Guidelines
Define how AI agents should:
- Interact with MCP tools
- Handle conversation context
- Manage stateless operations
- Store conversation history
- Error handling and fallbacks

## Output Format
Create a markdown document titled `specs/constitution.md` with:
- Clear section headers
- Numbered principles
- Concrete examples where applicable
- Rationale for each major decision
- References to hackathon requirements

## Example Structure

## Response snapshot

# Todo Evolution Constitution

## Core Principles

### I. Spec-Driven Development (NON-NEGOTIABLE)
All code implementation must be preceded by corresponding specifications; No implementation without a spec, no spec without acceptance criteria; Features must be traceable from specification to implementation through task breakdown.

### II. AI-First Architecture
Design systems with AI agent integration as primary consideration; MCP tools must be first-class citizens in architecture; All business logic should be accessible through MCP interfaces for AI consumption.

### III. Cloud-Native Design
Build for containerization and orchestration from day one; Stateless services with externalized configuration; Design for horizontal scaling and resilience; Infrastructure as code with declarative manifests.

### IV. User Privacy and Security
User data isolation is mandatory; Security practices must be implemented at every layer; No secrets in code; JWT-based authentication with proper token validation; Zero-trust approach to data access.

### V. Scalability from Day One
Design for horizontal scaling readiness; Database connection pooling required; Stateless design principles; Caching strategies built-in from phase 1; Load balancing preparation.

### VI. Technology Stack Compliance
Python 3.14 exclusively for all environments; UV package manager only (no pip allowed); Monolithic repository structure maintained throughout all phases; Neon Serverless PostgreSQL as the database of record.

## Technical Constraints

### Python and Package Management
- Python version: 3.14 exclusively for all virtual environments
- Package manager: UV only (no pip usage allowed under any circumstances)
- Architecture: Monolithic repository structure (all phases in single repository)
- Type hints required for all Python functions

### Backend Requirements
- Backend framework: FastAPI with async/await patterns
- Database ORM: SQLModel for database operations
- Authentication: Better Auth with JWT tokens
- API design: RESTful patterns with async/await for all I/O operations

### Frontend Requirements
- Frontend framework: Next.js 16 with App Router
- Language: TypeScript for all frontend files
- Styling: Tailwind CSS only (no inline styles)
- Architecture: Server Components by default, Client Components only for interactivity

### AI and MCP Integration
- AI framework: OpenAI Agents SDK
- MCP SDK: Official Model Context Protocol SDK
- MCP tools must provide CRUD operations for tasks
- Conversation state must be persisted in database

## Code Quality Standards

### Documentation and Type Safety
- Type hints mandatory for all Python functions
- Docstrings required for all functions, classes, and modules
- API endpoints must have proper OpenAPI documentation
- Frontend components must have TypeScript interfaces defined

### Testing Requirements
- Unit tests for all business logic functions
- Integration tests for API endpoints
- Minimum 80% code coverage for Python backend
- Frontend component testing with Jest/Cypress

### Error Handling and Logging
- Proper exception handling with custom exceptions where appropriate
- Structured logging with appropriate log levels
- HTTPException for API error responses with proper status codes
- Graceful degradation for external service failures

### Security Practices
- Input validation and sanitization for all user inputs
- SQL injection prevention through ORM usage
- XSS protection through proper output encoding
- Authentication and authorization checks on all protected endpoints

## Architecture Patterns

### Service Design
- Stateless services with externalized state management
- RESTful API design with consistent endpoint patterns
- Async/await patterns for all I/O operations
- Dependency injection for service composition

### Data Management
- SQLModel for database ORM operations
- All database queries must be async
- User data isolation through user_id filtering
- Connection pooling for database operations

### MCP and AI Integration
- MCP tools as first-class interfaces for AI agents
- State management through database persistence
- Conversation history storage and retrieval
- Tool schemas must follow official MCP specifications

### Authentication Flow
- JWT-based authentication with proper token validation
- User session management through Better Auth
- Token refresh mechanisms for long-lived sessions
- Secure token storage and transmission

## Development Workflow

### Spec-Kit Lifecycle
- MANDATORY ORDER: constitution → Specify → Plan → Tasks → Implement
- Never write code without a corresponding task
- Never create tasks without a plan
- Never plan without specifications and constitution
- All changes must flow through the specification hierarchy

### Git Workflow
- Feature branches from main for all development
- Pull requests required for all merges
- Squash and merge for feature branches
- Semantic commit messages following conventional commits

### Code Review Requirements
- Minimum one reviewer approval for all PRs
- Automated tests must pass before review
- Security scanning required for all changes
- Architecture compliance verification

### Testing Before Merge
- All unit tests must pass
- Integration tests must pass
- Code coverage must not decrease
- Manual testing verification for UI changes

## Performance Expectations

### API Response Times
- 95th percentile API response time under 500ms
- Database query optimization required for queries over 100ms
- Caching strategies for frequently accessed data
- Connection pooling to minimize database overhead

### Database Performance
- All queries must use appropriate indexes
- Query optimization for complex joins
- Database connection pooling configuration
- Asynchronous queries for improved throughput

### Frontend Performance
- Page load time under 3 seconds
- Optimized bundle sizes through code splitting
- Image optimization and lazy loading
- Progressive web app capabilities

### Kubernetes Performance (Phases 4-5)
- Pod startup time under 30 seconds
- Horizontal pod autoscaling configuration
- Resource limits and requests properly set
- Health checks and readiness probes

## Security Requirements

### Secret Management
- No secrets in source code under any circumstances
- Environment variables for configuration management
- Secrets stored in secure vault or cloud secret management
- Configuration validation for required environment variables

### Authentication and Authorization
- JWT token validation on all protected endpoints
- Token expiration and refresh mechanisms
- User data isolation through proper authorization
- Session management through Better Auth

### Data Protection
- User data isolation through user_id filtering
- Input validation and sanitization
- SQL injection prevention through ORM usage
- XSS protection through proper output encoding

### API Security
- Rate limiting for API endpoints
- Proper CORS configuration
- Authentication token validation
- Secure transmission (HTTPS/TLS)

## Scalability Guidelines

### Horizontal Scaling
- Stateless service design to enable horizontal scaling
- Externalized session management
- Database connection pooling
- Load balancing preparation

### Database Scaling
- Connection pooling for database operations
- Read replicas for read-heavy operations
- Proper indexing for query optimization
- Database sharding preparation for future needs

### Caching Strategies
- Application-level caching for frequently accessed data
- Database query result caching
- CDN for static assets
- Cache invalidation strategies

### Load Distribution
- Horizontal pod autoscaling configuration
- Load balancer configuration
- Service mesh preparation for complex deployments
- Traffic routing and management

## DevOps Standards

### Containerization
- Docker containers for all services
- Multi-stage builds for optimized images
- Security scanning for container images
- Container registry management

### Kubernetes Deployment
- Helm charts for Kubernetes deployment
- Infrastructure as code with declarative manifests
- Health checks and readiness probes
- Monitoring and logging integration

### CI/CD Pipeline
- Automated testing in CI pipeline
- Security scanning integration
- Automated deployment to staging
- Manual approval for production deployment

### Monitoring and Observability
- Structured logging for all services
- Metrics collection for performance monitoring
- Distributed tracing for complex operations
- Alerting for critical system events

## AI Agent Guidelines

### MCP Tool Design
- MCP tools must follow official specifications
- Tools must provide CRUD operations for tasks
- Proper error handling and validation in tools
- Consistent response formats across all tools

### Conversation Management
- State management through database persistence
- Conversation history retrieval for context
- Message storage and retrieval patterns
- Context window management for AI agents

### AI Integration Patterns
- Stateless operations with database persistence
- Error handling and fallback strategies
- Tool schema validation
- Response formatting for AI consumption

### Agent Interaction
- Proper authentication for MCP tool access
- User data isolation in AI interactions
- Conversation context management
- Response validation and sanitization

## Governance

This constitution is the authoritative source for all technical decisions in the Todo Evolution project. All development activities must comply with these principles. Amendments require explicit documentation, team approval, and migration planning. The constitution supersedes all other practices and guides. All pull requests and code reviews must verify compliance with these principles. Complexity must be justified against these foundational principles. Use CLAUDE.md for runtime development guidance.

**Version**: 1.0.0 | **Ratified**: 2026-01-05 | **Last Amended**: 2026-01-05

## Outcome

- ✅ Impact: Created foundational constitution document for Todo Evolution project that will govern all technical decisions across 5 phases of development
- 🧪 Tests: none
- 📁 Files: .specify/memory/constitution.md
- 🔁 Next prompts: /sp.specify to create feature specifications
- 🧠 Reflection: The constitution establishes clear principles and constraints that will guide the project's evolution from Python console app to cloud-native AI chatbot

## Evaluation notes (flywheel)

- Failure modes observed: none
- Graders run and results (PASS/FAIL): N/A
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): Begin feature specification based on constitution principles