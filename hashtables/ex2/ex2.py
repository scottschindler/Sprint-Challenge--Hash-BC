
#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = []

    # loop through scrambled tickets
    for ticket in tickets:
        # add to hashtable
        hash_table_insert(hashtable, ticket.source, ticket.destination)

    current_ticket = hash_table_retrieve(hashtable, 'NONE')
    route.append(current_ticket)

    # find order of tickers
    def sortTickets(ticket):
        if ticket == 'NONE':
            return

        # get next stop ticket
        next_ticket = hash_table_retrieve(hashtable, ticket)
        
        if next_ticket != 'NONE':
            # add to route
            route.append(next_ticket)
        
        # go to next ticket in trip
        return sortTickets(next_ticket)

    sortTickets(current_ticket)

    return route