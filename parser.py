# parser.py - The Reader for Free-Order Logic

class FolNode:
    def __init__(self, root):
        self.root = root        # The main thing (e.g., "Motor")
        self.role = None        # .s (Subject) or .o (Object)
        self.state = []         # .hot, .void, etc.
        self.location = None    # .l (Location)

    def __repr__(self):
        # This tells Python how to print the node nicely
        return f"FOL_NODE[ Root: '{self.root}' | Role: {self.role} | Tags: {self.state} ]"

def parse(text):
    print(f"--- Reading: {text} ---")
    
    # Step 1: Chop the snake (Split by dots)
    parts = text.split('.')
    
    # The first piece is ALWAYS the Root
    root_word = parts[0]
    node = FolNode(root_word)
    
    # Step 2: Analyze the Suffixes
    for suffix in parts[1:]:
        if suffix == 's':
            node.role = "SUBJECT"
        elif suffix == 'o':
            node.role = "OBJECT"
        elif suffix == 'l':
            node.role = "LOCATION"
        elif suffix == 't':
            node.state.append("VOLATILE")
        elif suffix == 'void':
            node.state.append("EMPTY")
        else:
            # Unknown tags get added as generic states (like 'hot' or 'fast')
            node.state.append(suffix)
            
    return node

# --- THE TEST ZONE ---
if __name__ == "__main__":
    # Test 1: The Motor Example
    print(parse("Motor.s.hot.t"))
    
    # Test 2: The Mars Rover Example
    print(parse("Rover.s.Mars.l.fast.t.collect.o"))
