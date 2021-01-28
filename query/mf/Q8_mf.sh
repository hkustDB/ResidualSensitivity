select max(count) from (select A, B, count(*) from R6 group by A, B) as t;
select max(count) from (select B, C, count(*) from R6 group by B, C) as t;
select max(count) from (select C, A, count(*) from R6 group by C, A) as t;
select max(count) from (select edge3_from, edge3_to, count(*) from edge3 group by edge3_from, edge3_to) as t;
select max(count) from (select edge4_from, edge4_to, count(*) from edge4 group by edge4_from, edge4_to) as t;
select max(count) from (select edge5_from, edge5_to, count(*) from edge5 group by edge5_from, edge5_to) as t;
