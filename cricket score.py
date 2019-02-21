class cricket:
    run=0
    def __init__(self,name,run):
        self.name=name
        self.run=run
    def total_run(self):
        for i in self.run:
            run=run+1
        print run
    def Player_name(self):
        for i in self.name:
            print i
c=cricket("virat",100)
d=cricket("sachin",200)
c.total_run()
c.player_name()
d.total_run()
d.player_name()
