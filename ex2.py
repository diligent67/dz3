def ticket_total(count, price=12):
    return count*price
def final_price(count, is_school_group=False):
    if is_school_group == True:
        return ticket_total(count) - ticket_total(count)*0.25
    else:
        return ticket_total(count)
print(final_price(count=3))
print(final_price(4, is_school_group=True))
print(ticket_total(2,price=15))
