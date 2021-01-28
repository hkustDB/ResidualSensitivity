select max(count) from (select part.P_PARTKEY,count(*) from part group by part.P_PARTKEY) as t;
select max(count) from (select partsupp.PS_SUPPKEY,count(*) from partsupp group by partsupp.PS_SUPPKEY) as t;
select max(count) from (select partsupp.PS_PARTKEY,count(*) from partsupp group by partsupp.PS_PARTKEY) as t;
select max(count) from (select partsupp.PS_SUPPKEY, partsupp.PS_PARTKEY, count(*) from partsupp group by partsupp.PS_SUPPKEY, partsupp.PS_PARTKEY) as t;
select max(count) from (select supplier.S_SUPPKEY,count(*) from supplier group by supplier.S_SUPPKEY) as t;
select max(count) from (select lineitem.L_SUPPKEY, lineitem.L_PARTKEY, count(*) from lineitem group by lineitem.L_SUPPKEY, lineitem.L_PARTKEY) as t;
select max(count) from (select lineitem.L_ORDERKEY,count(*) from lineitem group by lineitem.L_ORDERKEY) as t;
select max(count) from (select orders.O_ORDERKEY,count(*) from orders group by orders.O_ORDERKEY) as t;
