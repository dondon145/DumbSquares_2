import random

class Grid():

    def position_is_appropriate(self, obj):
        pos_x, pos_y = obj.get_pos()

        if pos_x % self.cell_width == 0 and pos_y % self.cell_height == 0:
            return True
        else:
            return False
        
    def fix_to_correct_position(self, obj):
        pos_x, pos_y = obj.get_pos()

        remainder_x = pos_x % self.cell_width
        remainder_y = pos_y % self.cell_height

        if remainder_x < 5:
            pos_x -= remainder_x
        else:
            pos_x = pos_x - remainder_x + self.cell_width
    
        if remainder_y < 5:
            pos_y -= remainder_y
        else :
            pos_y = pos_y - remainder_y + self.cell_height

        return pos_x, pos_y

    def move_all_objects(self):
        for i in range(len(self.objects_on_screen)-1):
            if self.objects_on_screen[i].get_material() == "sand":
                self.sand_go_down(self.objects_on_screen[i])
            elif self.objects_on_screen[i].get_material() ==  "water":
                self.water_go_down(self.objects_on_screen[i])
            elif self.objects_on_screen[i].get_material() == "static stone":
                self.place_static_stone(self.objects_on_screen[i])

    def add_on_screen(self, obj):
        self.objects_on_screen.append(obj)
        self.group.add(obj)
    
    def next_cell_is_empty(self, current_pos_x, current_pos_y, displacement_x, displacement_y):
        new_pos_x = current_pos_x + displacement_x
        new_pos_y = current_pos_y + displacement_y
        if new_pos_x < self.grid_width and new_pos_y < self.grid_height:
            if new_pos_x >= 0 and new_pos_y >= 0:
                if self.grid[new_pos_x, new_pos_y] == 'empty':
                    return True
        else : 
            return False

    def sand_go_down(self, obj):

        pos_x, pos_y = obj.get_pos()
        if self.position_is_appropriate(obj) == False:
            pos_x, pos_y = self.fix_to_correct_position(obj)
            obj.set_pos(pos_x, pos_y)

        if self.next_cell_is_empty(pos_x, pos_y, 0, self.cell_height):
            self.grid[pos_x, pos_y] = "empty"
            obj.change_pos_by(0, self.cell_height)
            new_pos_x, new_pos_y = obj.get_pos()
            self.grid[new_pos_x, new_pos_y] = obj
            
            # This makes sand stay under water, but it is bugged and sand stops acting as sand and instead makes tall sticks
            """elif pos_y + self.cell_height < self.grid_height:
                if self.grid[pos_x, pos_y + self.cell_height].get_material() == "water":
                    print("should work")
                    self.grid[pos_x, pos_y] , self.grid[pos_x, pos_y + self.cell_height] = self.grid[pos_x, pos_y + self.cell_height], self.grid[pos_x, pos_y]
                    obj.set_pos(pos_x, pos_y + self.cell_height)
                    self.grid[pos_x, pos_y].set_pos(pos_x, pos_y)
                    obj.update_rect()
                    self.grid[pos_x, pos_y].update_rect()"""
        else :
            num = random.randrange(0, 2)
            if num == 0:
                self.sand_go_down_right(obj)
            elif num == 1:
                self.sand_go_down_left(obj)


    # This should make sand stay under water, but it is bugged
    def sand_go_down_right(self, obj):
        pos_x, pos_y = obj.get_pos()

        if self.next_cell_is_empty(pos_x, pos_y, self.cell_width, self.cell_height):
            self.grid[pos_x, pos_y] = "empty"
            obj.change_pos_by(self.cell_width, self.cell_height)
            new_pos_x, new_pos_y = obj.get_pos()
            self.grid[new_pos_x, new_pos_y] = obj
        elif pos_y + self.cell_height < self.grid_height and pos_x + self.cell_width < self.grid_width:
                if self.grid[pos_x + self.cell_width, pos_y + self.cell_height].get_material() == "water":
                    self.grid[pos_x, pos_y] , self.grid[pos_x + self.cell_width, pos_y + self.cell_height] = self.grid[pos_x + self.cell_width, pos_y + self.cell_height], self.grid[pos_x, pos_y]
                    obj.set_pos(pos_x + self.cell_width, pos_y + self.cell_height)
                    self.grid[pos_x, pos_y].set_pos(pos_x, pos_y)
                    obj.update_rect()
                    self.grid[pos_x, pos_y].update_rect()
        else:
            pass

    # This should make sand stay under water, but it is bugged
    def sand_go_down_left(self, obj):
        pos_x, pos_y = obj.get_pos()

        if self.next_cell_is_empty(pos_x, pos_y, -self.cell_width, self.cell_height):
            self.grid[pos_x, pos_y] = "empty"
            obj.change_pos_by(-self.cell_width, self.cell_height)
            new_pos_x, new_pos_y = obj.get_pos()
            self.grid[new_pos_x, new_pos_y] = obj
        elif pos_y + self.cell_height < self.grid_height and pos_x - self.cell_width > 0:
                if self.grid[pos_x - self.cell_width, pos_y + self.cell_height].get_material() == "water":
                    self.grid[pos_x, pos_y] , self.grid[pos_x - self.cell_width, pos_y + self.cell_height] = self.grid[pos_x - self.cell_width, pos_y + self.cell_height], self.grid[pos_x, pos_y]
                    obj.set_pos(pos_x - self.cell_width, pos_y + self.cell_height)
                    self.grid[pos_x, pos_y].set_pos(pos_x, pos_y)
                    obj.update_rect()
                    self.grid[pos_x, pos_y].update_rect()
        else:
            pass


    def water_go_down(self, obj):

        pos_x, pos_y = obj.get_pos()
        if self.position_is_appropriate(obj) == False:
            pos_x, pos_y = self.fix_to_correct_position(obj)
            obj.set_pos(pos_x, pos_y)

        if self.next_cell_is_empty(pos_x, pos_y, 0, self.cell_height):
            self.grid[pos_x, pos_y] = "empty"
            obj.change_pos_by(0, self.cell_height)
            new_pos_x, new_pos_y = obj.get_pos()
            self.grid[new_pos_x, new_pos_y] = obj
        else:
            num = random.randrange(0, 2)
            if num == 0:
                if self.next_cell_is_empty(pos_x, pos_y, self.cell_width, self.cell_height):
                    self.go_down_right(obj)
                else: 
                    self.go_right(obj)
            elif num == 1:
                if self.next_cell_is_empty(pos_x, pos_y, -self.cell_width, self.cell_height):
                    self.go_down_left(obj)
                else:
                    self.go_left(obj)
    
    def go_right(self, obj):
        pos_x, pos_y = obj.get_pos()

        if self.next_cell_is_empty(pos_x, pos_y, self.cell_width, 0):
            self.grid[pos_x, pos_y] = "empty"
            obj.change_pos_by(self.cell_width, 0)
            new_pos_x, new_pos_y = obj.get_pos()
            self.grid[new_pos_x, new_pos_y] = obj

    def go_left(self, obj):
        pos_x, pos_y = obj.get_pos()

        if self.next_cell_is_empty(pos_x, pos_y, -self.cell_width, 0):
            self.grid[pos_x, pos_y] = "empty"
            obj.change_pos_by(-self.cell_width, 0)
            new_pos_x, new_pos_y = obj.get_pos()
            self.grid[new_pos_x, new_pos_y] = obj

    def go_down_right(self, obj):
        pos_x, pos_y = obj.get_pos()

        if self.next_cell_is_empty(pos_x, pos_y, self.cell_width, self.cell_height):
            self.grid[pos_x, pos_y] = "empty"
            obj.change_pos_by(self.cell_width, self.cell_height)
            new_pos_x, new_pos_y = obj.get_pos()
            self.grid[new_pos_x, new_pos_y] = obj
        else:
            pass

    def go_down_left(self, obj):
        pos_x, pos_y = obj.get_pos()

        if self.next_cell_is_empty(pos_x, pos_y, -self.cell_width, self.cell_height):
            self.grid[pos_x, pos_y] = "empty"
            obj.change_pos_by(-self.cell_width, self.cell_height)
            new_pos_x, new_pos_y = obj.get_pos()
            self.grid[new_pos_x, new_pos_y] = obj
        else:
            pass
    
    def place_static_stone(self, obj):
        pos_x, pos_y = obj.get_pos()

        if self.position_is_appropriate(obj) == False:
            pos_x, pos_y = self.fix_to_correct_position(obj)
            obj.set_pos(pos_x, pos_y)

        self.grid[pos_x, pos_y] = obj
            


    def generate_grid(self):
        for x in range(0, self.grid_width, self.cell_width):
            for y in range(0, self.grid_height, self.cell_height):
                self.grid[x,y] = 'empty'

    def update(self):
        self.move_all_objects()

    def __init__(self, group, grid_width, grid_height, cell_width, cell_height):
        self.grid = {}
        self.grid_width = grid_width
        self.grid_height = grid_height
        self.cell_width = cell_width
        self.cell_height = cell_height

        self.objects_on_screen = []
        self.group = group

        # functions
        self.generate_grid()
