def check_todo(text):
    """
    Takes text as an input in type str and checks if
    #TODO is in the input
    
    Parameters: 
        text - str of various length
        
    Returns:
        Bools - True or False. True if #TODO in text
        and false if it's not
        
    Side effects: 
        Doesn't print anything and no other side effects
    """

    return '#TODO' in str(text)
