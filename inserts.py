def insert_sample_data(db):
    create_orders(db)
    create_line_items(db)
    create_suppliers(db)
    create_parts(db)
    create_relationships(db)
    create_indexes(db)


def create_orders(db):
    result = db.run("CREATE (o1:Order {o_orderkey:1, o_orderdate:'2016-11-30', o_shippriority:0, "
                    "c_mktsegment:'Computers', n_name:'ESP', r_name:'BCN'}) RETURN o1")
    result = db.run("CREATE (o2:Order {o_orderkey:2, o_orderdate:'2016-12-01', o_shippriority:1, "
                    "c_mktsegment:'Computers', n_name:'ESP', r_name:'BCN'}) RETURN o2")
    result = db.run("CREATE (o3:Order {o_orderkey:3, o_orderdate:'2016-12-05', "
                    "c_mktsegment:'Chemistry', n_name:'BER', r_name:'GER'}) RETURN o3")


def create_line_items(db):
    db.run("CREATE (li11:LineItem {l_returnflag:'F', l_linestatus:'R', l_extendedprice:5.50, l_discount:0.50, "
           "l_quantity:1, l_tax:1.20, l_shipdate:'2016-12-01', n_name:'ESP', r_name:'BCN'})")
    db.run("CREATE (li21:LineItem {l_returnflag:'F', l_linestatus:'R', l_extendedprice:2.00, l_discount:0.00, "
           "l_quantity:3, l_tax:1.20, l_shipdate:'2016-12-01', n_name:'ESP', r_name:'BCN'})")
    db.run("CREATE (li12:LineItem {l_returnflag:'F', l_linestatus:'S', l_extendedprice:15, l_discount:0.3, "
           "l_quantity:1, l_tax:1.20, l_shipdate:'2016-12-02', n_name:'ESP', r_name:'BCN'})")


def create_suppliers(db):
    db.run("CREATE (sup1:Supplier {s_name:'Light Lights', s_address:'Light Stree 123', s_phone:'+34 000 00 00 00', "
           "s_comment:'This is a comment', s_acctbal:0.0, r_name:'BCN', n_name:'ESP'})")
    db.run("CREATE (sup2:Supplier {s_name:'Golden Gold', s_acctbal:1000.00, r_name:'BCN', n_name:'ESP'})")


def create_parts(db):
    db.run("CREATE (p1:Part {p_partkey:1, p_size:1, p_type:'Basic', p_mfgr:'WTF?'})")
    db.run("CREATE (p2:Part {p_partkey:2, p_size:4, p_type:'Luxury', p_mfgr:'WTF?'})")


def create_relationships(db):
    db.run("MATCH (o1:Order {o_orderkey: 1}), (li11:LineItem {l_discount: 0.50}), (li21:LineItem {l_discount: 0.00})"
           " CREATE (o1)-[:IS_FORMED_BY]->(li11), (o1)-[:IS_FORMED_BY]->(li21)")
    db.run("MATCH (o2:Order {o_orderkey: 2}), (li12:LineItem {l_discount: 0.3}) "
           "CREATE (o2)-[:IS_FORMED_BY]->(li12)")

    db.run("MATCH (sup1:Supplier {s_name:'Light Lights'}), (p1:Part {p_partkey: 1}) "
           "CREATE (sup1)-[:SUPPLIES {ps_supplycost:1.99}]->(p1)")
    db.run("MATCH (sup2:Supplier {s_name:'Golden Gold'}), (p1:Part {p_partkey: 1}), (p2: Part {p_partkey: 2}) "
           "CREATE (sup2)-[:SUPPLIES {ps_supplycost:1.98}]->(p1), (sup2)-[:SUPPLIES {ps_supplycost:9.99}]->(p2)")


def create_indexes(db):
    db.run("CREATE index on :Order {o_orderdate}")
    db.run("CREATE index on: Order {c_mktsegment}")
    db.run("CREATE index on: LineItem {l_shipdate}")
