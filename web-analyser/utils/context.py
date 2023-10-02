url = ""
file = None                 # Output File

session = None              # Overarching Session() object
default_req = None          # Standard GET request to /

hide_fail = False           # hide 'fail' messages
verbose = False             # how much should be printed


# Some helper function to clean up code in other files
def default_txt():
    return default_req.text


def default_len():
    return len(default_txt())
