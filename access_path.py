"Author: Matin"

from capstone import takeCommand, speak
import os
import shutil

class OS_PATH():
    DIR = ""
    last_query = ""
    def __init__(self, path = "C:"):
        self.DIR = path
    
    def Start(self):
        query = ""
        while(True):
            if("list contents" in query):
                self.list_dir_contents()
            elif("change directory" in query):
                content = self.list_dir_contents()
                content[len(content.keys())+2] = 'Go back...'
                speak("tell me which folder number you want to move to.")
                print("tell me which folder number you want to move to.")

                #command = takeCommand().lower()
                command = input("change dir")
                if(int(command) in content.keys()):
                    self.change_dir(content[int(command)])
                else:
                    speak("please tell the correct option")

            elif("delete" in query and "file" in query):
                content = self.list_dir_contents()
                speak("tell me which file number you want to delete.")
                print("tell me which file number you want to delete.")

                #command = takeCommand().lower()
                command = input("delete")
                if(int(command) in content.keys()):
                    self.remove_file(content[int(command)])
                else:
                    speak("please tell the correct option")

            elif("delete" in query and "folder" in query):
                content = self.list_dir_contents()
                speak("tell me which folder number you want to delete.")
                print("tell me which folder number you want to delete.")

                #command = takeCommand().lower()
                command = input("delete")
                if(int(command) in content.keys()):
                    self.remove_folder(content[int(command)])
                else:
                    speak("please tell the correct option")

            elif("stop" in query):
                break

            speak("tell me what we have to do.")
            query = takeCommand().lower()

    def change_dir(self, folder_name = ""):
        if(folder_name == ""):
            speak("Specify the folder name Sir.")
            print("Specify the folder name Sir.")
        elif(os.path.isdir(self.DIR+"\\"+folder_name)):
            self.DIR = self.DIR+"\\"+folder_name
            speak("changed the directory.")
            print(self.DIR)
        elif(folder_name == "Go back..."):
            self.DIR = os.path.dirname(self.DIR)
            speak("changed the directory.")
            print(self.DIR)

    def list_dir_contents(self):
        Content = {}
        c = 1
        for i in os.listdir(self.DIR):
            print(c, ". "+i)
            Content[c] = i
            c += 1
        return Content


    def remove_file(self, file_name = ""):
        if(file_name == "" or "." not in file_name):
            speak("Specify the file name Sir.")
            print("Specify the file name Sir.")
        elif(os.path.exists(self.DIR+"\\"+file_name)):
            speak("Do you want to delete the file "+file_name)
            print("Do you want to delete the file "+file_name)
            print("waiting for confirmation.....say yes or no.")
            command = takeCommand().lower()
           
            while('yes' not in command and 'no' not in command):
                command = takeCommand().lower()
                
            if('yes' in command):
                
                os.remove(self.DIR+"\\"+file_name)
                speak("deleted the file "+file_name)
        else:
            speak("I think the file do not exist sir. Look whether we are in the right directory.")
            print(self.DIR)

    def remove_folder(self, folder_name = ""):
        if(folder_name == ""):
            speak("Specify the folder name Sir.")
            print("Specify the folder name Sir.")
        elif(os.path.exists(self.DIR+"\\"+folder_name)):
            speak("Do you want to delete the folder "+folder_name)
            print("Do you want to delete the folder "+folder_name)
            print("waiting for confirmation.....say yes or no.")
            command = takeCommand().lower()
            
            while('yes' not in command and 'no' not in command):
                command = takeCommand().lower()
                
            if('yes' in command):
                shutil.rmtree(self.DIR+"\\"+folder_name)
                speak("deleted the folder "+folder_name)
        else:
            speak("I think the folder do not exist sir. Look whether we are in the right directory.")
            print(self.DIR)

    
            

if __name__ == '__main__':
    obj = OS_PATH("E:\\")
    obj.Start()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    