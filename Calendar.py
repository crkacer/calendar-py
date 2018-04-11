import os
'''

IMPORTANT NOTE: Do NOT change any of the function names or their signatures
(the parameters they take).
Your functions must behave exactly as described. Please check correctness by
running DocTests  included in function headers. You may not use any print or
input statements in your code.

Manage a calendar database.

A calendar is a dictionary keyed by date ("YYYY-MM-DD") with value being a list
of strings, the events on the specified date.

Example:
calendar["2017-10-12"] # is a list of events on "2017-10-12"

calendar["2017-10-12"]==["Eye doctor", "lunch with sid", "dinner with jane"]
'''


# -----------------------------------------------------------------------------
# Please implement the following calendar commands
# -----------------------------------------------------------------------------

def command_help():
    '''
    () -> str
    This function is already implemented. Please do not change it.
    Returns a help message for the system. That is...
    '''

    help = """
    Help for Calendar. The calendar commands are

    add DATE DETAILS               add the event DETAILS at the specified DATE
    show                           show all events in the claendar
    delete DATE NUMBER             delete the specified event (by NUMBER) from
                                   the calendar
    quit                           quit this program
    help                           display this help message

    Examples: user data follows command:

    command: add 2017-10-12 dinner with jane
    added

    command: show
        2017-10-12:
            0: Eye doctor
            1: lunch with sid
            2: dinner with jane
        2017-10-29:
            0: Change oil in blue car
            1: Fix tree near front walkway
            2: Get salad stuff, leuttice, red peppers, green peppers
        2017-11-06:
            0: Sid's birthday

    command: delete 2017-10-29 2
    deleted

    A DATE has the form YYYY-MM-DD, for example
    2017-12-21
    2016-01-02

    Event DETAILS consist of alphabetic characters,
    no tabs or newlines allowed.
    """
    return help


def command_add(date, event_details, calendar):
    '''
    (str, str, dict) -> str
    Add event_details to the list at calendar[date]
    Create date if it was not there

    date: A string date formatted as "YYYY-MM-DD"
    event_details: A string describing the event
    calendar: The calendar database
    return: empty string

    >>> calendar = {}
    >>> command_add("2017-02-28", "Python class", calendar)
    ''
    >>> calendar == {'2017-02-28': ['Python class']}
    True
    >>> command_add("2017-03-11", "CSCA08 test 2", calendar)
    ''
    >>> calendar == {'2017-03-11': ['CSCA08 test 2'], '2017-02-28':\
    ['Python class']}
    True
    >>> command_add("2017-03-11", "go out with friends after test", calendar)
    ''
    >>> calendar == {'2017-03-11': ['CSCA08 test 2', \
    'go out with friends after test'], '2017-02-28': ['Python class']}
    True
    >>>

    '''

    # YOUR CODE GOES HERE

    if date not in calendar:
        calendar[date] = []

    calendar[date].append(event_details)
    return ''


def command_show(calendar):
    r'''
    (dict) -> str
    Returns the list of events for calendar sorted in increasing date order
    as a string, see examples below for a sample formatting
    calendar: the database of events

    Example:
    >>> calendar = {}
    >>> command_add("2017-02-12", "Eye doctor", calendar)
    ''
    >>> command_add("2017-02-12", "lunch with sid", calendar)
    ''
    >>> command_add("2017-03-29", "Change oil in blue car", calendar)
    ''
    >>> command_add("2017-02-12", "dinner with Jane", calendar)
    ''
    >>> command_add("2017-03-29", "Fix tree near front walkway", calendar)
    ''
    >>> command_add("2017-03-29", "Get salad stuff", calendar)
    ''
    >>> command_add("2017-05-06", "Sid's birthday", calendar)
    ''
    >>> command_show(calendar)
    "\n    2017-02-12:\n        0: Eye doctor\n        1: lunch with sid\n        2: dinner with Jane\n    2017-03-29:\n        0: Change oil in blue car\n        1: Fix tree near front walkway\n        2: Get salad stuff\n    2017-05-06:\n        0: Sid's birthday"
    '''
    # Hint: Don't use \t (the tab character) to indent, or DocTest will fail
    # in the above testcase.
    # Put 4 spaces before the date, 8 spaces before each item.
    result = ""
    for date in calendar:
        result += "\n    " + date + ":"
        index = 0
        for event in calendar[date]:
            result += "\n        " + str(index) + ": " + event
            index += 1
    return result

