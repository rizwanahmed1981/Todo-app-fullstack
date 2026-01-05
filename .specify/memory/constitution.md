<!--
Sync Impact Report:
Version change: 1.0.0 → 1.1.0
Modified principles: N/A (new constitution)
Added sections: Enhanced Frontend Requirements, JWT Authentication Details, API Endpoint Structure, Database Indexing Requirements
Removed sections: N/A
Templates requiring updates:
- .specify/templates/plan-template.md ✅ updated
- .specify/templates/spec-template.md ✅ updated
- .specify/templates/tasks-template.md ✅ updated
- .specify/templates/commands/*.md ✅ reviewed
Follow-up TODOs: None
-->

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
- All API endpoints must follow the pattern `/api/{user_id}/` to ensure proper user data isolation
- All endpoints require valid JWT token in Authorization header: `Authorization: Bearer <token>`
- Backend services must validate JWT tokens and extract user information for data filtering

### Frontend Requirements
- Frontend framework: Next.js 16 with App Router
- Language: TypeScript for all frontend files
- Styling: Tailwind CSS only (no inline styles)
- Architecture: Server Components by default, Client Components only for interactivity
- API calls must include JWT tokens in request headers for all authenticated endpoints
- Better Auth integration for user session management and JWT token acquisition

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
- JWT token validation on all protected endpoints
- User data isolation through proper authorization

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
- Database queries must use appropriate indexes for performance

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
- Frontend JWT tokens must be attached to all backend API requests
- Backend must validate JWT tokens and filter data by authenticated user ID

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
- Required indexes: tasks.user_id for user data filtering, tasks.completed for status filtering

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
- All API endpoints must filter data by authenticated user_id

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

**Version**: 1.1.0 | **Ratified**: 2026-01-05 | **Last Amended**: 2026-01-05