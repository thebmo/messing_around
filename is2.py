# 1) You are working at a magazine. Write a function that takes in two lists of customers, last month and this month,
# renewals, cancelations, new subscriptions

# https://wiki.python.org/moin/TimeComplexity

# last_month = ['Conor', 'Paul', 'Brian']
# this_month = ['Paul', 'Brian', 'Norbert']
# return renewals, cancellations, new_subs


# takes list arg (this/last month)
def sub_changes(last_month, this_month):
    sub_actions = []
    
    for last_sub in last_month:
        if last_sub in set(this_month):
            sub_actions.append((last_sub, 'renewal'))
        else:
            sub_actions.append((last_sub, 'cancel'))
    
    for this_sub in this_month:
        if this_sub not in set(last_month):
            sub_actions.append((this_sub, 'new subscriber'))

    return sub_actions

    
# takes list arg (this/last month)
def sub_dict(last_month, this_month):
    sub_actions = {}
    for sub in last_month:
        sub_actions[sub] = 'canceled'
    
    for sub in this_month:
        if sub in sub_actions:
            sub_actions[sub] = 'renewal'
        else:
            sub_actions[sub] = 'new subscriber'
            

    return sub_actions
    
def main():
    last_month = ['Conor', 'Paul', 'Brian']
    this_month = ['Paul', 'Brian', 'Norbert']
    
    changes = sub_changes(last_month, this_month)
    
    print 'last month:\n', last_month
    print 'this month:\n', this_month
    print 'changes:\n', changes
    print type(changes)
    sett = set(changes)
    print type(sett)
    
    changes = sub_dict(last_month, this_month)
    print changes
# boiler code    
if __name__ == '__main__':
    main()