import random


def apply_production_rule(grammar, text, index):
    results = set()
    if not text[index].isupper():
        results.add(text)
    else:
        prefix = text[:index]
        suffix = text[index+1:]
        for rule in grammar.rules[text[index]]:
            if rule == "#":
                new_text = prefix + suffix 
            else:
                new_text = prefix + rule + suffix 
            new_text = new_text.replace("#", "") 
            results.add(new_text)
    return results

def rightmost_derivation(grammar, text):
    for i in range(len(text)-1, -1, -1):
        if text[i].isupper():
            return apply_production_rule(grammar, text, i)

def leftmost_derivation(grammar, text):
    for i in range(len(text)):
        if text[i].isupper():
            return apply_production_rule(grammar, text, i)

def display_sample_outputs(grammar):
    all_strings = create_all_strings(grammar, grammar.start_symbol, 10)
    for i in range(0, 5):
        print(list(all_strings)[random.randint(0, len(all_strings)-1)])

def create_all_strings(grammar, current, limit):
    if len(current) > limit:
        return set()

    possible_expansions = set()
    has_variables = False
    
    for i in range(len(current)):
        if current[i].isupper():
            has_variables = True
            possible_expansions = possible_expansions.union(apply_production_rule(grammar, current, i))
    
    if not has_variables:
        result_set = set()
        result_set.add(current)
        return result_set 
    else:
        final_results = set()
        for expansion in possible_expansions:
            final_results = final_results | create_all_strings(grammar, expansion, limit)
        return final_results

def verify_string_membership(grammar, current_form, depth_limit, target_string):
    global path_trace

    if len(current_form) > depth_limit:
        return False

    expansion_set = set()
    has_variables = False
    
    for i in range(len(current_form)):
        if current_form[i].isupper():
            has_variables = True
            expansion_set = expansion_set.union(apply_production_rule(grammar, current_form, i))
    
    if not has_variables:
        if target_string == current_form:
            path_trace = current_form
            return True 
    else:
        for expansion in expansion_set:
            if verify_string_membership(grammar, expansion, depth_limit, target_string):
                path_trace = current_form + " -> " + path_trace
                return True

    return False

class ContextFreeGrammar:
    def __init__(self):
        self.terminal_symbols = set()
        self.variable_symbols = set()
        self.rules = dict()
        self.start_symbol = ''

    def display_grammar(self):
        print("start: ", self.start_symbol)
        print("variables: ", self.variable_symbols)
        print("terminals: ", self.terminal_symbols)
        print("productions:")
        for variable in self.rules:
            print("    ", variable, " ---> ", self.rules[variable])

    def include_terminal(self, symbol):
        if symbol not in self.terminal_symbols:
            self.terminal_symbols.add(symbol)

    def include_variable(self, symbol):
        if symbol not in self.variable_symbols:
            self.variable_symbols.add(symbol)
    
    def define_start_symbol(self, symbol):
        self.start_symbol = symbol

    def include_rule(self, rule_string):
        rule_string = rule_string.strip()
        left_side = rule_string[0:1]
        self.include_variable(left_side)

        if left_side not in self.rules:
            self.rules[left_side] = set()

        rule_string = rule_string[1:]
        rule_string = rule_string.strip(" ")
        rule_string = rule_string.split("->")

        for part in rule_string:
            if part != "":
                part = part.split("|")
                for production in part:
                    production = production.strip()
                    if production != "":
                        self.rules[left_side].add(production)
                        for character in production:
                            if character.isupper():
                                self.include_variable(character)
                            else:
                                self.include_terminal(character)

    def read_grammar(self):
        print("-----Grammar Input-----")
        
        print("\nSpecify the start symbol:")
        symbol = input()
        self.define_start_symbol(symbol)
        
        print("\nInput production rules: (format: S -> aA | bbB, use # for epsilon, press Enter when finished)")
        rule = input()
        while rule != "":
            self.include_rule(rule)
            rule = input()

        print("----------------------")

def sample_grammar_setup(grammar):
    if True: 
        grammar.define_start_symbol("S")
        grammar.include_rule("S -> aSd | A ")
        grammar.include_rule("A -> bAcc | bcc ")

path_trace = ""
cfg = ContextFreeGrammar()

cfg.read_grammar()

print("\nSample strings from the grammar...")
display_sample_outputs(cfg)

print("\nProvide a string to trace its derivation...")
input_string = input()
if not verify_string_membership(cfg, cfg.start_symbol, 12, input_string):
    print("String is not generated by this grammar")
else: 
    print(path_trace)

print("\nProvide a string to verify membership...")
input_string = input()
if not verify_string_membership(cfg, cfg.start_symbol, 12, input_string):
    print("String is not generated by this grammar")
else: 
    print("String belongs to the grammar")
