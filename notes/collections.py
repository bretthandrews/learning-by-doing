class Collections():
    pass

c = Collections()
for i, row in enumerate(data):
    if i % 2 == 0:
        c.set_year()
        c.year = f(row)
    else:
        for i in range(10):
            c.add()

c.to_pandas()
c.to_sql()
