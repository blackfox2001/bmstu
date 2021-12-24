def field(items, *args):
    assert len(args) > 0
    result = []
    for item in items:
        if len(args) == 1:
            if args[0] in item.keys():
                result.append(item[args[0]])
        else:
            res = dict()
            for key in args:
                if key in item.keys():
                    res[key] = item[key]
            result.append(res)
    return result