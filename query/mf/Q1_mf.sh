select max(count) from (select nation.N_NATIONKEY,count(*) from nation group by nation.N_NATIONKEY) as t;
select max(count) from (select customer.C_NATIONKEY,count(*) from customer group by customer.C_NATIONKEY) as t;
select max(count) from (select customer.C_CUSTKEY,count(*) from customer group by customer.C_CUSTKEY) as t;
select max(count) from (select orders.O_CUSTKEY,count(*) from orders group by orders.O_CUSTKEY) as t;
select max(count) from (select orders.O_ORDERKEY,count(*) from orders group by orders.O_ORDERKEY) as t;
select max(count) from (select lineitem.L_ORDERKEY,count(*) from lineitem group by lineitem.L_ORDERKEY) as t;
select max(count) from (select lineitem.L_suppkey,count(*) from lineitem group by lineitem.L_suppkey) as t;
select max(count) from (select supplier.S_SUPPKEY,count(*) from supplier group by supplier.S_SUPPKEY) as t;
