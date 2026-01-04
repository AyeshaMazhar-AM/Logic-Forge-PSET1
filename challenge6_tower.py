def towerOfHanoi(n, from_rod, to_rod, aux_rod):
    if n == 1:
        print(f"Disk 1 moved from {from_rod} to {to_rod}")
        return
 
    towerOfHanoi(n-1, from_rod, aux_rod, to_rod)
    print(f"Disk {n} moved from {from_rod} to {to_rod}")
    towerOfHanoi(n-1, aux_rod, to_rod, from_rod)

towerOfHanoi(3, 'A', 'C', 'B')