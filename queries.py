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
                    "WHERE p.p_size = 1 and p.p_type STARTS WITH 'Ba' and s.r_name = 'BCN' and S.ps_supplycost = 1.98 "
                    "RETURN s.s_acctbal, s.s_name, s.r_name, p.p_partkey, p.p_mfgr, s.s_address, s.s_phone, s.s_comment",
                    {"size": size, "type": type, "region": region})
    for record in result:
        print(record)
    print()


def execute_query_3(db, segment, date1, date2):
    pass


def execute_query_4(db, name, date):
    pass
