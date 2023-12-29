# 104042731
def mars_roverars(robot: list, limmits: int) -> int: 
    """Рассчитать количество платформ.""" 
    pos_max: int = len(robot) - 1 #Позиция самого большого числа в массиве. 
    pos_min: int = 0 #Позиция самого минимального числа в массиве. 
    robot.sort()  
    count: int = 0 
    while pos_max >= pos_min: 
        if (robot[pos_max] + robot[pos_min]) <= limmits: 
            pos_min += 1 
        pos_max -= 1 
        count += 1         
    return count 
 
def main() -> None: 
    robots: list = [int(array_counter) for array_counter in input().split(' ')] 
    limit = int(input()) 
    print(mars_roverars(robots, limit)) 
 
if __name__ == '__main__': 
    main()
