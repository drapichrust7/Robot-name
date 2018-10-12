import string, random, sys
class Robot():
    def __init__(self,robot_name='', names_list=[]):
        self.robot_name=robot_name
        self.names_list=names_list

    def generate_name(self,robot_name):
        char1=random.choice(string.ascii_uppercase)
        char2=random.choice(string.ascii_uppercase)
        int1=random.randint(0,9)
        int2=random.randint(0,9)
        char3=random.choice(string.ascii_uppercase)
        char4=random.choice(string.ascii_uppercase)
        #self.robot_name=char1+char2+str(int1)+str(int2)+char3+char4
        self.robot_name='Roki'
        
    
    def save_name(self):
        if self.robot_name in self.names_list:
            print('Robot '+self.robot_name+' już istnieje')
        else:           
            self.names_list.append(self.robot_name)
            print('Dodano robota '+self.robot_name)
       
    def wipe_name(self, robot_name):
        if robot_name not in self.names_list:
            print('Robot '+robot_name+' nie istnieje')
        else:
            self.names_list.remove(robot_name)
            print('Usunięto robota '+robot_name)


myRobot=Robot()
while True:
    print('1.Dodaj robota\n2.Usuń robota\n3.Wyświetl listę\n4.Wyjdź')
    action=input()
    if action=='1':
        myRobot.generate_name('')
        myRobot.save_name()
    if action=='2':
        print('Wprowadź nazwę')
        name=input()
        myRobot.wipe_name(name)
    elif action=='3':
        print('Lista robotów \n'+str(myRobot.names_list))
    elif action=='4':
        print('Koniec')
        break


