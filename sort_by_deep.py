levels_dict = {}


def sort_by_parenthesis_level(s, level=0):
    # type: (str,int) -> None
    """
    This function get a string and print sorted string by level parenthesis level.
    :param s: string to sort
    :param level: which lever are we in this call
    :return:
    """
    if level not in levels_dict.keys():
        levels_dict[level] = ""
    while s and not s.startswith(("(", ")")):
        levels_dict[level] += s[0]
        s = s[1:]
    if s.startswith("("):
        sort_by_parenthesis_level(s[1:], level + 1)
    if s.startswith(")"):
        sort_by_parenthesis_level(s[1:], level - 1)
    if not s:
        print ("".join(levels_dict.values()))
