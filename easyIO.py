import sys

# *** USER I/O ***

def get_user_input(**kwargs):
    """Get user input, of specific type if required"""

    # Unpack arguments
    message=kwargs.get("message","")
    dtype=kwargs.get("dtype","str")

    # Get input, repeat message if incorrect data type
    if dtype=="int": # integer data type
        while True:
            try:
                user_input=int(raw_input(message))
                break
            except:
                pass
    elif dtype=="float": # float data type
        while True:
            try:
                user_input=float(raw_input(message))
                break
            except:
                pass
    elif dtype=="string": # string data type
        while True:
            try:
                user_input=str(raw_input(message))
                break
            except:
                pass
    elif dtype=="bool": # boolean data type
        while True:
            true_values=["true","t","yes","y"]
            false_values=["false","f","no","n"]
            all_values=true_values+false_values
            try:
                user_input=raw_input(message).lower()
                if user_input in all_values:
                    if user_input in true_values:
                        user_input=True
                    else:
                        user_input=False
                    break
            except:
                pass
    else:
        user_input=None

    return user_input

def get_user_menu_selection(title,menu):
    """Display menu options as enumerated list, return index of user selected option"""

    print title
    for i, option in enumerate(menu):
        print "{:})  {:}".format(i+1,option)
    user_selection=get_user_input(dtype="int")-1

    return user_selection


if __name__=="__main__":
    menu=["a","b","c"]
    print get_user_menu_selection("Select option",menu)
