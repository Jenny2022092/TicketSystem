# This is a ticket class where user details are saved
class Ticket:
    # This is a Ticket class constructor
    def __init__(self, staffID, name, email, description):
        self.staffID = staffID
        self.name = name
        self.email = email
        self.description = description
        self.response = "Not Yet Provided"
        self.status = "Open"

    def __str__(self):
        return f"Ticket Number: {self.ticketNumber} \nTicket Creator: {self.name} \nStaff ID: {self.staffID} \nEmail Address: {self.email} \nDescription: {self.description} \nResponse: {self.response} \nTicket Status: {self.status}\n"


#This is a help desk class

class HelpDesk:
    ticketNumber = 2000
    openTickets = 0
    closedTickets = 0

# This is a HelpDesk class constructor
    def __init__(self):
        self.tickets = []

#This is a submit ticket function
    def submitTicket(self, staffID, name, email, description):
        newTicket = Ticket(staffID, name, email, description)
        self.tickets.append(newTicket)
        newTicket.ticketNumber = HelpDesk.ticketNumber
        HelpDesk.ticketNumber += 1
        #password change request are process in this if block
        if "Password Change" in description:
            newTicket.response = f"New Password: {staffID[:2]}{name[:3]}"
            HelpDesk.closedTickets += 1
            newTicket.status = "Closed"
        return newTicket

    # This is a respondToTicket function
    def respondToTicket(self, ticketNumber, response):
        for ticket in self.tickets:
            if ticket.ticketNumber == ticketNumber:
                ticket.response = response
                ticket.status = "Closed"

    # This is a reopenTicket function
    def reopenTicket(self, ticketNumber):
        for ticket in self.tickets:
            if ticket.ticketNumber == ticketNumber:
                ticket.status = "Reopened"

    # This is a displayTicket  function
    def displayTicket(self, ticketNumber):
        for ticket in self.tickets:
            if ticket.ticketNumber == ticketNumber:
                print(ticket)

#This displayStatistics function displays the stats of users ticket
    def displayStatistics(self):
        print(f"Number of tickets Created: {HelpDesk.ticketNumber - 2000} \nNumber of resolved tickets: {HelpDesk.closedTickets}  \nNumber of tickets to solve: {HelpDesk.openTickets}")



def main():
    # Creating object of HelpDesk class
    helpDesk = HelpDesk()
    print('\n\n------------Printing Tickets------------\n')
    # Passing parameters (which contains user id, name, email and query) in submitTicket function of HelpDesk class
    helpDesk.submitTicket("25896", "John", "john@gmail.com", "Password Change")
    helpDesk.submitTicket("36525", "Butler", "butler@gmail.com", "Password Change")
    helpDesk.submitTicket("19252", "Mike", "mike@gmail.com", "Password Change")
    # Passing parameters in respondToTicket function of HelpDesk class to response user query
    helpDesk.respondToTicket(2000, " New password generated: vnwdu87")
    helpDesk.respondToTicket(2001, " New password generated: abnegeu43")
    helpDesk.respondToTicket(2002, " New password generated: jemn90u")
    # Displaying tickets of user
    helpDesk.displayTicket(2000)
    helpDesk.displayTicket(2001)
    helpDesk.displayTicket(2002)
    print('\n\n------------Displaying Ticket Statistics------------\n')
    # Displaying user stats of tickets
    helpDesk.displayStatistics()


main()


