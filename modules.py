class exponentials:
    def __init__(self, e, x):
        self.e = e
        self.x = x
    def exponent(self):
        result = 1
        for i in range(self.x):
            result *= self.e
        return result

class power_arrays:
    def __init__(self, arr, powers):
        self.arr = arr
        self.powers = powers
    def power(self):
        arr1 = []
        #for i in self.arr:
        #    arr1.append(i**self.powers) 
        arr1 = [i**self.powers for i in self.arr]
        return arr1

class subsequency:
    def __init__(self, arr, sequence):
        self.arr = arr
        self.sequence = sequence
    def isSubsequent(self):
        seqIdx = 0
        for i in self.arr:
            if seqIdx == len(self.sequence):
                break
            if self.sequence[seqIdx] == i:
                seqIdx += 1
        return seqIdx == len(self.sequence)

class fibonacci:
    def __init__(self, n):
        self.n = n
    # Using memoization with python dictionary to remember values existing in the dict # super fast
    def fib(self, memo={}):
        if self.n in memo: return memo[self.n]
        if self.n<=2: return 1
        memo[self.n] =  fibonacci(self.n-1).fib() + fibonacci(self.n-2).fib()
        return memo[self.n]

class gridTraveller:
    def __init__(self, y, x):        
        self.x = x
        self.y = y
    def travel(self, memo={}):
        if (self.y,self.x) in memo: return memo[(self.y, self.x)]
        if self.y==0 or self.x==0: return 0
        if self.y==1 and self.x==1: return 1
        memo[self.y, self.x] = gridTraveller(self.y-1, self.x).travel(memo) + gridTraveller(self.y, self.x-1).travel(memo)
        return memo[(self.y, self.x)]

class canSum:
    def __init__(self, targetSum, array):
        self.targetSum = targetSum
        self.array = array
    def boolSum(self, memo={}):  
        if self.targetSum in memo: return memo[self.targetSum]
        if self.targetSum==0: 
            return True 
        if self.targetSum<0: 
            return False 
        for i in self.array:
            self.targetSum = self.targetSum - i
            if canSum(self.targetSum, self.array).boolSum(memo)==True:
                memo[self.targetSum] = True
                return True 

        memo[self.targetSum] = False
        return False 

class combine:
    def __init__(self, sum, array1):
        self.sum = sum
        self.array1 = array1
    def howSum(self, memo={}):   #, 
        if self.sum in memo: return memo[self.sum]
        if self.sum ==0: return []
        if self.sum < 0 : return None
        for i in self.array1:
            self.sum -= i
            x = combine(self.sum, self.array1).howSum(memo)
            if  x != None:
                memo[self.sum] = [*x, i]
                return memo[self.sum]
        memo[self.sum] = None
        return memo[self.sum]

class anagram:
    def __init__(self, s1, s2):
        self.s1 = s1
        self.s2 = s2
    def isAnagram(self):
        self.s1 = sorted(self.s1.lower())
        self.s2 = sorted(self.s2.lower())
        if len(self.s1)==len(self.s2):
            for i, j in zip(self.s1, self.s2):
                if i!=j:
                    return "It is not an Anagram"
            
            return "It is an Anagram"
        else:
            return "It is not an Anagram"
            
class primeNumber:
    def __init__(self, arry):
        self.arry = arry
    def isPrime(self):
        for i in range(2, self.arry):
            if self.arry % i == 0:
                return False
        return True

class findIndex:
    def __init__(self, my_array, my_number):
        self.my_array = my_array
        self.my_number = my_number
    def one_dimension(self):
        count  = 0
        for i in self.my_array:
            if i==self.my_number:
                return count
            else:
                count+= 1
        return(f"{self.my_number} is not in iterable")
    def two_dimension(self):
        count = 0
        for i in (self.my_array[j] for j in range(len(self.my_array))):
            if self.my_number in i:
                return(count, i.index(self.my_number))
                
            else:
                count += 1
        return (f"{self.my_number} is not in iterable")
import random
class shuffleCards:
    
    def __init__(self, cards):
        self.cards = cards
    def shuffling(self):
        x = list(random.shuffle(self.cards))
        c = []
        for i in x:
            c.append(i)
        return c
import urllib.request
import subprocess
import socket
import os

