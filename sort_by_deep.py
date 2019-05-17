levels_dict = {}


def sort_by_deep_parenthesis_level(s, deep=0):
    # type: (str,int) -> None
    """
    This function get a string and print sorted string by deep parenthesis level.
    :param s: string to sort
    :param deep: which lever are we in this call
    :return:
    """
    if deep not in levels_dict.keys():
        levels_dict[deep] = ""
    while s and not s.startswith(("(", ")")):
        levels_dict[deep] += s[0]
        s = s[1:]
    if s.startswith("("):
        sort_by_deep_parenthesis_level(s[1:], deep + 1)
    if s.startswith(")"):
        sort_by_deep_parenthesis_level(s[1:], deep - 1)
    if not s:
        print ("".join(levels_dict.values()))
