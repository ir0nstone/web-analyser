# Context
Contains variables used throughout the entire program, for example `session`, which is the overarching `Session()` object used by all functions.

# Constants
Stores variables in an attempt to make code cleaner.

# Log
Provides functionality for logging output both to the terminal and to a file at the same time.

##### `__log()`
The base function that does the printing and the saving.

##### `info()`
Wrapper function around `__log()` that uses a blue `*` for information.

##### `fail()`
Wrapper function around `__log()` that uses a red `-` when no data is found or a scan is unsuccessful.

##### `success()`
Wrapper function around `__log()` that uses a green `+` when something is found or a scan is successful.

# Utils
Provides helper functions that may be needed multiple times.

##### `grab()`
Simple wrapper function for ease of use that makes a request using `context.session`.

##### `fix_url()`
Converts URLs to an acceptable format. <br>

e.g. `github.com` to `http://www.github.com`

##### `fix_filepath()`
For the savefile.
* If a full path is specified, the full path is used.
* If a relative path is specified, the current location gets appended to the front

##### `cookie_string_to_dict()`
Converts the user's input of a cookie such as `username=bob; password=bobbob` into a dictionary that can be used with requests.

##### `get_full_response()`
Returns a string that contains all the headers as well as the text response.