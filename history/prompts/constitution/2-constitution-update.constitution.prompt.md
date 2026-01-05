---
id: 2
title: constitution-update
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
 - specs/constitution.md
tests:
 - none
---

## Prompt

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
Todo Evolution - Project Constitution
1. Core Principles
1.1 Spec-Driven Development
Principle: No code shall be written without a corresponding specification and task.
Rationale: Prevents scope creep, ensures alignment, enables AI agents to work deterministically.
Implementation:

Every feature begins in speckit.specify
Architecture documented in speckit.plan
Work broken into speckit.tasks
Code references Task IDs

1.2 Python 3.14 Exclusively
Principle: All virtual environments must use Python 3.14.
Rationale: Ensures consistency, leverages latest features, prevents version conflicts.
Enforcement:

uv venv --python 3.14 for all environments
CI/CD checks Python version
No exceptions allowed


Generate the complete constitution now.

## Response snapshot

The constitution has been successfully created with all 10 required sections. The document establishes the foundational principles for the Todo Evolution project, covering:

1. Core Principles - Spec-driven development, AI-first architecture, cloud-native design, privacy/security, scalability, and technology stack compliance
2. Technical Constraints - Python 3.14, UV package manager, monolithic architecture, and all specified technology requirements
3. Code Quality Standards - Type hints, documentation, testing requirements, error handling, and security practices
4. Architecture Patterns - Stateless services, RESTful design, MCP tools, and JWT authentication
5. Development Workflow - Spec-Kit lifecycle, Git workflow, code review requirements
6. Performance Expectations - API response times, database performance, frontend performance, and Kubernetes performance
7. Security Requirements - Secret management, authentication, data protection, and API security
8. Scalability Guidelines - Horizontal scaling, database scaling, caching strategies, and load distribution
9. DevOps Standards - Containerization, Kubernetes deployment, CI/CD, and monitoring
10. AI Agent Guidelines - MCP tool design, conversation management, and agent interaction patterns

The constitution is now in place to govern all technical decisions throughout the 5 phases of the Todo Evolution project.

## Outcome

- ✅ Impact: Created comprehensive constitution document that establishes foundational principles for the Todo Evolution project across all 5 development phases
- 🧪 Tests: none
- 📁 Files: .specify/memory/constitution.md, specs/constitution.md
- 🔁 Next prompts: /sp.specify to begin creating feature specifications based on constitution principles
- 🧠 Reflection: The constitution provides a solid foundation for spec-driven development and ensures consistent implementation across all phases of the project

## Evaluation notes (flywheel)

- Failure modes observed: none
- Graders run and results (PASS/FAIL): N/A
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): Begin feature specification process using the established constitution