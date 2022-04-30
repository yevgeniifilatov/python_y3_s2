#!/usr/bin/python3

from random import randrange
import datetime as dt
from uuid import uuid4


class Ticket:

    def __init__(self):
        try:
            c = input("Enter N: ")
            self.cost = float(c) if c else 100.0
            self.ticket_id = uuid4().hex
        except ValueError:
            print("Error: incorrect input. Use only int or float")

    def compose(self, dat, td, evt):
        printable = "Ticket ID: %s\nEvent: %s\nEvent Date: %s\nPurchased on: %s\n" \
                    "Price: %i\n" % (self.ticket_id, evt, dat, td, self.cost)
        tkt = [self.ticket_id, self.cost, dat, td, printable]
        print(printable, tkt)
        return tkt


class TicketStudent(Ticket):

    def __init__(self):
        self.cost *= 0.5


class TicketBooth:

    def __init__(self):
        self.ticket_list = []
        events = ["Python Webinar", "Pottery class", "The Score world tour", "Apple keynote", "Hot Ones feat. MatPat"]
        dates = [dt.date(randrange(2023, 2029), randrange(1, 13), randrange(1, 29)) for i in range(len(events))]
        self.event_list = dict(zip(events, dates))
        self.td = dt.date.today()

    def create_ticket(self):
        [print(i+1, list(self.event_list.keys())[i], list(self.event_list.values())[i]) for i in range(5)]
        evt = int(input("Enter event number(1-5): ")) - 1
        std = int(input("Enter 1 if you are a student and 0 if not: "))
        print(list(self.event_list.keys()))
        if std:
            tmp = TicketStudent()
            ticket = tmp.compose(list(self.event_list.values())[evt], self.td, list(self.event_list.keys())[evt])
        else:
            tmp = Ticket()
            ticket = tmp.compose(list(self.event_list.values())[evt], self.td, list(self.event_list.keys())[evt])


if __name__ == '__main__':
    tb = TicketBooth()
    tb.create_ticket()
