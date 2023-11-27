def oxford_comma(items):
    if len(items)==1:
        stringify="".join(items)
        return stringify
    elif len(items)==2:
        stringify=" and ".join(items)
        return stringify
    else:
        stringify=", ".join(items[:-1]) + ", and " + items[-1]
        return stringify
    
