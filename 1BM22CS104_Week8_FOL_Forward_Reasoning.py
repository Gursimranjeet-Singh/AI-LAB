class KnowledgeBase:
    def __init__(self):
        self.american = set()  
        self.hostile = set()  
        self.sold = set()      
        self.criminal = set()  
    
    def add_american(self, person):
        self.american.add(person)
        print(f"Added to American citizens: {person}")
    
    def add_hostile(self, country):
        self.hostile.add(country)
        print(f"Added to hostile countries: {country}")
    
    def add_sold(self, weapon, seller, buyer):
        self.sold.add((weapon, seller, buyer))
        print(f"Added sale: {seller} sold {weapon} to {buyer}")
    
    def check_crime(self, seller, buyer):
        if seller in self.american and buyer in self.hostile:
            return True
        return False

    def forward_reasoning(self):
        for weapon, seller, buyer in self.sold:
            print(f"\nChecking sale: {seller} sold {weapon} to {buyer}")
            
            if self.check_crime(seller, buyer):
                print(f"Crime detected! {seller} is a criminal because they sold weapons to a hostile nation.")
                self.criminal.add(seller)
            else:
                print(f"No crime detected for {seller}.")

    def is_criminal(self, person):
        return person in self.criminal


kb = KnowledgeBase()

kb.add_american("Robert")  
kb.add_hostile("A")       
kb.add_sold("Missiles", "Robert", "A")  

kb.forward_reasoning()

if kb.is_criminal("Robert"):
    print("\nRobert is a criminal.")
else:
    print("\nRobert is not a criminal.")
