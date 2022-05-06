#!/usr/bin/python3

from random import randrange
import datetime as dt
from uuid import uuid4
from os import path


class Ticket:

    def __init__(self):
        try:
            c = input("Enter N: ")
            self.cost = float(c) if c else 100.0
            self.ticket_id = uuid4().hex
        except ValueError:
            print("Error: incorrect input. Use only int or float")

    def compose(self, dat, td, evt):
        printable = "Ticket ID: %s;Event: %s;Event Date: %s;Purchased on: %s;" \
                    "Price: %i" % (self.ticket_id, evt, dat, td, self.cost)
        tkt = [self.ticket_id, self.cost, dat, td, printable]
        print(printable.replace(";", "\n"))
        return tkt


class TicketStudent(Ticket):

    def __init__(self):
        super().__init__()
        self.cost *= 0.5


class TicketPreorder(Ticket):

    def __init__(self):
        super().__init__()
        self.cost *= 0.7


class TicketLate(Ticket):

    def __init__(self):
        super().__init__()
        self.cost *= 1.2


class TicketBooth:

    def __init__(self):
        self.ticket_list = []
        events = ["Python Webinar", "Pottery class", "The Score world tour", "Apple keynote", "Hot Ones feat. MatPat"]
        dates = [dt.date(randrange(2023, 2029), randrange(1, 13), randrange(1, 29)) for i in range(len(events))]
        self.event_list = dict(zip(events, dates))
        self.td = dt.date.today()
        self.db_file = "./data.txt"

    def create_ticket(self):
        [print(i+1, list(self.event_list.keys())[i], list(self.event_list.values())[i]) for i in range(5)]
        evt = int(input("Enter event number(1-5): ")) - 1
        std = int(input("Enter 1 if you are a student and 0 if not: "))
        ds = list(self.event_list.values())[evt] - self.td
        if std:
            tmp = TicketStudent()
        elif ds.days > 90:
            tmp = TicketPreorder()
        elif ds.days < 7:
            tmp = TicketLate()
        else:
            tmp = Ticket()
        ticket = tmp.compose(list(self.event_list.values())[evt], self.td, list(self.event_list.keys())[evt])
        store = ','.join([str(e) for e in ticket])+"\n"
        with open(self.db_file, 'a') as file:
            file.write(store)

    def locate_tkt(self):
        if not path.exists(self.db_file) or path.getsize(self.db_file) <= 0:
            print("No tickets have been bought yet!")
            exit(0)
        tkt_id = input("Enter ticket ID: ")
        with open(self.db_file, "r") as file:
            for line in file:
                if tkt_id in line:
                    tkt = line.strip().split(",")[-1].replace(";", "\n")
                    print("Ticket found:\n", tkt)
                    break
            else:
                print("Ticket with ID %s doesn't exist" % tkt_id)


if __name__ == '__main__':
    tb = TicketBooth()
    action = int(input("Enter 1 to order ticket or 0 to search by ticket ID: "))
    if not action:
        tb.locate_tkt()
    else:
        tb.create_ticket()
