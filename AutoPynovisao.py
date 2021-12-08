###############################	código de automação de processos no software pynovisao	####################################

#	objetivo:	automatizar processos para acelerar a analise e comparação de algoritmos
#	processos: 	acesso aos apps, dataset, imagem, segmentação, extração, treinamento, classificação e análise
#	progresso: 	     100%	,  100%  , 100%  ,    100%    ,   80%   ,     100%   ,    100%      ,    20%






#libraries and dependencies
import os
import time
import math
import pyautogui


#constants
marking_qtd = 6									#cicle/image counter
dataset_path = '/home/edy/Downloads/pynovisao/pynovisao-master/data/DatasetArtigo' #dataset path
pynovisao_path = 'cd Downloads/pynovisao/pynovisao-master/src'			#pynovisao source folder
image_folder = '/home/edy/Downloads/pynovisao/pynovisao-master/data/DatasetArtigo' #images database
#image_path = '/home/edy/Downloads/pynovisao/pynovisao-master/data/DatasetArtigo/camaldulensis6.tif'
segment_number = '50'									#segmentation's superpixels number



print("verification: \n")								#starts terminal verification

#functions
def openTerminal(): #opening terminal
    pyautogui.hotkey('ctrl', 'alt', 't')						#open terminal command
    
    print("terminal opened")								#verification
    time.sleep(10)
    

def closeTerminal(): #closing pynovisao app
    time.sleep(1)
    pyautogui.click(x=50, y=200, button='right')					#open terminal menu
    time.sleep(1)
    pyautogui.click(x=200, y=120)							#show open windows
    time.sleep(1)
    pyautogui.click(x=340, y=105)							#show open windows
    time.sleep(1)
    pyautogui.hotkey('enter')								#choose window to close
    time.sleep(3)									#close app command	
    
    print("terminal closed \n\n\n\n")							#verification
    time.sleep(5)
    

def openPyno(): #open pynovisao app
    pyautogui.write('source pyno360/bin/activate')					#actvating virtual enviroment
    pyautogui.hotkey('enter')
    time.sleep(2)
    
    pyautogui.write(pynovisao_path)							#pynovisao path
    pyautogui.hotkey('enter')

    pyautogui.write('python3 main.py')						#opening pynovisao
    pyautogui.hotkey('enter')

    print("pynovisao opened")								#verification
    time.sleep(14)

def closePyno(): #closing terminal
    pyautogui.click(x=30, y=400)							#open terminal menu
    time.sleep(2)
    pyautogui.hotkey('alt','f4')							#show open windows
    time.sleep(2)
    pyautogui.hotkey('enter')								#choose window to close
    time.sleep(5)									#close app command
    
    print("pynovisao closed")								#verification
    time.sleep(2)

def setDataset(): #set user dataset
    pyautogui.hotkey('ctrl','d')							#dataset menu
    time.sleep(3)
    pyautogui.write(dataset_path) 							#dataset path string
    time.sleep(3)
    pyautogui.hotkey('enter')								#confirm dataset 
    time.sleep(1)
    pyautogui.hotkey('enter')								#confirm dataset 
    
    print("dataset opened")								#verification
    time.sleep(6)
    

def openImage(i): #open image file
    species_names = ['camaldulensis','citriodora', 'gg', 'grandis','saligna', 'urophylla'] #species names
    image_name = image_folder + "/" + species_names[i] + "/" + species_names[i] + "1.tif"   
    print(image_name)
    
    
    pyautogui.hotkey('ctrl', 'o')							#open image menu
    time.sleep(3)
    
    pyautogui.write(image_name)							#image path	
    time.sleep(2)
    pyautogui.hotkey('enter')								#confirm image 
    
    
    print("image opened")								#verification
    time.sleep(10)    				


def configSegmentation(): #configure slic to segment XX superpixels 
    pyautogui.click(x=115, y=315)
    pyautogui.hotkey('ctrl', 'g')							#open segmentation menu
    time.sleep(2)
    pyautogui.press(['backspace', 'backspace', 'backspace'])				#erase default segment number
    time.sleep(2)
    pyautogui.write(segment_number)							#write correct segment number
    time.sleep(2)
    pyautogui.hotkey('enter')   							#confirm
    
    print("segmentation configured")							#verification
    time.sleep(5)
    
def execSegmentation(): #executes segmentation
    pyautogui.click(clicks=2,x=200, y=570)						#set pyno to front
    pyautogui.hotkey('ctrl', 's')							#execution command
    
    time.sleep(3)
    pyautogui.click(x=660, y=580)							#cancelling image saving
    
    print("segmentation executed")							#verification
    time.sleep(7)
    