def command_delete(date, entry_number, calendar):
    '''
    (str, int, dict) -> str
    Delete the entry at calendar[date][entry_number]
    If calendar[date] is empty, remove this date from the calendar.
    If the entry does not exist, do nothing
    date: A string date formatted as "YYYY-MM-DD"
    entry_number: An integer indicating the entry in calendar[date] to delete
    calendar: The calendar database
    return: a string indicating any errors, "" for no errors

    Example:

    >>> calendar = {}
    >>> command_add("2017-02-28", "Python class", calendar)
    ''
    >>> calendar == {'2017-02-28': ['Python class']}
    True
    >>> command_add("2017-03-11", "CSCA08 test 2", calendar)
    ''
    >>> calendar == {'2017-03-11': ['CSCA08 test 2'], '2017-02-28':\
    ['Python class']}
    True
    >>> command_add("2017-03-11", "go out with friends after test", calendar)
    ''
    >>> calendar == {'2017-03-11': ['CSCA08 test 2', \
    'go out with friends after test'], '2017-02-28': ['Python class']}
    True
    >>> command_delete("2015-01-01", 1, calendar)
    '2015-01-01 is not a date in the calendar'
    >>> command_delete("2017-03-11", 3, calendar)
    'There is no entry 3 on date 2017-03-11 in the calendar'
    >>> command_delete("2017-02-28", 0, calendar)
    ''
    >>> calendar == {'2017-03-11': ['CSCA08 test 2', \
    'go out with friends after test']}
    True
    >>> command_delete("2017-03-11", 0, calendar)
    ''
    >>> calendar == {'2017-03-11': ['go out with friends after test']}
    True
    >>> command_delete("2017-03-11", 0, calendar)
    ''
    >>> calendar == {}
    True

    '''

    # YOUR CODE GOES HERE
    if date not in calendar:
        return date + ' is not a date in the calendar'
    else:
        if entry_number > len(calendar[date]):
            return 'There is no entry ' + str(entry_number) + ' on date ' + date + ' in the calendar'
        else:
            if len(calendar[date]) < 2:
                del calendar[date]
            else:
                calendar[date].pop(entry_number)
            return ''

# -----------------------------------------------------------------------------
# Functions dealing with calendar persistence
# -----------------------------------------------------------------------------

'''
The calendar is read and written to disk.

...

date_i is "YYYY-MM-DD"'
description can not have tab or new line characters in them.

'''


def save_calendar(calendar):
    '''
    (dict) -> bool
    Save calendar to 'calendar.txt', overwriting it if it already exists.

    The format of calendar.txt is the following:

    date_1:description_1\tdescription_2\t...\tdescription_n\n
    date_2:description_1\tdescription_2\t...\tdescription_n\n
    date_3:description_1\tdescription_2\t...\tdescription_n\n
    date_4:description_1\tdescription_2\t...\tdescription_n\n
    date_5:description_1\tdescription_2\t...\tdescription_n\n

    Example: The following calendar...

        2017-02-28:
            0: Python class
        2017-03-11:
            0: CSCA08 test 2
            1: go out with friends after test

    appears in calendar.txt as ...

    2017-02-28:Python class
    2017-03-11:CSCA08 test 2    go out with friends after test

    calendar: dictionary containing a calendar
    return: True if the calendar was saved.
    Normally we should return False otherwise, however we have not
    learned yet how to handle errors. Therefore there will be no testing
    for cases when the save_calendar operation can fail. Also there is no
    need to provide error handling code. You may if you like, however
    no extra credit will be given, and additionally, you may have to
    explain to the grader/instructor in full how did you do the handling.
    '''
    # YOUR CODE GOES HERE
    outfile = open("calendar.txt", "w")
    for date in calendar:
        outfile.write(date + ":")
        for event in calendar[date]:
            outfile.write(event + "\t")
        outfile.write("\n")
    outfile.close()
    return True


def load_calendar():
    '''
    () -> dict
    Load calendar from 'calendar.txt'. If calendar.txt does not exist,
    create and return an empty calendar. For the format of calendar.txt
    see save_calendar() above. Please observe there are cases when
    the load_calendar operation can fail. There is no
    need to provide error handling code. You may if you like, however
    no extra credit will be given, and additionally, you may have to
    explain to the grader/instructor in full how did you do the handling.
    In case you decide to do error handling, you must return an empty
    calendar in case of various errors.

    return: calendar.

    '''

    # YOUR CODE GOES HERE
    fn = "calendar.txt"
    calendar = dict()
    if os.path.exists(fn):
        fh = open(fn, "r")
        with fh as file:
            for line in file:
                arr = line.split(":")
                calendar[arr[0]] = list()
                events = arr[1].split("\t")
                for event in events:
                    calendar[arr[0]].append(event)
                calendar[arr[0]] = calendar[arr[0]][:-1]
    else:
        open(fn, "w")
    file.close()
    return calendar




# -----------------------------------------------------------------------------
# Functions dealing with parsing commands
# -----------------------------------------------------------------------------


def is_command(command):
    '''
    (str) -> bool
    Return whether command is indeed a command, that is, one of
    "add", "delete", "quit", "help", "show"
    You are not allowed to use regular expressions in your implementation.
    command: string
    return: True if command is one of ["add", "delete", "quit", "help", "show"]
    false otherwise
    Example:
    >>> is_command("add")
    True
    >>> is_command(" add ")
    False
    >>> is_command("List")
    False

    '''

    # YOUR CODE GOES HERE

    return command in ["add", "delete", "quit", "help", "show"]


