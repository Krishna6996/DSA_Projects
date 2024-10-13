'''
    This file contains the class definition for the StrawHat class.
'''
from crewmate import CrewMate
from heap import Heap
from treasure import Treasure
def comparator_1(a,b):
    if(b.arrival_time + b.size > a.arrival_time + a.size):
        return True
    elif(b.arrival_time + b.size < a.arrival_time + a.size):
        return False
    else:
        return a.id < b.id

class StrawHatTreasury:
    '''qwe nm
    Class to implement the StrawHat Crew Treasury
    '''
    
    def __init__(self, m):
        '''
        Arguments:
            m : int : Number of Crew Mates (positive integer)
        Returns:
            None
        Description:
            Initializes the StrawHat
        Time Complexity:
            O(m)
        '''

        self.crewmates_by_load = []
        for i in range(0,m):
           
            crew = CrewMate()
            self.crewmates_by_load.append(crew)
        self.crewmates_by_load_heap = Heap(lambda a, b: a.load < b.load,self.crewmates_by_load)
        self.working_crewmates = []
        self.current_time = 0  
        
    
    def add_treasure(self, treasure):
        '''
        Arguments:
            treasure : Treasure : The treasure to be added to the treasury
        Returns:
            None
        Description:
            Adds the treasure to the treasury
        Time Complexity:
            O(log(m) + log(n)) where
                m : Number of Crew Mates
                n : Number of Treasures
        '''
        tre = treasure
        person = self.crewmates_by_load_heap.extract()
        
        person.load = max(person.load,tre.arrival_time) + tre.size
        self.crewmates_by_load_heap.insert(person)
        if person.working != True :
            self.working_crewmates.append(person)
            person.working = True
        person.treasures.append(tre)
        self.current_time = tre.arrival_time


    

       
    
    def get_completion_time(self):
        arr_zero_completion_time = []

        # Process each crewmate's list of treasures
        for crewmember in self.working_crewmates:
            temp_arr = []
            temp_heap = Heap(comparator_1, temp_arr)
            #print(f"\nProcessing crewmember with treasures: {crewmember.treasures}")

            # Insert treasures into the heap
            for trap in crewmember.treasures:
                t = trap.arrival_time
                s = trap.size
                i = trap.id
                temp_treasure = Treasure(i, s, t)
                temp_treasure.completion_time=t
                #print(f"Inserting treasure {temp_treasure.id} with size {s} and arrival time {t}")

                if temp_heap.size() == 0:
                    temp_heap.insert(temp_treasure)
                    #print(f"Heap was empty, inserted treasure {temp_treasure.id}")
                else:
                    #print(f"Top of the heap before processing: {temp_heap.top()}")

                    if (temp_heap.top().size - (temp_treasure.completion_time - temp_heap.top().completion_time) <= 0):
                        #print(f"Top treasure size depleted, processing...")
                        while temp_heap.top().size - (temp_treasure.completion_time - temp_heap.top().completion_time) <= 0 and temp_heap.size() != 0:
                            temp_heap.top().completion_time = temp_heap.top().size + temp_heap.top().completion_time
                            new = temp_heap.top().completion_time
                            #print(f"Treasure {temp_heap.top().id} completed at time {new}")
                            temp_treasure_2 = temp_heap.extract()
                            arr_zero_completion_time.append(temp_treasure_2)
                            if temp_heap.size() == 0:
                                break

                            if temp_heap.size() > 0:
                                temp_heap.top().completion_time = new
                                #print(f"Adjusted top treasure arrival time to {new}")


                        if temp_heap.size() != 0:
                            if temp_treasure.size + temp_treasure.arrival_time > temp_heap.top().arrival_time + temp_heap.top().size:
                                temp_heap.insert(temp_treasure)
                                #print(f"Inserted treasure {temp_treasure.id} after adjusting top of the heap")
                            else:
                                temp2 = temp_heap.extract()
                                temp2.size -= (temp_treasure.completion_time - temp2.completion_time)
                                temp2.completion = temp_treasure.completion_time
                                temp_heap.insert(temp_treasure)
                                temp_heap.insert(temp2)
                                #print(f"Inserted treasures {temp_treasure.id} and {temp2.id} after swapping")
                        else:
                            temp_heap.insert(temp_treasure)
                            #print(f"Heap was empty again, inserted treasure {temp_treasure.id}")
                    else:
                        if temp_treasure.size + temp_treasure.completion_time < temp_heap.top().completion_time + temp_heap.top().size:
                            temp_heap.top().size -= (temp_treasure.completion_time - temp_heap.top().completion_time)
                            temp_heap.top().completion_time = temp_treasure.completion_time
                            #print(f"Inserted treasure {temp_treasure.id} after reducing top treasure's size to {temp_heap.top().size} and {temp_heap.top().arrival_time}")
                            temp_heap.insert(temp_treasure)
                        else:
                            temp2 = temp_heap.extract()
                            temp2.size -= (temp_treasure.completion_time - temp2.completion_time)
                            temp2.completion_time = temp_treasure.completion_time
                            temp_heap.insert(temp_treasure)
                            temp_heap.insert(temp2)
                            #print(f"Inserted treasures {temp_treasure.id} and {temp2.id} after adjusting")

                # Processing remaining treasures in the heap
            load = 0
            if temp_heap.size() > 0:
                temp_heap.top().completion_time = temp_heap.top().size + temp_heap.top().completion_time
                #print(f"Top treasure {temp_heap.top().id} completion time set to {temp_heap.top().completion_time}")

            while temp_heap.size() != 0:
                    load = temp_heap.top().completion_time
                    arr_zero_completion_time.append(temp_heap.extract())
                    #print(f"Extracted and completed treasure, new load time: {load}")
                    if temp_heap.size() != 0:
                        temp_heap.top().completion_time = load + temp_heap.top().size
                        #print(f"Set new top treasure {temp_heap.top().id} completion time to {temp_heap.top().completion_time}")

        # Sort treasures by ID and return the completion times
        arr_zero_completion_time.sort(key=lambda x: x.id)
        #print(f"\nFinal sorted treasures based on ID:")
        #for treasure in arr_zero_completion_time:#
            #print(f"Treasure {treasure.id}: Completion Time {treasure.completion_time}")
            
        return arr_zero_completion_time

        
                


                
                
