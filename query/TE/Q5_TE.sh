select max(count) from (select edge1_from, edge1_to, count(*) from edge1 group by edge1_from, edge1_to) as t;
select max(count) from (select edge2_from, edge2_to, count(*) from edge2 group by edge2_from, edge2_to) as t;
select max(count) from (select edge3_from, edge3_to, count(*) from edge3 group by edge3_from, edge3_to) as t;
select max(count) from (select edge1_from, edge2_to, count(*) from edge1, edge2 where edge1_to=edge2_from group by edge1_from, edge2_to) as t;
select max(count) from (select edge3_from, edge1_to, count(*) from edge3, edge1 where edge3_to=edge1_from group by edge3_from, edge1_to) as t;
select max(count) from (select edge2_from, edge3_to, count(*) from edge2, edge3 where edge2_to=edge3_from group by edge2_from, edge3_to) as t;
