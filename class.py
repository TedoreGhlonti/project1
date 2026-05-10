class Robot:
    def action(self):
        
        return "I am a robot, I help people."
    
class CleanerRobot(Robot):
    def action(self):
        return "I am cleaning the floor."
    
class CookRobot(Robot):

    def action(self):
        return "I am cooking dinner."
    

basic_robot = Robot()
cool_robot = CleanerRobot()
other_robot = CookRobot()

print(basic_robot.action())
print(cool_robot.action())
print(other_robot.action())
        


        
        
        
        
        

        


        
        

        

        
        
        