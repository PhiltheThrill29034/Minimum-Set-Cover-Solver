import re
from Utils import *
from DiscoZooSolver import DiscoZooSolver
from DiscoZooState import DiscoZooState
from Animals import *
import time



def pick_from_region():
    print("Available Regions:",", ".join(r.capitalize() for r in REGIONS.keys()))
    print("(Type \"menu\" anytime to go back to the main selection menu)")
    
    while True:
        print("Available Regions:",", ".join(r.capitalize() for r in REGIONS.keys()))
        usrChoice = input("Pick a region: ").upper().strip()
        if (usrChoice in REGIONS):
            AnimalEnum = REGIONS[usrChoice]

            print(f"Animals in {usrChoice.capitalize()}:")
            for i,a in enumerate(AnimalEnum,1):
                print(f"{i}. {a}")

            animal_list = list(AnimalEnum)
            while True:
                usrAnimal = input("Pick your animal (name or number), or enter \"0\" or \"menu\" to go back to region selection: ").upper().strip()
                if usrAnimal == "0" or usrAnimal == "MENU":
                    break
                if usrAnimal.isdigit():
                    idx = int(usrAnimal) - 1
                    if 0<=idx<len(animal_list):
                        return animal_list[idx].value
                    else:
                        print("Number out of range! Pick a valid animal.")
                else:
                    try:
                        finalAnimal = AnimalEnum[usrAnimal]
                        return finalAnimal.value
                    except KeyError:
                        print("Animal does not exist! Pick a valid animal.")
        elif usrChoice == "MENU":
            return None
        else:
            print("The region does not exist! Pick a valid region.")
        

    
        
    


def custom_tile_input(min_tiles=2,max_tiles=5):
    print("Enter the tiles of your choice in the format (x,y)")
    print(f"You can enter up to {max_tiles} tiles, and at least {min_tiles} tile(s). Press enter anytime to stop adding tiles.")

    pattern = []
   
    while len(pattern)<max_tiles:
        prompt = f"Enter tile {len(pattern) + 1}"
        if len(pattern)>=min_tiles:
            prompt+=", or press enter to exit"
        tileIn = input(prompt+": ").strip()
        if not tileIn:
            if (len(pattern)<min_tiles):
                exit = input("Would you like to exit and cancel the pattern? Press enter to confirm: ").strip()
                if not exit:
                    return None
                continue
            break
            

        tile = parse_coord(tileIn,5)

        if not tile:
            print(f"Invalid Tile Format!! Use (row, col) between {min_tiles} and {max_tiles}.")
            continue

        zero_indexed_tile = (tile[0]-1, tile[1]-1)

        if (zero_indexed_tile in pattern):           
            print("You have already given this tile!")
            continue

        pattern.append(zero_indexed_tile)
              
            

    return pattern
        

def get_solution(pattern,rows=5,cols=5):

    print(f"Valid Heuristics: {DiscoZooState.VALID_HEURISTICS}")
    heuristic = input("Pick a heuristic: ")
    
    replacements = findPlacements(pattern,rows,cols)

    DiscoZooState.set_grid_dimensions(rows,cols)

    try:
        DiscoZooState.set_heuristic(heuristic)
    except ValueError as e:
        print(e)
        return None
    
    initialState = DiscoZooState(None, replacements, None)

    solution = DiscoZooSolver.astar_solver_debug(initialState)
    

    if solution is not None:
        sol_clicks = DiscoZooSolver.backtrack(solution)

        uncovered = [p for p in replacements if set(sol_clicks).isdisjoint(p)]
    
        print(f"Total placements on 7x7: {len(replacements)}")
        print(f"Solution clicks: {len(sol_clicks)}")
        print(f"Uncovered placements: {len(uncovered)}") #verify that no uncovered placements are left

        return sol_clicks
    else:
        return None
    
def disco_zoo_version():

    header = "     DISCO ZOO MODE (5x5 GRID)    "
            
    print(f"\n{BOLD}"+"═"*len(header)+f"{RESET}")
    print(f"{BOLD}{header}{RESET}")
    print(f"{BOLD}"+"═"*len(header)+f"{RESET}")
    while (True):
        pattern = None
        
        
        print(f" {CYAN}[1]{RESET} Custom Animal Pattern")
        print(f" {CYAN}[2]{RESET} Choose an Animal from a Region")
        print(f" {DIM}[0] Exit{RESET}")
        print(f"{DIM}──────────────────────────────────────{RESET}")

        choice = input(f"{BOLD}Pick an option from the menu: {RESET}")
        
        if (choice=="1"):

            pattern = custom_tile_input()

        elif (choice=="2"):

            pattern = pick_from_region()

        elif (choice=="0"):
            print("\n")
            break

        if pattern is not None:

            solution = get_solution(pattern)
        
            if solution is not None:
                print(f"{GREEN}Optimal click sequence found!{RESET}")
                DiscoZooSolver.print_board(solution)
            else:
                print(f"{RED}No solution found...{RESET}")
        
    
def custom_grid_version():

    header = f"     CUSTOM GRID VERSION     "
    print(f"\n{BOLD}"+"═"*len(header)+f"{RESET}")
    print(f"{BOLD}{header}{RESET}")
    print(f"{BOLD}"+"═"*len(header)+f"{RESET}")
    while(True):
        print(f"{DIM}Press enter, 'q', or type \"exit\" anytime to exit custom grid mode{RESET}")

        rowNum = get_dimension(f"{CYAN}[1]{RESET} Enter number of rows (or Enter to cancel): ")
        
        if rowNum is None:
            print(f"{YELLOW}Exiting custom grid mode...\n {RESET}")
            return
        
        colNum = get_dimension(f"{CYAN}[2]{RESET} Enter number of columns (or Enter to cancel): ")
        if colNum is None:
            print(f"{YELLOW}Exiting custom grid mode...\n {RESET}")
            return
        
        pattern = custom_tile_input(1,rowNum*colNum)

        if pattern is not None:
            print("Code reached here")
            start = time.time_ns()
            solution = get_solution(pattern,rowNum,colNum)
            
            end = time.time_ns()
            print("Checkpoint 2 - Solution computed")
            if solution is not None:
                print(f"{DIM}Solution found in {(end-start)/1000000:.2f} ms{RESET}")
                print(f"{GREEN}Optimal click sequence found!{RESET}")
                DiscoZooSolver.print_board(solution,rowNum,colNum)
            else:
                print(f"{RED}No solution found...{RESET}")




def main_loop():

    header = "     MINIMUM SET COVER PATHFINDING ALGORITHM     "
    print(f"\n{BOLD}"+"═"*len(header)+f"{RESET}")
    print(f"{BOLD}{header}{RESET}")
    print(f"{BOLD}"+"═"*len(header)+f"{RESET}")

    while (True):
        print(f" {CYAN}[1]{RESET} Disco Zoo Mode")
        print(f" {CYAN}[2]{RESET} Custom Grid Size Mode")
        print(f" {DIM}[0] Exit{RESET}")
        print(f"{DIM}──────────────────────────────────────{RESET}")


        
        choice = input(f"{BOLD}Pick an option from the menu: {RESET}")

        if (choice == "1"):
            disco_zoo_version()
        elif choice == "2":
            custom_grid_version()
        elif choice == "0":
            print(f"{GREEN}Thank you for using the program! Bye!{RESET}")
            break
        else:
            print(f"{YELLOW} Please pick a valid choice from the menu.{RESET}")


        
        
main_loop()
















