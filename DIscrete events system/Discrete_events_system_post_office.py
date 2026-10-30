"""
DISCRETE EVENTS SYSTEM 
This program simulates the operation of a post office with
a single service window. When customers arrive at the office,
one of two scenarios occurs:
1) The window is free: the customer proceeds directly to the
window and is served over a certain period of time.
2) The window is occupied: the customer joins a FIFO
(first-in, first-out) queue.

Each customer is defined by three attributes:
an ID number, an arrival time, and the duration of their service.
The service window opens at time t=0 and never closes for breaks.
The simulation concludes once the final customer has been served.

By Vladimir Romanko, October 2026.
"""
import heapq as he
from collections import deque

class STATE:
    ''' State of the post office   '''
    def __init__(self):
        self.window_open = True
        self.clients = 0
        self.t_current = 0
        self.client_queue = deque()
    def add_client(self,client):
        """ Adds a client in the queue """
        self.clients += 1
        self.client_queue.append(client)
    def pop_client(self):
        """ Delete (pop) a client in the queue """
        self.clients -= 1
        return self.client_queue.popleft()
    def __str__(self):
        """ Displays the status of the post office """
        if self.window_open == True:
            return ' Time ' + str(self.t_current) + ' window is free ' +\
                ' Clients in queue ' + str(self.clients)
        else:
            return ' Time ' + str(self.t_current) + ' window is busy ' +\
                ' Clients in queue ' + str(self.clients)

class CLIENT:
    def __init__(self,number,t_arrival,duration):
        self.number = number
        self.t = t_arrival
        self.d = duration
    def __lt__(self, other):
        """ Compares the client with another sorted by processing order priority """
        return self.t < other.t
    def __str__(self):
        return str(self.number)
             
        
class EVENT:
    def __lt__(self, other):
        """ Compares the event with another sorted by processing order priority """
        return self.t < other.t

class ARRIVAL(EVENT):
    ''' Event: arrival of a client      '''
    def __init__(self,client):
        self.t = client.t
        self.name = 'ARRIVAL'
        self.number = client.number
        self.d = client.d
        self.client = client
    def __str__(self):
        return self.name + ': Client number '+ str(self.number) +\
            ' arrival time is ' + str(self.t) + ' duration is ' + str(self.d)
    def action(self,queue,state):
        state.t_current = self.t
        if state.window_open == False:
            state.add_client( self.client )
        else:
            state.window_open = False
            queue.insert( SERVICE_END(self.client, self.t) )
             

class SERVICE_END(EVENT):
    ''' Event: ending of service of a client      '''
    def __init__(self,client, start_time):
        self.t = start_time + client.d
        self.name = 'SERVICE_END'
        self.number = client.number
        self.client = client
    def action(self,queue,state):
        state.t_current = self.t
        if state.clients > 0:
            next_client = state.pop_client()
            queue.insert( SERVICE_END(next_client, self.t) )
        else:
            state.window_open = True
            
    def __str__(self):
        return 'Ending of service of client number ' +\
            str(self.number)

class EVENT_QUEUE:
    def __init__(self):
        self.q = []
    def notEmpty(self):
        return len(self.q) > 0
    def remaining(self):
        return len(self.q)
    def insert(self,event):
        """  Create a new event in the queue    """
        he.heappush(self.q,event)
    def nextt(self):
        """ Returns and removes from the queue the next event to be processed"""
        return he.heappop(self.q)
    def __str__(self):
        if self.q:
            for i in range( len(self.q) ):
                print(self.q[i])
        return '--------'
   

'''      MAIN PROGRAM       '''

Q = EVENT_QUEUE() # Creating an event queue
# Creating a queue (stream) of customers at the Post Office
# Customer number; Arrival time (in minutes); Service time (in minutes)
Q.insert( ARRIVAL(CLIENT(1,0.1,3)) )
Q.insert( ARRIVAL(CLIENT(2,1,4)) )
Q.insert( ARRIVAL(CLIENT(3,2.5,5.1)) )
Q.insert( ARRIVAL(CLIENT(4,3,1.2)) )
Q.insert( ARRIVAL(CLIENT(5,4,5.7)) )
Q.insert( ARRIVAL(CLIENT(6,4.4,10)) )
Q.insert( ARRIVAL(CLIENT(7,5.7,3.3)) )
Q.insert( ARRIVAL(CLIENT(8,6.8,6.3)) )
    
print(Q);  print('--------')
S = STATE()
print('Initial state is:', S)
print('--------')
# Processing events until the queue is Q is empty
while Q.notEmpty():
    e = Q.nextt()
    assert e.t >= S.t_current
    print(e)
    e.action(Q,S)
    print('State after event:', S)
    if S.clients > 0:
        print('QUEUE OF CLIENTS:',end=' ')
        for client in S.client_queue:
            print(client, end=' ')
        print('')
    print('--------')
print('The last client was served at time',S.t_current)
    



