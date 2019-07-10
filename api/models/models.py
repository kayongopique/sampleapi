class WorkOrder:
    """
    Creates a work order model.
    """
    def __init__(self,title,description,workerid,deadline):
        self.title = title
        self.description = description
        self.deadline= deadline
        self.workerid = workerid
    

class Worker:
    """
    class creates a worker model.
    """
    def __init__(self,name,email,company):
        self.name = name
        self.email = email
        self.company = company
        