def is_calendar_date(date):
    '''
    (str) -> bool
    Return whether date looks like a calendar date
    date: a string
    return: True, if date has the form "YYYY-MM-DD" and False otherwise
    You are not allowed to use regular expressions in your implementation.
	Also you are not allowed to use isdigit() or similar functions.

    Example:

    >>> is_calendar_date("15-10-10") # invalid year
    False
    >>> is_calendar_date("2015-10-15")
    True
    >>> is_calendar_date("2015-5-10") # invalid month
    False
    >>> is_calendar_date("2015-15-10") # invalid month
    False
    >>> is_calendar_date("2015-05-10")
    True
    >>> is_calendar_date("2015-10-55") # invalid day
    False
    >>> is_calendar_date("2015-55") # invalid format
    False
    >>> is_calendar_date("jane-is-gg") # YYYY, MM, DD should all be digits
    False

    Note: This does not validate days of the month, or leap year dates.

    >>> is_calendar_date("2015-04-31") # True even though April has only 30 days.
    True

    '''
    # Algorithm: Check length, then pull pieces apart and check them. Use only
    # basic string
    # manipulation, comparisons, and type conversion. Please do not use any
    # powerful date functions
    # you may find in python libraries.
    # 2015-10-12
    # 0123456789

    # YOUR CODE GOES HERE
    if len(date) > 10 or len(date) < 10:
        return False
    try:
        month = int(date.split("-")[1])
        day = int(date.split("-")[2])

        return month < 13 and day < 32

    except ValueError:
        return False

def is_natural_number(str):
    '''
    (str) -> bool
    Return whether str is a string representation of a natural number,
    that is, 0,1,2,3,...,23,24,...1023, 1024, ...
    In CS, 0 is a natural number
    param str: string
    return: True if num is a string consisting of only digits. False otherwise.
    Example:

    >>> is_natural_number("0")
    True
    >>> is_natural_number("05")
    True
    >>> is_natural_number("2015")
    True
    >>> is_natural_number("9 3")
    False
    >>> is_natural_number("sid")
    False
    >>> is_natural_number("2,192,134")
    False

    '''
    # Algorithm:
    # Check that the string has length > 0
    # Check that all characters are in ["0123456789"]

    # YOUR CODE GOES HERE
    numbers = "0123456789"
    if len(str) == 0:
        return False
    for i in str:
        if i not in numbers:
            return False
    return True


def parse_command(line):
    '''
    (str) -> list
    Parse command and arguments from the line. Return a list
    [command, arg1, arg2, ...]
    Return ["error", ERROR_DETAILS] if the command is not valid.
    Return ["help"] otherwise.
    The valid commands are

    1) add DATE DETAILS
    2) show
    3) delete DATE NUMBER
    4) quit
    5) help

    line: a string command
    return: A list consiting of [command, arg1, arg2, ...].
    Return ["error", ERROR_DETAILS], if
    line can not be parsed.

    Example:
    >>> parse_command("add 2015-10-21 budget meeting")
    ['add', '2015-10-21', 'budget meeting']
    >>> parse_command("")
    ['help']
    >>> parse_command("not a command")
    ['help']
    >>> parse_command("help")
    ['help']
    >>> parse_command("add")
    ['error', 'add DATE DETAILS']
    >>> parse_command("add 2015-10-22")
    ['error', 'add DATE DETAILS']
    >>> parse_command("add 2015-10-22 Tims with Sally.")
    ['add', '2015-10-22', 'Tims with Sally.']
    >>> parse_command("add 2015-10-35 Tims with Sally.")
    ['error', 'not a valid calendar date']
    >>> parse_command("show")
    ['show']
    >>> parse_command("show calendar")
    ['error', 'show']
    >>> parse_command("delete")
    ['error', 'delete DATE NUMBER']
    >>> parse_command("delete 15-10-22")
    ['error', 'delete DATE NUMBER']
    >>> parse_command("delete 15-10-22 1")
    ['error', 'not a valid calendar date']
    >>> parse_command("delete 2015-10-22 3,14")
    ['error', 'not a valid event index']
    >>> parse_command("delete 2015-10-22 314")
    ['delete', '2015-10-22', '314']
    >>> parse_command("quit")
    ['quit']

    '''
    # HINT: You can first split, then join back the parts of
    # the final argument.
    # YOUR CODE GOES HERE

    words = line.split();

    if len(words) == 0:
        return ["help"]
    if words[0] == "add":
        details = " ".join(words[2:])
        if len(words) < 3:
            return ["error", "add DATE DETAILS"]
        elif not is_calendar_date(words[1]):
            return ["error", "not a valid calendar date"]
        else:
            return ["add", words[1], details]
    elif words[0] == "show":
        if len(words) != 1:
            return ["error", "show"]
        else:
            return ["show"]
    elif words[0] == "delete":
        if len(words) != 3:
            return ["error", "delete DATE NUMBER"]
        elif not is_calendar_date(words[1]):
            return ["error", "not a valid calendar date"]
        elif not is_natural_number(words[2]):
            return ["error", "not a valid event index"]
        else:
            return ["delete", words[1], words[2]]
    elif words[0] == "quit":
        return ["quit"]
    else:
        return ["help"]

if __name__ == "__main__":
    import doctest
    doctest.testmod()
