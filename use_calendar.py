import Calendar as calendar

# ----------------------------------------------------------------------------
# Functions dealing with the user. This is the calendar application.
# Please do use input and print as needed in order to provide a
# nice and meaningful user interaction with your application.
# ----------------------------------------------------------------------------


def user_interface():
    '''
    Load calendar.txt and then interact with the user. The user interface
    operates as follows, the text after command: is the command entered by the
    user.
    calendar loaded
    command: add 2017-10-21 budget meeting
    added
    command: add 2017-10-22 go to the gym
    added
    command: add 2017-10-23 go to the gym
    added
    command: add 2017-11-01 Make sure to submit csc108 assignment 2
    added
    command: add 2017-12-02 Make sure to submit csc108 assignment 3
    added
    command: add 2017-11-06 Term test 2
    added
    command: add 2017-10-29 Get salad stuff,lettuce, red peppers, green peppers
    added
    command: add 2017-11-06 Sid's birthday
    added
    command: show
	
        2017-10-21:
            0: budget meeting
        2017-10-22:
            0: go to the gym
        2017-10-23:
            0: go to the gym
        2017-10-29:
            0: Get salad stuff, leuttice, red peppers, green peppers
        2017-11-01:
            0: Make sure to submit csc108 assignment 2
        2017-11-06:
            0: Term test 2
            1: Sid's birthday
        2017-12-02:
            0: Make sure to submit csc108 assignment 3
    command: delete 2017-10-29 0
    deleted
    command: delete 2015-12-03 0
    2015-12-03 is not a date in the calendar
    command: delete 2017-12-02 0
    deleted
    command: show
	
        2017-10-21:
            0: budget meeting
        2017-10-22:
            0: go to the gym
        2017-10-23:
            0: go to the gym
        2017-11-01:
            0: Make sure to submit csc108 assignment 2
        2017-11-06:
            0: Term test 2
            1: Sid's birthday
    command: quit
    calendar saved

    :return: None
    '''
    # Your code goes here
    myCalendar = calendar.load_calendar()
    print("calendar loaded")
    while True:
        command = input("command: ")
        result = calendar.parse_command(command)
        if result[0] != "error":
            if result[0] == "quit":
                calendar.save_calendar(myCalendar)
                print("calendar saved")
                break
            elif result[0] == "help":
                help = calendar.command_help()
                print(help)
            elif result[0] == "add":
                calendar.command_add(result[1], result[2], myCalendar)
                print("added")
            elif result[0] == "show":
                show = calendar.command_show(myCalendar)
                print(show)
            elif result[0] == "delete":
                calendar.command_delete(result[1], int(result[2]), myCalendar)
                print("deleted")


if __name__ == "__main__":
    user_interface()
