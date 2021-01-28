select max(count) from (select edge1_to, count(*) from edge1 group by edge1_to) as t;
select max(count) from (select edge2_from, count(*) from edge2 group by edge2_from) as t;
select max(count) from (select edge2_to, count(*) from edge2 group by edge2_to) as t;
select max(count) from (select edge3_from, count(*) from edge3 group by edge3_from) as t;
select max(count) from (select edge3_to, count(*) from edge3 group by edge3_to) as t;
select max(count) from (select edge4_from, count(*) from edge4 group by edge4_from) as t;
select max(count) from (select edge4_to, count(*) from edge4 group by edge4_to) as t;
select max(count) from (select edge5_from, count(*) from edge5 group by edge5_from) as t;
