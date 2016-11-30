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
    print()


def execute_query_2(db, size, type, region):
    result = db.run(
        "MATCH (s:Supplier)-[S:SUPPLIES]->() where s.r_name = {region} return min(S.ps_supplycost) as min_supplycost",
        {"region": region})
    for record in result:
        min_supplycost = float(record["min_supplycost"])

    result = db.run("MATCH (p:Part)<-[S:SUPPLIES]-(s:Supplier) "
                    "WHERE p.p_size = {size} and p.p_type STARTS WITH {type} "
                    "and s.r_name = {region} and S.ps_supplycost = {min_supplycost}"
                    "RETURN s.s_acctbal, s.s_name, s.n_name, p.p_partkey, "
                    "p.p_mfgr, s.s_address, s.s_phone, s.s_comment "
                    "ORDER BY s.s_acctbal DESC, s.n_name, s.s_name, p.p_partkey",
                    {"size": size, "type": type, "region": region, "min_supplycost": min_supplycost})
    for record in result:
        print(record)
    print()


def execute_query_3(db, segment, date1, date2):
    result = db.run("MATCH (n:LineItem)<-[]-(o:Order)"
                    "WHERE o.c_mktsegment = {segment} and o.o_orderdate < {date1} and n.l_shipdate > {date2} "
                    "WITH o.o_orderkey as l_orderkey, sum(n.l_extendedprice*(1-n.l_discount)) as revenue,"
                    "o.o_orderdate as o_orderdate, o.o_shippriority as o_shippriority "
                    "RETURN l_orderkey, revenue, o_orderdate, o_shippriority"
                    "ORDER BY revenue DESC, o_orderdate",
                    {"segment": segment, "date1": date1, "date2": date2})

    for record in result:
        print(record)
    print()


def execute_query_4(db, name, date):
    date2 = date
    date2.replace(year = date2.year + 1)
    result = db.run("MATCH (n:LineItem)<-[]-(o:Order)"
                    "WHERE  n.r_name = {name} and n.n_name = o.n_name and o.o_orderdate >= {date}"
                    "and o.o_orderdate < {date2}"
                    "WITH sum(n.l_extendedprice*(1-n.l_discount)) as revenue"
                    "RETURN n.n_name, revenue"
                    "ORDER BY revenue DESC",
                    {"name": name, "date": date, "date2": date2})

    for record in result:
        print(record)
    print()
