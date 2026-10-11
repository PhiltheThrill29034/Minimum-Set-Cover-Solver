## this is it
import heapq
from Utils import findPlacements
from DiscoZooState import DiscoZooState

class DiscoZooSolver:

    @staticmethod
    def astar_solver(initialState):

        frontier = []

        closedSet = set()

        initialState.h()
        
        heapq.heappush(frontier,initialState)

        

        while len(frontier) > 0: # same as while len(frontier) > 0
            
            
            current = heapq.heappop(frontier)
            

            if (current.isFinal()):
                return current

            if current in closedSet:
                continue

            closedSet.add(current)
            
            for child in current.get_children():

                
                if child in closedSet:
                    continue

               

                heapq.heappush(frontier,child)

        return None

    @staticmethod
    def astar_solver_debug(initialState):
    
        frontier = []
    
        closedSet = set()
    
        initialState.h()
            
        heapq.heappush(frontier,initialState)
    
        iter = 0
    
        while len(frontier) > 0: # same as while len(frontier) > 0
            iter +=1
                
            current = heapq.heappop(frontier)
            if iter % 10000 == 0:
                    print(f"[A*]: {iter} states explored\n" 
                          f"Frontier size: {len(frontier)}\n"
                          f"Depth: {current.g_cost}\n"
                          f"F-score: {current.f}\n"
                          f"Remaining placements: {len(current.remaining_placements)}")
    
            if (current.isFinal()):
                    return current
    
            if current in closedSet:
                    continue
    
            closedSet.add(current)
                
            for child in current.get_children():
    
                    
                if child in closedSet:
                    continue
    
                   
    
                heapq.heappush(frontier,child)
    
        return None

    @staticmethod
    def backtrack(final_state):

        temp = final_state
        
        raw_clicks = []
        while temp.parent is not None:
            
            raw_clicks.append(temp.last_click)
            temp=temp.parent

        
        raw_clicks.reverse()
        return raw_clicks
        
        # for i,click in enumerate(raw_clicks,1):
        #     print(f"Click {i}: {click}")
           

    @staticmethod
    def backtrack_UI(final_state):
    
        temp = final_state
            
        raw_clicks = []
        while temp.parent is not None:
                
            raw_clicks.append(temp.last_click)
            temp=temp.parent
    
        raw_clicks.reverse()  
        
        
        for i,click in enumerate(raw_clicks,1):
            print(f"Click {i}: {click[0]+1},{click[1]+1}")
            i+=1
    
    @staticmethod
    def print_board(clicks,rows=5,cols=5):

        

        max_row_len = len(f"Row {rows} ")

        header_pad = " "*(max_row_len+1)

        max_cell_len = max(len(f" Col {cols} "), len(f"[{len(clicks)}]"))

        col_headers = "".join(f" Col {c+1} ".center(max_cell_len) + " " for c in range(cols))
        print(header_pad + col_headers)

        seperator = " "*max_row_len+"├"+("─"*max_cell_len+"┼")*(cols -1) + ("─"*max_cell_len+"┤")

        click_nums = {coord:step for step,coord in enumerate(clicks,1)}

        top_line = " "*max_row_len+"┌"+("─"*max_cell_len+"┬")*(cols -1) + ("─"*max_cell_len+"┐")
        bottom_line = " "*max_row_len+"└"+("─"*max_cell_len+"┴")*(cols -1) + ("─"*max_cell_len+"┘")
        print(top_line)

        for r in range(rows):

            row_label = f"Row {r+1} ".ljust(max_row_len)
            row_cells=[]

            for c in range(cols):
                
                outp = f"[{click_nums[(r,c)]}]" if (r,c) in clicks else "."
                row_cells.append(outp.center(max_cell_len))
                
            print(row_label+"│"+"│".join(row_cells)+"│")
            print(seperator) if r < rows - 1 else print(bottom_line)










