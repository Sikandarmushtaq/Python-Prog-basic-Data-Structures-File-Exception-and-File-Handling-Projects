#functions postional arguments default arguments keyword arguments]


def adddition(a,b,c):    #posttion argument mey agr ham ney parameter mey 4 vaalue receive kar rahi hai lakin 
    #ham arguments mey 3 value bhj rahy hai to postional argument ka error aye ga 
    print(a+b+c)
adddition(1,2,3)


def multiply(a,b=3):   #yah par argument mey ham khud sey value rakh skty hai agr ham koi value ni dyna ch aray
    #argument sey parameter mey to koi error ni aye ga sy khty hai defaut arguments
    print(a+b)
multiply(1)

def subtract(a,b): #keyword argument mey ham agr chty hai k parameter mey ham ju vale rakhy vo phly b ko jaye then a
    #ko by default value phly a ko jaye gi phir b ko lakin ham agr argyment mey value assign kar dy to ham jis nam sey 
    #parameter mey rakha ha variable osi nam sey paramter mey osy phly rakh k tu named ya keyword arguments dy skty hai 
    print(b-a)
subtract(b=2,a=1)