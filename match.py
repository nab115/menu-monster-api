def get_matching_items(restaurants, target):
    results = []

    for r in restaurants:
        matching_items = []

        for item in r['items']:
            if(_is_match(target.lower(), item['name'].lower()) != -1):
                matching_items.append(item)
        
        r['items'] = matching_items
        if matching_items:
            results.append(r)
        
    return results


def _is_match(target, item_name):
    match_ = item_name.find(target)
    print(target + ' ' + item_name + ' ' + str(match_))
    return match_