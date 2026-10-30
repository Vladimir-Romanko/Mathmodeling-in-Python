# Discrete Event Simulation: Post Office Queue

A small Python project that simulates a post office with **one service window** using a **discrete-event simulation (DES)** approach.

Instead of advancing time in fixed increments (`dt`), the simulation jumps directly to the next scheduled event. The system state changes only when an event occurs.

## Model description

The post office has a single service window and a FIFO (*first-in, first-out*) queue.

Each customer is described by three attributes:

- **ID** — the customer's unique number;
- **arrival time** — the time at which the customer arrives;
- **service duration** — how long the customer needs to be served.

The model follows these rules:

1. The service window is free at time `t = 0` and remains available throughout the simulation.
2. If a customer arrives while the window is free, service starts immediately.
3. If the window is busy, the customer joins the end of the FIFO queue.
4. When service finishes, the next customer in the queue starts service immediately. If the queue is empty, the window becomes free.
5. The simulation ends after all customers have arrived and completed service.

All arrival times and service durations are specified before the simulation starts. Time is continuous, but the simulation processes only event times.

## Events

The model uses two event types:

| Event | Meaning | Action |
|---|---|---|
| `ARRIVAL` | A customer arrives | Start service if the window is free; otherwise add the customer to the waiting queue. |
| `SERVICE_END` | A customer's service is completed | Start service for the next waiting customer, or make the window free if nobody is waiting. |

When a customer starts service at time `t_start`, the corresponding service-completion event is scheduled for:

```text
t_end = t_start + service_duration
```

This is important for customers who have to wait: their service end time is based on when service actually starts, not on their arrival time.

## Discrete-event simulation algorithm

The simulation follows this cycle:

1. Create the initial system state: the window is free, the waiting queue is empty, and the current time is zero.
2. Insert all customer-arrival events into the event queue.
3. Extract the event with the earliest timestamp.
4. Advance the simulation clock directly to that event's time.
5. Execute the event action. The action updates the system state and may schedule a new event.
6. Repeat until the event queue is empty.

There is no fixed time step and no loop that increments time by `dt`.

## Data structures and classes

- `STATE` — stores the current simulation time, the window status, and the FIFO waiting queue.
- `CLIENT` — stores a customer's ID, arrival time, and service duration.
- `EVENT` — provides time-based comparison for events in the priority queue.
- `ARRIVAL` — represents a customer arrival and implements its state transition.
- `SERVICE_END` — represents the end of service and either starts the next customer's service or frees the window.
- `EVENT_QUEUE` — wraps Python's `heapq` priority queue and returns the next event in chronological order.
- `collections.deque` — implements the FIFO queue of waiting customers.

The event queue and the customer waiting queue serve different purposes: the event queue orders future events by time, while the customer queue preserves the order in which waiting customers arrived.

## Input data

The example in the script defines eight customers. Each entry has the form:

```python
CLIENT(customer_id, arrival_time, service_duration)
```

| Customer | Arrival time (minutes) | Service duration (minutes) |
|---:|---:|---:|
| 1 | 0.1 | 3.0 |
| 2 | 1.0 | 4.0 |
| 3 | 2.5 | 5.1 |
| 4 | 3.0 | 1.2 |
| 5 | 4.0 | 5.7 |
| 6 | 4.4 | 10.0 |
| 7 | 5.7 | 3.3 |
| 8 | 6.8 | 6.3 |

To try another scenario, change the customer definitions in the main program. The times and durations are measured in minutes.

## How to run

The project uses only the Python standard library. No third-party packages are required.

1. Make sure Python 3 is installed.
2. Save the program to a file, for example `main.py`.
3. Run it from a terminal:

   ```bash
   python main.py
   ```

The program prints each processed event, the state of the service window, and the customers currently waiting in the queue. At the end, it prints the time when the last customer's service is completed.

## Result for the example input

For the eight customers listed above, the service schedule is:

| Customer | Service starts | Service ends |
|---:|---:|---:|
| 1 | 0.1 | 3.1 |
| 2 | 3.1 | 7.1 |
| 3 | 7.1 | 12.2 |
| 4 | 12.2 | 13.4 |
| 5 | 13.4 | 19.1 |
| 6 | 19.1 | 29.1 |
| 7 | 29.1 | 32.4 |
| 8 | 32.4 | 38.7 |

**The last customer finishes service at approximately `t = 38.7` minutes.** Python's floating-point arithmetic may display this value as `38.699999999999996`; this is a representation/rounding effect, not a scheduling error.

## Assumptions and current limitations

- The example assumes that no two events occur at exactly the same timestamp. The event queue currently orders events by time only and does not define a separate priority rule for simultaneous events (for example, an arrival occurring at exactly the same time as a service completion).
- The model uses predetermined customer arrival times and service durations; random arrivals and random service durations are not generated.
- The simulation reports the event log and the final completion time. It does not currently calculate additional performance statistics such as average waiting time or maximum queue length.

---

This project is a compact practice implementation of a discrete-event system: the clock advances from one event to the next, and event actions update the state and schedule future events.
