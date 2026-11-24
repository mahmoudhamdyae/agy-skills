---
name: add-job-event-listener
description: >-
  Laravel + Filament + HMVC Clean Architecture workflow: Move side effects, long-running tasks, and external API calls into Events, Listeners, and queued Jobs.
---

# Add Job Event Listener Flow

## Goal

Move side effects, long-running tasks, and external API calls into Events, Listeners, and queued Jobs.

## Mandatory Rules

- Use Jobs for long-running tasks or external API calls.
- Use Events to signal that something happened.
- Use Listeners to react to Events.
- Every side effect should have a separate Job or Listener.
- Jobs and Listeners should implement `ShouldQueue` by default unless low latency is strictly required.
- Do not send emails, SMS, notifications, or external requests directly from Controllers or Services.
- Add tests.

## Workflow

### 1. Plan

1. Identify the side effect.
2. Identify the triggering business event.
3. Decide whether the side effect should be:
    - Event + Listener
    - Direct Job dispatch
    - Multiple listeners
4. Identify payload data.
5. Identify retry/failure behavior.
6. Propose the async flow and wait for approval.

### 2. Implement

After approval only:

1. Create or update the Event.
2. Create or update the Listener.
3. Create or update the Job if needed.
4. Implement `ShouldQueue` unless explicitly justified otherwise.
5. Dispatch the Event from the correct Service after successful business operation.
6. Keep Controllers free of side effects.
7. Add tests for:
    - Event dispatch
    - Listener registration
    - Job dispatch
    - Failure cases where applicable

### 3. Review

1. Verify side effects are decoupled.
2. Verify queue behavior.
3. Verify tests pass.
4. Summarize:
    - Event added
    - Listener added
    - Job added
    - Queue behavior
    - Tests added