def segMarcation(xCen, yCen, class_number): #marks superpixels in circle format
    pyautogui.click(x=200, y=570)							#set pyno to front
    
    radius = 25									#circle radius marking

    class_h = [220, 250, 280, 310, 330, 360, 390]					#class buttons height
    yBut= class_h[class_number]							#objective class button height
    pyautogui.click(x=170, y=yBut)							#select class
	
    pyautogui.click(x=xCen, y=yCen)							#center pixel marking
    print("central sppx marked: (", xCen, ",", yCen, ")\n") 				#verification
    '''    
    '''
    angulo = 0
    for j in range(marking_qtd):							#marking loop
        print("angle: ", angulo)
        cosAng = math.cos(angulo)							#cos
        senAng = math.sin(angulo)							#sen
     
        print("cos: ", cosAng, "\nsen: ", senAng)					#verification
        
        xMarc = xCen+(radius*round(math.cos(round(math.radians(angulo),2))))		#x coordinate resolution
        yMarc = yCen+(radius*round(math.sin(round(math.radians(angulo),2))))		#y coordinate resolution
                					
        pyautogui.click(x=xMarc, y=yMarc)						#click confirm
        time.sleep(3)
        
        print(j+1, "º superpixel marked: (", xMarc, ",", yMarc, ")\n")		#verification
                
        angulo = angulo+ (360/marking_qtd)						#angle iteration
    
    print("\nradius: ", radius)							#verification
    time.sleep(10)
    
def execExtraction(): #executes extraction
    pyautogui.hotkey('ctrl', 'f')							#execution command
    
    print("extraction executed")							#verification
    time.sleep(40)
    
def configTraining(classif_name,): #configures training algorithms
    pyautogui.click(x=495, y=70)							#opens training menu
    time.sleep(1)		
    pyautogui.click(x=505, y=130)							#config training menu
    time.sleep(3)
    pyautogui.hotkey(['backspace', 'backspace', 'backspace'])
    pyautogui.write(classif_name, interval=0.1)					#choosing algorithm
    
    #estudar os parametros de cada algoritmo pra ca e pro artigo
    
    print("training configured")							#verification
    time.sleep(10)

def execTraining(): #executes training
    pyautogui.hotkey('ctrl', 't')							#execution command
    
    print("training executed")							#verification
    time.sleep(10)

def execClassification(): #executes classification
    pyautogui.hotkey('ctrl', 'c')							#executes classification
    
    print("classification executed")							#verification
    time.sleep(30)
    
def crossvalidation():
    pyautogui.hotkey('ctrl', 'x')							#executes cross validation
      
    print("cross validation executed")						#verification
    time.sleep(10)



######################################################MAIN

openTerminal()
openPyno()
setDataset()
openImage(0)						#camaldulensis
configSegmentation()
execSegmentation()
segMarcation(580, 345, 0)				#camaldulensis
execExtraction()
execTraining()
closeTerminal()


for k in range(1,6):

    openTerminal()
    openPyno()
    setDataset()
    openImage(k)					#['0camaldulensis','1citriodora', '2gg', '3grandis','4saligna', '5urophylla']
    configSegmentation()
    execSegmentation()
    segMarcation(580, 345, k)					
    execExtraction()
    closeTerminal()






'''







execSegmentation()
segMarcation(425, 280, 1)				#camaldulensis
execExtraction()
configTraining("RandomForest")

execTraining()
crossvalidation()


segMarcation(580, 345, 2)				#citriodora
segMarcation(765, 405, 3)				#gg
segMarcation( , , )					#grandis
segMarcation( , , )					#saligna
segMarcation( , , )					#urophylla
'''



#notes
'''

tested_imgs = 0 
tifs_number = 0									#tracking
species_number = 0									#tracking
species_names = ['camaldulensis','citriodora', 'gg', 'grandis','saligna', 'urophylla'] #species names
classif_names = ['SMO', 'RandomForest', 'J48', 'RandomCommittee']			#classification algorithms names


    if segment_number == "250":							#marcation range following segmentation complexity
        marcationCircles = 2	
    if segment_number == "500":
        marcationCircles = 4 
    if segment_number == "750":
        marcationCircles = 6
	    
    #for i in range(marcationCircles):						#marcation range loop
def getImageName(): #generates image name
    files = [f for f in os.listdir(dataset_folder) if os.path.isfile(f)]
    for f in files:
            tifs_number = tifs_number + 1
    
    specie = species_names[species_number]
    image_path = image_folder +'/'+ specie +'/'+ specie + file_number +'.tif'
	        #'/home/edy/Downloads/pynovisao/pynovisao-master/data/DatasetArtigo / camaldulensis / camaldulensis23.tif'
    tifs_number = tifs_number
    
    return image_name

def execExperimenter():
	

def readClassification(): #stores the result to make an average after
	
'''










