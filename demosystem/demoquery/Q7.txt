select count(*) from edge1, edge2, edge3, edge4, edge5 where edge1_to=edge2_from and edge2_to=edge3_from and edge3_to=edge4_from and edge4_to=edge5_from and edge5_to=edge1_from;
