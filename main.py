def replace_last(list_):
    if len(list_) == 0:
        return list_
    else:
        list_.insert(0, list_.pop())
        return list_
