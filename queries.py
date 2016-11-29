
def execute_query_1(db, date):
    result = db.run("MATCH (n:LineItem) "
                    "WHERE n.l_shipdate <= {date}"
                    "WITH n.l_returnflag as returnflag, n.l_linestatus as linestatus, sum(n.l_quantity) as sum_qty,"
                    "sum(n.l_extendedprice) as sum_base_price, sum(n.l_extendedprice*(1-n.l_discount)) as sum_disc_price, "
                    "sum(n.l_extendedprice*(1-n.l_discount)*(1+n.l_tax)) as sum_charge, avg(n.l_quantity) as avg_qty, "
                    "avg(n.l_extendedprice) as avg_price, avg(n.l_discount) as avg_disc, count(*) as count_order "
                    "RETURN returnflag, linestatus, sum_qty, sum_base_price, sum_disc_price, sum_charge, avg_qty, avg_price, avg_disc,  count_order "
                    "ORDER BY returnflag, linestatus", {"date": date})

    for record in result:
        print(record)

def execute_query_2(db, size, types, region):
    pass


def execute_query_3(db, segment, date1, date2):
    pass


def execute_query_4(db, name, date):
    pass
