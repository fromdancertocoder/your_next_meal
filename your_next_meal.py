class Treenode:
    def __init__(self, name, blerb, cost = None, style = None,):
        self.name = name
        self.blerb = blerb
        self.cost = cost
        self.style = style
        self.children = []    
    
    def add_child(self, node):    
        self.children.append(node)

    def add_restaurant(self, node):
        current_node = self
        index = len(node.cost)
        index -= 1
        next_node = current_node.children[index]
        current_node = next_node
        if node.style == "American":
            next_node = current_node.children[0]
        elif node.style == "Asian":
            next_node = current_node.children[1]
        elif node.style == "TexMex":
            next_node = current_node.children[2]
        elif node.style == "French":
            next_node = current_node.children[3]
        elif node.style == "Italian":
            next_node = current_node.children[4]                        
        current_node = next_node
        current_node.add_child(node)

    def traverse(self, level = 0):
        current_node = self
        while level < 2:
            print(current_node.blerb)
            decision  = int(input("make your selection: "))
            if decision <= len(current_node.children):
                index = decision - 1
                next_node = current_node.children[index]
                current_node = next_node
                level += 1
            else:
                print("invalid choice. Try again")
                continue
        if len(current_node.children) == 0:
            print("no restaurants fit your request... sorry... good bye")
            return    
        print(current_node.blerb)
        while True: 
          for node in current_node.children:
              print(node.name)
          more = input("type a restaurant's name for more info or end to stop \n")
          if more.lower() == "end":
              print("Thank you for using Your Next Meal")
              break

          for node in current_node.children:
              if node.name.lower() == more:
                  print(node.blerb)
                       



                



intro_blerb = """
welcome Your Next Meal!
what is your price range for this meal
1: cheap
2: moderate
3: expensive"""

type_blerb = """
what type of cusine would you like?
1: American
2: Asian
3: TexMex
4: French
5: Italian"""

final_blerb = """
the following restaunts fit your style and price range
type the name of the restautant for more info"""
# database of nodes starting at the root
root_node = Treenode("root", intro_blerb)

cheap = Treenode("cheap", type_blerb)
moderate = Treenode("moderate", type_blerb)
expensive = Treenode("expensive", type_blerb)
american_cheap = Treenode("American", final_blerb)
texmex_cheap = Treenode("TexMex", final_blerb)
asian_cheap = Treenode("Asian", final_blerb)
french_cheap = Treenode("French", final_blerb)
italian_cheap = Treenode("Italian", final_blerb)
american_moderate = Treenode("American", final_blerb)
asian_moderate = Treenode("Asian", final_blerb)
texMex_moderate = Treenode("texmex", final_blerb)
french_moderate = Treenode("French", final_blerb)
italian_moderate = Treenode("Italian", final_blerb)
american_expensive = Treenode("American", final_blerb)
asian_expensive = Treenode("Asian", final_blerb)
texmex_expensive = Treenode("TexMex", final_blerb)
french_expensive = Treenode("French", final_blerb)
italian_expensive = Treenode("Italian", final_blerb)

taco_bell = Treenode("Taco Bell", "you know it, you both love it and hate it", "$", "TexMex")
mcdonalds = Treenode("McDonalds", "MMMMM...ya know not sure if i'm lovin it", "$", "American")
silk_road = Treenode("Silk Road", "we serve you sushi hundereds of miles from the ocean", "$$", "Asian")

#adding base nodes
root_node.add_child(cheap)
root_node.add_child(moderate)
root_node.add_child(expensive)
cheap.add_child(american_cheap)
cheap.add_child(asian_cheap)
cheap.add_child(texmex_cheap)
cheap.add_child(french_cheap)
cheap.add_child(italian_cheap)
moderate.add_child(american_moderate)
moderate.add_child(asian_moderate)
moderate.add_child(texMex_moderate)
moderate.add_child(french_moderate)
moderate.add_child(italian_moderate)
expensive.add_child(american_expensive)
expensive.add_child(asian_expensive)
expensive.add_child(texmex_expensive)
expensive.add_child(french_expensive)
expensive.add_child(italian_expensive)
#adding restautants
root_node.add_restaurant(taco_bell)
root_node.add_restaurant(mcdonalds)
root_node.add_restaurant(silk_road)
# calling the function
root_node.traverse()
