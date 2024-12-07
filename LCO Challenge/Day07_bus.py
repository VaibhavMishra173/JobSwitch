# city bus carry 1,200,000 people each day. how many people bus carry 
# in one year (365 days) without using *,/,operator,bitwise,loop

def cnt(one_day,one_year):
    if(one_year==0):
        return 0
    if(one_year>0):
        return(one_day+cnt(one_day,one_year-1))
    if(one_year<0):
        return -cnt(one_day,-one_year)



one_day = 1200000
one_year = 365

print(cnt(one_day,one_year))