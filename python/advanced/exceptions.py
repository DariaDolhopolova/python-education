"""An example of exception-catching"""
# actor = {"name": "John Cleese", "rank": "awesome"}
actor = {"name": "John", "rank": "awesome"}


def get_last_name():
    """The function returns last names and
    catches exceptions."""
    try:
        return actor["name"].split()[1]
    except IndexError:
        return "There's no last name"


get_last_name()
print("All exceptions caught! Good job!")
print("The actor's last name is %s" % get_last_name())
