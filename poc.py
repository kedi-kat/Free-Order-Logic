class FOL_Interpreter:
    def __init__(self):
        # This is our "Memory" (The Bag)
        self.memory = {}
        self.buffer = {"action": None, "target": None, "value": None}

    def reset_buffer(self):
        self.buffer = {"action": None, "target": None, "value": None}

    def parse_token(self, token):
        # LOGIC: Check the SUFFIX, not the position.
        parts = token.split('.')
        
        # 1. Check for Values (.int, .str)
        if "int" in parts:
            # "Value.int.5" -> We grab the last part "5"
            self.buffer["value"] = int(parts[-1])
            return "Found Value"
            
        # 2. Check for Targets (.x, .y, .log)
        if "x" in parts:
            self.buffer["target"] = "x"
            return "Found Target X"
        if "y" in parts:
            self.buffer["target"] = "y"
            return "Found Target Y"
            
        # 3. Check for Actions (.set, .print, .add)
        if "set" in parts:
            self.buffer["action"] = "SET"
            return "Found Action SET"
        if "print" in parts:
            self.buffer["action"] = "PRINT"
            return "Found Action PRINT"

    def execute_sentence(self, sentence):
        print(f"\n--- Processing: '{sentence}' ---")
        self.reset_buffer()
        
        # STEP 1: SCATTER (Split by space)
        tokens = sentence.split()
        
        # STEP 2: GATHER (Identify parts by suffix, ignore order)
        for token in tokens:
            self.parse_token(token)
            
        # STEP 3: EXECUTE (Run logic only if parts exist)
        if self.buffer["action"] == "SET":
            target = self.buffer["target"]
            val = self.buffer["value"]
            self.memory[target] = val
            print(f"✅ SUCCESS: Set memory '{target}' to {val}")
            
        elif self.buffer["action"] == "PRINT":
            target = self.buffer["target"]
            if target in self.memory:
                print(f"🖨️ OUTPUT: Variable '{target}' is {self.memory[target]}")
            else:
                print(f"⚠️ ERROR: Target '{target}' is empty (.void)")

# =========================================
#  THE TEST 
# ==========================================
interpreter = FOL_Interpreter()

# Test 1: Standard Order (Settler Logic)
interpreter.execute_sentence("Target.x Value.int.10 Action.set")

# Test 2: Chaotic Order (Nomad Logic) - REVERSE
interpreter.execute_sentence("Action.set Value.int.99 Target.x")

# Test 3: Total Shuffle 
interpreter.execute_sentence("Value.int.500 Action.set Target.y")

# Test 4: Print the results (Order doesn't matter here either)
interpreter.execute_sentence("Target.x Action.print")
interpreter.execute_sentence("Action.print Target.y")