#import scapy.all as scapy
class InternetDetails():
    def __init__(self):
        pass
    def availableNetworks(self):
        ## shows all the wifi networks arounds
        try:
            devices = subprocess.check_output(['netsh', 'wlan', 'show', 'network'])
            devices = devices.decode('utf-8').split("\n")
            net_type,auth,ssid = "Network type","Authentication","SSID"
            for x in devices:
                for i,n in zip(x, range(len(x))):
                    if i.isdigit() and n==10:
                        print(f"There are {i} available networks\n")
                        break
                if ssid in x or net_type in x or auth in x:
                    print(x)
        except:
            return "No available WiFi nearby. Consider checking your internet connectivity."
    def connectKnownWifi(self, wifi_name):
        ## connect your device to any known networks
        try:
            os.system('cmd /c "netsh wlan show networks"')
            os.system('cmd /c "netsh wlan connect name={}"'.format(wifi_name))
        except:
            return("Create a new connection")
    def hasInternet(self, host='https://google.com'):
        ## check if your wifi supports browsing or is connected to the internet
        try:
            urllib.request.urlopen(host)    #this module prompts the browser to open any website
            return True                     # if it's opened then your wifi has internet else the except clause is executed
        except:
            return False
    def getIp(self):
        ## get your current ip address
        try:
            return socket.gethostbyname(socket.gethostname())       ##this function gets your current ip address
        except:
            return "127.0.0.1"                  ###if there is no network your default ip address is the one of your local host machine

    
    def showWifiProfile(self, wifi_name):
        ####get the profile details of any known wifi network 
        data = subprocess.check_output(["netsh", "wlan", "show", "profiles", wifi_name]).decode("utf-8").split("\n")    ###gives the entire data
        for i in data:
            name,types, ssids,radio,cost="Name", "Type","SSID name","Radio type","Cost"         ##we choose to minimize it into a more readable format
            if name in i or types in i or ssids in i or radio in i or cost in i:                ##including the most important details
                print(i)
    def showPasswords(self):
        ###show passowrds of all the wifi networks you have ever connected to
        data = subprocess.check_output(["netsh", "wlan", "show", "profiles"]).decode("utf-8").split("\n")
        profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]         ###we collect a list of all the wifi networks we have
        for i in profiles:                                                                     ##ever connected to
            results = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles', i, "key=clear"]).decode("utf-8").split("\n")    ##key=clear helps to
            results = [x.split(":")[1][1:-1] for x in results if "Key Content" in x]                        ##to make the password visible
            try:
                print("{:<30} |   {:<}".format(i, results[0]))
            except IndexError:
                print("{:<30} |   {:<}".format(i, ""))

class readCsvFiles():
    def __init__(self, path_name):
        self.path_name = path_name
    def get_headers(self, file):
        return file[0].strip().split(",")
    def convert_file_list(self, files):
        values = []
        for x in range(len(files)):
            if x==0:
                continue
            else:
                values.append(files[x].strip().split(','))
        return values
    def convert_items_float(self, ln):
        for x in range(len(ln)):
            for i in range(len(ln[x])):
                if ln[x][i]=="":
                    ln[x][i]="0"
                    ln[x][i] = float(ln[x][i])
                else:
                    ln[x][i] = float(ln[x][i])
        return ln
    def convert_list_dict(self, ln):
        total_loans=[]
        headers = readCsvFiles.get_headers(self,ln)
        for x in range(0, len(ln)):
            ln2={}
            for n in range(0, len(ln[x])):
                ln2[headers[n]] = ln[x][n]
            total_loans.append(ln2)
        return total_loans
    def read_csv(self,id=0):
        with open(self.path_name, 'r') as f:
            loan = f.readlines()
            if id==0: return readCsvFiles.get_headers(self,loan)
            elif id==1:  
                loan = readCsvFiles.convert_file_list(self,loan)
                return loan
            elif id==2:
                loan = readCsvFiles.convert_file_list(self,loan)
                loan = readCsvFiles.convert_items_float(self,loan)
                return loan
            elif id==3:
                loan = readCsvFiles.convert_file_list(self,loan)
                loan = readCsvFiles.convert_items_float(self,loan)
                loan = readCsvFiles.convert_list_dict(self,loan)
                return loan
            else:
                return "ID doesn't exist"
