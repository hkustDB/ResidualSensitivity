create table t44 as select edge1_to, count(*) from edge1 group by edge1_to;
create table t11 as select edge2_to, count(*) from edge1, edge2 where edge1_to=edge2_from group by edge2_to;
create table t22 as select edge3_to, sum(count) as count from t11, edge3 where edge2_to=edge3_from group by edge3_to;
create table t33 as select edge4_to, sum(count) as count from t22, edge4 where edge3_to=edge4_from group by edge4_to;
Select sum(count) from  t33, edge5 where edge4_to=edge5_from;
drop table t44;
drop table t11;
drop table t22;
drop table t33;
