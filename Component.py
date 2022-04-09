class Component:
    def __init__(self,id=0,nb_states=0,states = []):
        self.id = id
        self.nb_states = nb_states
        self.states = states
    
    def __str__(self):
        return "\tComponent_ID : " + str(self.id) + " Nb_States : " + str(self.nb_states) + " States " + str(self.states)
    